#!/home/abyot/miniconda3/envs/vcflibnew/bin/python
import argparse
import subprocess
from io import StringIO
import pandas as pd
import os
import time
import shutil
import uuid
import re
from concurrent.futures import ProcessPoolExecutor, as_completed

TEMP_BASE = '/dev/shm'
AVAILABLE_CORES = os.cpu_count() or 1
NUM_WORKERS = AVAILABLE_CORES


def get_chromosome_mapping(vcf_chroms, ref_fai_path):
    """
    Create a mapping between VCF chromosome names and reference chromosome names.
    Handles common naming convention mismatches:
    - chr1 <-> 1 <-> NC_* (NCBI accession)
    Returns a dict mapping VCF chrom names to reference chrom names, or None if no mapping needed.
    """
    ref_chroms = []
    if os.path.exists(ref_fai_path):
        with open(ref_fai_path, 'r') as f:
            for line in f:
                parts = line.strip().split('\t')
                if parts:
                    ref_chroms.append(parts[0])

    if not ref_chroms:
        return None

    vcf_set = set(vcf_chroms)
    ref_set = set(ref_chroms)
    if vcf_set & ref_set:
        return None

    def extract_chrom_number(name):
        """Extract chromosome number from various naming formats."""
        name = str(name)
        match = re.search(r'chr(\d+|[XYM]|MT)', name, re.IGNORECASE)
        if match:
            return match.group(1).upper()
        match = re.search(r'^(\d+|[XYM]|MT)$', name, re.IGNORECASE)
        if match:
            return match.group(1).upper()
        return None

    mapping = {}
    ref_by_number = {}
    for ref_name in ref_chroms:
        num = extract_chrom_number(ref_name)
        if num:
            ref_by_number[num] = ref_name

    for vcf_name in vcf_chroms:
        num = extract_chrom_number(vcf_name)
        if num and num in ref_by_number:
            mapping[vcf_name] = ref_by_number[num]
    if not mapping:
        vcf_numbered = []
        for vcf_name in vcf_chroms:
            num = extract_chrom_number(vcf_name)
            if num and num.isdigit():
                vcf_numbered.append((int(num), vcf_name))
        vcf_numbered.sort()

        ref_accessions = [r for r in ref_chroms if r.startswith(('NC_', 'NW_', 'NT_'))]

        if len(vcf_numbered) > 0 and len(ref_accessions) >= len(vcf_numbered):
            for i, (_, vcf_name) in enumerate(vcf_numbered):
                if i < len(ref_accessions):
                    mapping[vcf_name] = ref_accessions[i]

    if mapping:
        print(f"Detected chromosome naming mismatch. Created mapping for {len(mapping)} chromosomes.")
        sample = list(mapping.items())[:3]
        for vcf_name, ref_name in sample:
            print(f"  {vcf_name} -> {ref_name}")
        if len(mapping) > 3:
            print(f"  ... and {len(mapping) - 3} more")
        return mapping

    return None


def rename_vcf_chromosomes(input_vcf, output_vcf, chrom_mapping, temp_dir):
    """
    Rename chromosomes in VCF file using bcftools annotate --rename-chrs.
    Returns the path to the renamed VCF file, or input_vcf if no renaming needed.
    """
    if not chrom_mapping:
        return input_vcf
    rename_file = os.path.join(temp_dir, 'chrom_rename.txt')
    with open(rename_file, 'w') as f:
        for old_name, new_name in chrom_mapping.items():
            f.write(f"{old_name}\t{new_name}\n")

    print("Renaming chromosomes in VCF file...")
    try:
        cmd = ['bcftools', 'annotate', '--rename-chrs', rename_file, '-Oz', '-o', output_vcf, input_vcf]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Warning: bcftools annotate failed: {result.stderr}")
            return input_vcf

        subprocess.run(['tabix', '-p', 'vcf', output_vcf], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Chromosomes renamed successfully.")
        return output_vcf
    except Exception as e:
        print(f"Warning: Failed to rename chromosomes: {e}")
        return input_vcf
    finally:
        if os.path.exists(rename_file):
            os.remove(rename_file)

def run_cas_offinder(args):
    """
    Run cas-offinder on a single fasta file.
    """
    fasta_file, temp_dir, query_input_template, device_id = args

    try:
        target_path = os.path.join(temp_dir, fasta_file)
        query_input_path = os.path.join(temp_dir, f"query_{fasta_file}.txt")
        lines = query_input_template.copy()
        lines.insert(0, target_path + '\n')

        with open(query_input_path, 'w') as f:
            f.writelines(lines)

        off_target_output = os.path.join(temp_dir, fasta_file + '.txt')
        off_target_cmd = ['./cas-offinder', query_input_path, device_id, off_target_output]
        result = subprocess.run(off_target_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if os.path.exists(query_input_path):
            os.remove(query_input_path)

        return {
            'success': result.returncode == 0,
            'fasta_file': fasta_file,
            'output_file': off_target_output
        }
    except Exception as e:
        return {
            'success': False,
            'fasta_file': fasta_file,
            'error': str(e)
        }


def process_chromosome_pipeline(args):
    """
    Process a single chromosome through the entire pipeline:
    extract -> vcfallelicprimitives -> norm -> vcfcreatemulti -> bgzip -> vcf2fasta
    Must be at module level for pickling.
    """
    input_vcf, chrom, ref_path, temp_dir, fasta_prefix = args

    try:
        input_vcf_basename = os.path.basename(input_vcf)
        chrom_vcf = os.path.join(temp_dir, f"{input_vcf_basename}{chrom}.vcf.gz")
        processed_vcf = os.path.join(temp_dir, f"output_{input_vcf_basename}{chrom}.vcf.gz")
        chrom_uncompressed = os.path.join(temp_dir, f"{input_vcf_basename}{chrom}.vcf")
        extract_cmd = ["bcftools", "view", "-o", chrom_uncompressed, input_vcf, chrom]
        result = subprocess.run(extract_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            return {'success': False, 'chrom': chrom, 'error': f'Extract failed: {result.stderr}'}

        if not os.path.exists(chrom_uncompressed) or os.path.getsize(chrom_uncompressed) < 100:
            return {'success': False, 'chrom': chrom, 'error': 'No data for chromosome'}

        processed_uncompressed = os.path.join(temp_dir, f"output_{input_vcf_basename}{chrom}.vcf")

        vcfallelic = ["vcfallelicprimitives", chrom_uncompressed]
        norm = ["bcftools", "norm", "-m-"]
        vcfcreatemulti = ["vcfcreatemulti"]

        with open(processed_uncompressed, 'w') as out_handle:
            p1 = subprocess.Popen(vcfallelic, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p2 = subprocess.Popen(norm, stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p3 = subprocess.Popen(vcfcreatemulti, stdin=p2.stdout, stdout=out_handle, stderr=subprocess.PIPE)
            p1.stdout.close()
            p2.stdout.close()
            p3.communicate()

        if not os.path.exists(processed_uncompressed) or os.path.getsize(processed_uncompressed) < 100:
            processed_uncompressed = chrom_uncompressed
        chrom_fasta_prefix = os.path.join(temp_dir, f"{input_vcf_basename}{chrom}.fasta")
        vcf2fasta_cmd = ['vcf2fasta', '-f', ref_path, '-p', chrom_fasta_prefix, '-n', 'NAN', processed_uncompressed]
        result = subprocess.run(vcf2fasta_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        files_to_cleanup = [chrom_vcf, chrom_vcf + '.csi', processed_vcf, processed_vcf + '.csi',
                           processed_vcf + '.tbi']
        if processed_uncompressed != chrom_uncompressed:
            files_to_cleanup.extend([chrom_uncompressed, processed_uncompressed])
        else:
            files_to_cleanup.append(chrom_uncompressed)
        for f in files_to_cleanup:
            if os.path.exists(f):
                os.remove(f)

        if result.returncode != 0:
            stderr_msg = result.stderr.strip()
            if 'not phased' in stderr_msg:
                return {'success': False, 'chrom': chrom, 'error': 'VCF not phased'}
            elif 'unable to find FASTA index' in stderr_msg:
                return {'success': False, 'chrom': chrom, 'error': 'Wrong reference genome'}
            else:
                return {'success': False, 'chrom': chrom, 'error': f'vcf2fasta failed: {stderr_msg}'}

        fasta_created = [f for f in os.listdir(temp_dir) if f.startswith(f"{input_vcf_basename}{chrom}.fasta")]
        return {'success': True, 'chrom': chrom, 'fasta_count': len(fasta_created)}

    except subprocess.CalledProcessError as e:
        return {'success': False, 'chrom': chrom, 'error': str(e)}
    except Exception as e:
        return {'success': False, 'chrom': chrom, 'error': str(e)}

def compress_and_index(file_path, ref_path, query_input, device_id):
    created_at = time.time()
    file_name = os.path.basename(file_path)
    output_vcf = file_name if file_name.endswith(".gz") else f"{file_name}.gz"
    error_message = ''

    task_id = str(uuid.uuid4())
    temp_dir = os.path.join(TEMP_BASE, f'vcf_process_{task_id[:8]}')
    os.makedirs(temp_dir, exist_ok=True)

    try:
        tabix_result = subprocess.run(
            ['tabix', '-p', 'vcf', file_name],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True
        )

        if "is not BGZF" in tabix_result.stderr:
            if file_name.endswith(".gz"):
                print("File is gzipped but not BGZF. Decompressing and recompressing...")
                subprocess.run(['gunzip', '-k', file_name], check=True)
                uncompressed_file = file_name[:-3]
                subprocess.run(["bgzip", "-c", "-@", str(NUM_WORKERS), uncompressed_file],
                             stdout=open(output_vcf, "wb"), check=True)
                os.remove(uncompressed_file)
            else:
                print("File is not compressed. Compressing with BGZF...")
                subprocess.run(["bgzip", "-c", "-@", str(NUM_WORKERS), file_name],
                             stdout=open(output_vcf, "wb"), check=True)
            subprocess.run(['tabix', '-p', 'vcf', output_vcf],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"File compressed and indexed as: {output_vcf}")
        else:
            print(f"File is already BGZF-compressed and indexed: {file_name}")

        print("Getting chromosome list...")
        chrom_result = subprocess.run(
            ['bcftools', 'index', '-s', output_vcf],
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True
        )

        if not chrom_result.stdout.strip():
            vcf2tsv_result = subprocess.run(['vcf2tsv', output_vcf],
                                            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
            df = pd.read_csv(StringIO(vcf2tsv_result.stdout), sep='\t',
                            dtype={'INFO': str, 'FORMAT': str}, low_memory=False)
            unique_chroms = [str(c) for c in df['#CHROM'].unique()]
        else:
            unique_chroms = [line.split('\t')[0] for line in chrom_result.stdout.strip().split('\n')]

        ref_fai_path = ref_path + '.fai'
        chrom_mapping = get_chromosome_mapping(unique_chroms, ref_fai_path)

        ref_chroms = set()
        if os.path.exists(ref_fai_path):
            with open(ref_fai_path, 'r') as f:
                for line in f:
                    parts = line.strip().split('\t')
                    if parts:
                        ref_chroms.add(parts[0])

        if chrom_mapping:
            renamed_vcf = os.path.join(temp_dir, f"renamed_{output_vcf}")
            renamed_result = rename_vcf_chromosomes(output_vcf, renamed_vcf, chrom_mapping, temp_dir)
            if renamed_result != output_vcf:
                output_vcf = renamed_result
                unique_chroms = [chrom_mapping[c] for c in unique_chroms if c in chrom_mapping]
                print(f"After mapping, processing {len(unique_chroms)} chromosomes that exist in reference")

        if ref_chroms:
            chrom_items = [c for c in unique_chroms if c in ref_chroms]
            if not chrom_items:
                first_two_components = os.sep.join(ref_path.split(os.sep)[:3])
                fai_files = [f for f in os.listdir(first_two_components) if f.endswith('.fai')]
                chrom_id = 'ch'
                for f in fai_files:
                    with open(os.path.join(first_two_components, f)) as fh:
                        lines = fh.readlines()
                        if len(lines) >= 2:
                            chrom_id = lines[1][:2]
                            break
                chrom_items = [c for c in unique_chroms if chrom_id in c or (c and c[0].isdigit())]
        else:
            chrom_items = unique_chroms

        if not chrom_items:
            chrom_items = unique_chroms

        def is_main_chromosome(name):
            n = name.lower()
            exclude_patterns = ['scaffold', 'super_scaffold', 'contig', 'nw_', 'nt_', 'un_', 'random', 'hap', 'alt', 'fix', 'patch']
            if any(p in n for p in exclude_patterns):
                return False
            if n.startswith('chr'):
                suffix = n[3:]
                return suffix.isdigit() or suffix in ('x', 'y', 'm', 'mt', 'w', 'z')
           
            if n.startswith('ch') and len(n) > 2:
                suffix = n[2:]
                return suffix.isdigit() or suffix in ('x', 'y', 'm', 'mt', 'w', 'z')
            
            if n.startswith('nc_'):
                return True

            if n.isdigit():
                return True
           
            if n in ('x', 'y', 'm', 'mt', 'w', 'z'):
                return True
            return False

        original_count = len(chrom_items)
        chrom_items = [c for c in chrom_items if is_main_chromosome(c)]
        if len(chrom_items) < original_count:
            print(f"Filtered out {original_count - len(chrom_items)} scaffolds/contigs, keeping {len(chrom_items)} main chromosomes")

        print(f"Found {len(chrom_items)} chromosomes to process")
        err_response = ''
        for item in chrom_items:
            if item not in unique_chroms:
                err_response = "Error: #CHROM name mismatch between VCF and reference genome."

        fasta_prefix = os.path.join(temp_dir, os.path.basename(output_vcf) + '.fasta')

        print(f'Processing {len(chrom_items)} chromosomes in parallel with {NUM_WORKERS} workers...')
        print('  (Each: extract -> normalize -> vcf2fasta)')

        process_args = [(output_vcf, chrom, ref_path, temp_dir, fasta_prefix) for chrom in chrom_items]

        results = []
        errors = []
        with ProcessPoolExecutor(max_workers=NUM_WORKERS) as executor:
            futures = {executor.submit(process_chromosome_pipeline, args): args[1] for args in process_args}
            completed = 0
            for future in as_completed(futures):
                result = future.result()
                results.append(result)
                completed += 1
                if completed % 5 == 0 or completed == len(chrom_items):
                    print(f'  Progress: {completed}/{len(chrom_items)} chromosomes')
                if not result.get('success'):
                    error_message = result.get('error', '')
                    errors.append(f"{result.get('chrom')}: {error_message}")

        if errors:
            print(f"  Errors in {len(errors)} chromosomes:")
            for err in errors[:5]:
                print(f"    - {err}")

       
        temp_contents = os.listdir(temp_dir)
        print(f"  Temp directory contains {len(temp_contents)} files")

        fasta_files = [f for f in os.listdir(temp_dir) if '.fasta' in f and not f.endswith('.fasta.fai')]
        print(f"  Found {len(fasta_files)} fasta files: {fasta_files[:5]}{'...' if len(fasta_files) > 5 else ''}")
        combined_content = f"{task_id}{file_name}_off_target_result.txt"
        allelic_off_target_files = []
        uploadedfile = ''

        is_gpu_mode = device_id.upper().startswith('G')
        cas_offinder_workers = 1 if is_gpu_mode else NUM_WORKERS

        if is_gpu_mode:
            print(f'Running cas-offinder on {len(fasta_files)} fasta files sequentially (GPU mode)...')
        else:
            print(f'Running cas-offinder on {len(fasta_files)} fasta files in parallel with {cas_offinder_workers} workers...')


        with open(query_input, 'r') as f:
            query_lines = f.readlines()
        while query_lines and (query_lines[0].startswith('./') or query_lines[0].startswith('/')):
            query_lines = query_lines[1:]

        cas_offinder_args = [
            (fasta_file, temp_dir, query_lines, device_id)
            for fasta_file in fasta_files
        ]

        with ProcessPoolExecutor(max_workers=cas_offinder_workers) as executor:
            futures = {executor.submit(run_cas_offinder, args): args[0] for args in cas_offinder_args}
            completed = 0
            for future in as_completed(futures):
                result = future.result()
                completed += 1
                if result.get('success'):
                    allelic_off_target_files.append(result.get('output_file'))
                else:
                    print(f"  Warning: cas-offinder failed for {result.get('fasta_file')}")
                if completed % 5 == 0 or completed == len(fasta_files):
                    print(f'  cas-offinder progress: {completed}/{len(fasta_files)}')

        try:
            with open(combined_content, 'w') as outfile:
                for off_file in allelic_off_target_files:
                    if os.path.exists(off_file):
                        with open(off_file, 'r') as infile:
                            outfile.write(infile.read())
        except Exception as e:
            uploadedfile = f"Error: {e}"
            combined_content = ''

        if not fasta_files and not error_message:
            sample_result = subprocess.run(
                ["bcftools", "query", "-l", output_vcf],
                capture_output=True, text=True
            )
            num_samples = len(sample_result.stdout.splitlines())
            if num_samples != 1:
                uploadedfile = f"Error: Multi-sample VCF ({num_samples} samples). Only single sample allowed."
            elif err_response:
                uploadedfile = err_response
            elif error_message:
                uploadedfile = error_message

    finally:
        print(f"Cleaning up temp directory: {temp_dir}")
        shutil.rmtree(temp_dir, ignore_errors=True)

    finished_at = time.time()
    execution_time = finished_at - created_at
    return {
        'success': True,
        'error': {uploadedfile},
        'off_target result': {combined_content},
        'Process completed in (Seconds)': {execution_time}
    }

def main():
    parser = argparse.ArgumentParser(description="Identify potential off-target sites based on VCF files.")
    parser.add_argument('-i', '--input', type=str, required=True,
                       help="Input file name (Phased and single sample VCF file)")
    parser.add_argument('-r', '--ref_path', type=str, required=True,
                       help="Full path to the target organism reference genome")
    parser.add_argument('-t', '--query_input', type=str, required=True,
                       help="Target sequence file (input.txt)")
    parser.add_argument('-d', '--device_id', type=str, required=True,
                       help="Device ID: C for CPU, G for GPU, G0 for GPU device 0")
    parser.add_argument('-w', '--workers', type=int, default=None,
                       help=f"Number of parallel workers (default: auto-detect, currently {AVAILABLE_CORES} cores)")
    args = parser.parse_args()

    global NUM_WORKERS
    NUM_WORKERS = args.workers if args.workers else AVAILABLE_CORES
    print(f"Using {NUM_WORKERS} CPU cores for parallel processing")

    output_vcf = compress_and_index(args.input, args.ref_path, args.query_input, args.device_id)
    print(f"status: {output_vcf}")
    print("Finished successfully.")

if __name__ == "__main__":
    main()
