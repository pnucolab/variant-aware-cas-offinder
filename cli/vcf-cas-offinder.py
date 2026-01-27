#!/home/abyot/miniconda3/envs/vcflibnew/bin/python
import argparse
import subprocess
import os
import sys
import re
import time
import uuid
import shlex
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from multiprocessing import cpu_count
import shutil
import glob
import pysam


def get_gpu_memory_info(device_id='0'):
    """
    Query GPU memory information using nvidia-smi.
    Returns (total_mb, free_mb, used_mb) or None if unavailable.
    """
    try:
        # Extract GPU index from device_id (e.g., 'G0' -> '0', 'G' -> '0')
        gpu_idx = '0'
        if device_id.startswith('G') and len(device_id) > 1:
            gpu_idx = device_id[1:]

        result = subprocess.run(
            ['nvidia-smi', '--query-gpu=memory.total,memory.free,memory.used',
             '--format=csv,noheader,nounits', '-i', gpu_idx],
            capture_output=True, text=True, timeout=10, check=False
        )

        if result.returncode == 0:
            parts = result.stdout.strip().split(',')
            if len(parts) >= 3:
                total_mb = int(parts[0].strip())
                free_mb = int(parts[1].strip())
                used_mb = int(parts[2].strip())
                return (total_mb, free_mb, used_mb)
    except (subprocess.TimeoutExpired, FileNotFoundError, ValueError) as e:
        print(f"Warning: Could not query GPU memory: {e}")

    return None


def estimate_optimal_gpu_workers(device_id='G0', estimated_memory_per_job_mb=2000, safety_margin=0.8, max_workers=16):
    """
    Dynamically estimate optimal number of parallel GPU workers based on available memory.
    If nvidia-smi is not available (e.g., inside container), use max_workers as default.
    """
    gpu_info = get_gpu_memory_info(device_id)

    if gpu_info is None:
        print(f"Could not query GPU memory (nvidia-smi unavailable), using maximum {max_workers} workers")
        return max_workers

    total_mb, free_mb, used_mb = gpu_info

    available_mb = free_mb * safety_margin

    optimal_workers = int(available_mb / estimated_memory_per_job_mb)

    optimal_workers = max(1, min(max_workers, optimal_workers))

    print(f"GPU Memory: {total_mb}MB total, {free_mb}MB free, {used_mb}MB used")
    print(f"Estimated {estimated_memory_per_job_mb}MB per job -> {optimal_workers} parallel workers")

    return optimal_workers


class FastaWriter:
    """
    High-performance FASTA writer using bytearray buffer.
    Optimized for large sequences with minimal memory allocations.
    """
    def __init__(self, filepath, header):
        self.filepath = filepath
        self.file = open(filepath, 'wb', buffering=1024*1024)
        self.buffer = bytearray()
        self.line_length = 80
        self.flush_threshold = 10 * 1024 * 1024  
        self.file.write(f">{header}\n".encode())

    def write(self, sequence):
        """Add sequence to buffer with periodic flushing"""
        if sequence:
            self.buffer.extend(sequence.encode() if isinstance(sequence, str) else sequence)

        if len(self.buffer) >= self.flush_threshold:
            self._flush_complete_lines()

    def _flush_complete_lines(self):
        """Write complete 80-char lines to file"""
        buf_len = len(self.buffer)
        complete_chars = (buf_len // self.line_length) * self.line_length

        if complete_chars > 0:
            output = bytearray()
            for i in range(0, complete_chars, self.line_length):
                output.extend(self.buffer[i:i+self.line_length])
                output.append(ord('\n'))
            self.file.write(output)
            self.buffer = self.buffer[complete_chars:]

    def close(self):
        """Flush remaining buffer and close file"""
        self._flush_complete_lines()
        if self.buffer:
            self.file.write(self.buffer)
            self.file.write(b'\n')
        self.file.close()


def vcf2fasta_python_single_chrom(args):
    """
    Process a single chromosome - convert VCF variants to FASTA.
    Optimized version with batched reference reads and efficient memory usage.
    """
    vcf_file, chrom, ref_file, output_dir, sample_name, chrom_mapping = args

    try:
        ref_fasta = pysam.FastaFile(ref_file)

        # Use chromosome mapping to find the correct reference chromosome name
        ref_chrom = chrom_mapping.get(chrom, chrom) if chrom_mapping else chrom

        if ref_chrom not in ref_fasta.references:
            ref_fasta.close()
            return (chrom, {}, f"Chromosome {chrom} not in reference (tried mapping to {ref_chrom})")

        chrom_length = ref_fasta.get_reference_length(ref_chrom)
        vcf = pysam.VariantFile(vcf_file)
        samples = list(vcf.header.samples)
        if not samples:
            vcf.close()
            ref_fasta.close()
            return (chrom, {}, "No samples in VCF")

        target_sample = sample_name if sample_name in samples else samples[0]

        # Detect ploidy from first variant's GT field
        ploidy = 2  # default to diploid
        for record in vcf.fetch(chrom):
            sample_data = record.samples[target_sample]
            gt = sample_data.get('GT', None)
            if gt is not None:
                ploidy = len(gt)
                break
        vcf.close()
        vcf = pysam.VariantFile(vcf_file)  

        output_files = {}
        fasta_writers = {}
        for hap in range(ploidy):
            output_file = os.path.join(output_dir, f"chrom_{chrom}_hap{hap}.fa")
            output_files[hap] = output_file
            fasta_writers[hap] = FastaWriter(output_file, f"{target_sample}_{chrom}:{hap}")

        last_pos = {hap: 1 for hap in range(ploidy)}
        CHUNK_SIZE = 1000000  
        ref_cache = {}
        ref_cache_start = {}

        def get_ref_cached(start, end):
            """Get reference sequence with caching"""
            cache_key = start // CHUNK_SIZE
            if cache_key not in ref_cache:
                chunk_start = cache_key * CHUNK_SIZE
                chunk_end = min((cache_key + 1) * CHUNK_SIZE, chrom_length)
                ref_cache[cache_key] = ref_fasta.fetch(ref_chrom, chunk_start, chunk_end)
                ref_cache_start[cache_key] = chunk_start

            if end > (cache_key + 1) * CHUNK_SIZE:
                return ref_fasta.fetch(ref_chrom, start, end)

           
            cache_start = ref_cache_start[cache_key]
            local_start = start - cache_start
            local_end = end - cache_start
            return ref_cache[cache_key][local_start:local_end]

      
        variant_count = 0
        for record in vcf.fetch(chrom):
            variant_count += 1

            sample_data = record.samples[target_sample]
            gt = sample_data.get('GT', None)

            if gt is None or not sample_data.phased:
                continue

         
            alleles = [record.ref] + list(record.alts) if record.alts else [record.ref]
            pos = record.pos  

            for hap_idx in range(len(gt)):
                allele_idx = gt[hap_idx]
                if allele_idx is None or allele_idx >= len(alleles):
                    continue

                allele = alleles[allele_idx]

                if pos > last_pos[hap_idx]:
                    ref_seq = get_ref_cached(last_pos[hap_idx] - 1, pos - 1)
                    fasta_writers[hap_idx].write(ref_seq)

              
                fasta_writers[hap_idx].write(allele)

                
                last_pos[hap_idx] = pos + len(record.ref)
            if variant_count % 100000 == 0:
                current_chunk = min(last_pos.values()) // CHUNK_SIZE
                old_keys = [k for k in ref_cache if k < current_chunk - 1]
                for k in old_keys:
                    del ref_cache[k]
                    del ref_cache_start[k]

        for hap in range(ploidy):
            if last_pos[hap] <= chrom_length:
                remaining_ref = ref_fasta.fetch(ref_chrom, last_pos[hap] - 1, chrom_length)
                fasta_writers[hap].write(remaining_ref)
            fasta_writers[hap].close()

        vcf.close()
        ref_fasta.close()

        return (chrom, output_files, None)

    except Exception as e:  # pylint: disable=broad-exception-caught
        return (chrom, {}, str(e))


def vcf2fasta_python_parallel(vcf_file, ref_file, chromosomes, output_prefix, work_dir, num_workers=None):
    """
    Python implementation of vcf2fasta with parallel chromosome processing.
    """
    if num_workers is None:
        num_workers = cpu_count()

    step_start = time.time()
    try:
        vcf = pysam.VariantFile(vcf_file)
        samples = list(vcf.header.samples)
        vcf.close()
        if not samples:
            return [], "No samples in VCF file"
        sample_name = samples[0]
    except Exception as e:  # pylint: disable=broad-exception-caught
        return [], f"Error reading VCF: {e}"

    try:
        ref_fasta = pysam.FastaFile(ref_file)
        ref_chroms = list(ref_fasta.references)
        ref_fasta.close()
        
        ref_descriptions = get_fasta_descriptions(ref_file)
        chrom_mapping = build_chrom_mapping(chromosomes, ref_chroms, ref_descriptions)
        mapped = len([c for c in chromosomes if c in chrom_mapping])
        unmapped = [c for c in chromosomes if c not in chrom_mapping]
        print(f"Chromosome mapping: {mapped}/{len(chromosomes)} mapped")
        if chrom_mapping:
            for vcf_c, ref_c in list(chrom_mapping.items())[:3]:
                if vcf_c != ref_c:
                    print(f"  Example: {vcf_c} -> {ref_c}")
        if unmapped:
            print(f"  Unmapped: {unmapped[:3]}")
            if ref_descriptions:
                print(f"  Ref descriptions sample: {list(ref_descriptions.items())[:2]}")
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"Warning: Could not build chromosome mapping: {e}")
        chrom_mapping = {}

    print(f"Processing sample: {sample_name}")
    print(f"Processing {len(chromosomes)} chromosomes with {min(num_workers, len(chromosomes))} workers...")
    process_args = [
        (vcf_file, chrom, ref_file, work_dir, sample_name, chrom_mapping)
        for chrom in chromosomes
    ]

    chrom_files = {}  # Dynamic: will be populated based on detected ploidy
    errors = []
    completed = 0

    effective_workers = min(num_workers, len(chromosomes))

    with ProcessPoolExecutor(max_workers=effective_workers) as executor:
        futures = {executor.submit(vcf2fasta_python_single_chrom, args): args[1] for args in process_args}

        for future in as_completed(futures):
            chrom = futures[future]
            completed += 1

            try:
                result_chrom, hap_files, error = future.result()
                if error:
                    errors.append(f"{result_chrom}: {error}")
                else:
                    for hap, filepath in hap_files.items():
                        if hap not in chrom_files:
                            chrom_files[hap] = {}
                        chrom_files[hap][result_chrom] = filepath

                if completed % 5 == 0 or completed == len(chromosomes):
                    print(f"  Progress: {completed}/{len(chromosomes)} chromosomes")

            except Exception as e:  # pylint: disable=broad-exception-caught
                errors.append(f"{chrom}: {str(e)}")

    print(f"[Timing] Parallel chromosome processing: {time.time() - step_start:.2f}s")

    merge_start = time.time()
    final_fasta_files = []

    def chrom_sort_key(c):
        c_stripped = c.replace('chr', '') if c.startswith('chr') else c
        if c_stripped.isdigit():
            return (0, int(c_stripped))
        elif c_stripped == 'X':
            return (1, 23)
        elif c_stripped == 'Y':
            return (1, 24)
        elif c_stripped in ['MT', 'M']:
            return (1, 25)
        return (2, c)

    sorted_chroms = sorted(chromosomes, key=chrom_sort_key)

    for chrom in sorted_chroms:
        for hap in sorted(chrom_files.keys()):
            if chrom in chrom_files[hap]:
                chrom_file = chrom_files[hap][chrom]
                if os.path.exists(chrom_file):
                    final_file = f"{output_prefix}{sample_name}_{chrom}:{hap}.fa"
                    shutil.move(chrom_file, final_file)
                    final_fasta_files.append(final_file)

    print(f"[Timing] Move chromosome files: {time.time() - merge_start:.2f}s")
    print(f"[Timing] Total Python vcf2fasta: {time.time() - step_start:.2f}s")
    print(f"Generated {len(final_fasta_files)} FASTA files")

    error_message = None
    if errors:
        for err in errors:
            if 'not phased' in err.lower():
                error_message = 'Error: your vcf file is not phased. Only Phased and single sample vcf is allowed.'
                break
        if not error_message and len(errors) == len(chromosomes):
            error_message = f"All chromosomes failed: {errors[0]}"
        elif not error_message and errors:
            error_message = f"Warnings in {len(errors)} chromosomes"
            print(f"Warnings: {errors[:3]}...")

    return final_fasta_files, error_message


def vcf2fasta_python_chunked(result_file, ref_path, chrom_item, task_id, num_workers=None, work_dir=None):
    """
    Wrapper function to match the interface of vcf2fasta_parallel_chunked.
    """
    if num_workers is None:
        num_workers = cpu_count() 
    if os.path.exists('/dev/shm') and os.access('/dev/shm', os.W_OK):
        temp_dir = f"/dev/shm/vcf2fasta_py_{task_id}"
        print(f"Using RAM disk for temp processing: {temp_dir}")
    else:
        temp_dir = f"/tmp/vcf2fasta_py_{task_id}"
        print(f"Using temp directory: {temp_dir}")

    os.makedirs(temp_dir, exist_ok=True)
    if work_dir:
        output_prefix = os.path.join(work_dir, f"{os.path.basename(result_file)}.fasta")
    else:
        output_prefix = f"{os.path.basename(result_file)}.fasta"

    try:
        fasta_files, error = vcf2fasta_python_parallel(
            result_file,
            ref_path,
            chrom_item,
            output_prefix,
            temp_dir,
            num_workers
        )
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

    return fasta_files, error


def get_vcf_variant_count(vcf_file):
    """Get total number of variants in VCF using index"""
    result = subprocess.run(
        ['bcftools', 'index', '-n', vcf_file],
        capture_output=True, text=True, check=False
    )
    if result.returncode == 0 and result.stdout.strip():
        return int(result.stdout.strip())
    result = subprocess.run(
        f"bcftools view -H {shlex.quote(vcf_file)} | wc -l",
        shell=True, capture_output=True, text=True, check=False
    )
    return int(result.stdout.strip())


def get_chrom_variant_counts(vcf_file):
    """Get variant counts per chromosome"""
    result = subprocess.run(
        ['bcftools', 'index', '-s', vcf_file],
        capture_output=True, text=True, check=False
    )

    chrom_counts = {}
    for line in result.stdout.strip().split('\n'):
        if line:
            parts = line.split('\t')
            if len(parts) >= 3:
                chrom_counts[parts[0]] = int(parts[2])
    return chrom_counts


def is_standard_chromosome(chrom):
    """Check if chromosome is standard (1-22, X, Y, MT)"""
    chrom_stripped = chrom.replace('chr', '') if chrom.startswith('chr') else chrom
    if chrom_stripped.isdigit():
        return True
    if chrom_stripped in ['X', 'Y', 'MT', 'M']:
        return True
    return False


def extract_chrom_number(chrom_name):
    """Extract chromosome number/identifier from various naming formats."""
    if chrom_name.startswith('chr'):
        return chrom_name[3:]
    match = re.search(r'chromosome[_\s-]*(\w+)', chrom_name, re.IGNORECASE)
    if match:
        return match.group(1)
    match = re.search(r'^(\d+)$', chrom_name)
    if match:
        return match.group(1)
    return chrom_name


def get_fasta_descriptions(ref_file):
    """
    Read FASTA file headers to extract sequence descriptions.
    Returns dict: {seq_id: full_description}
    """
    descriptions = {}
    try:
        with open(ref_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('>'):
                    header = line[1:].strip()
                    parts = header.split(None, 1)  
                    seq_id = parts[0]
                    description = parts[1] if len(parts) > 1 else ''
                    descriptions[seq_id] = description
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"Warning: Could not read FASTA headers: {e}")
    return descriptions


def build_chrom_mapping(vcf_chroms, ref_chroms, ref_descriptions=None):
    """
    Build a mapping from VCF chromosome names to reference chromosome names.
    Handles common naming convention differences (chr1 vs 1 vs NC_...).
    Returns dict: {vcf_chrom: ref_chrom}
    """
    mapping = {}
    if ref_descriptions is None:
        ref_descriptions = {}

    for vcf_chrom in vcf_chroms:
        if vcf_chrom in ref_chroms:
            mapping[vcf_chrom] = vcf_chrom
            continue

        vcf_id = extract_chrom_number(vcf_chrom)

        for ref_chrom in ref_chroms:
            if ref_chrom in mapping.values():
                continue  

            ref_id = extract_chrom_number(ref_chrom)
            if vcf_id.lower() == ref_id.lower():
                mapping[vcf_chrom] = ref_chrom
                break

            if f'chromosome {vcf_id}' in ref_chrom.lower() or f'chromosome_{vcf_id}' in ref_chrom.lower():
                mapping[vcf_chrom] = ref_chrom
                break

            ref_desc = ref_descriptions.get(ref_chrom, '')
            if ref_desc:
                match = re.search(r'chromosome[_\s-]+(\S+)', ref_desc, re.IGNORECASE)
                if match:
                    desc_chrom_id = match.group(1).rstrip(',')
                    if vcf_id.lower() == desc_chrom_id.lower():
                        mapping[vcf_chrom] = ref_chrom
                        break
                    if vcf_chrom.startswith('chr') and vcf_chrom[3:].lower() == desc_chrom_id.lower():
                        mapping[vcf_chrom] = ref_chrom
                        break
                    trailing_num = re.search(r'[-_](\d+)$', desc_chrom_id)
                    if trailing_num:
                        if vcf_id == trailing_num.group(1):
                            mapping[vcf_chrom] = ref_chrom
                            break

            if vcf_chrom.startswith('chr') and ref_chrom == vcf_chrom[3:]:
                mapping[vcf_chrom] = ref_chrom
                break
            if ref_chrom.startswith('chr') and vcf_chrom == ref_chrom[3:]:
                mapping[vcf_chrom] = ref_chrom
                break

    return mapping


def get_chromosomes_from_vcf(vcf_file):
    """Get list of chromosomes from VCF file"""
    result = subprocess.run(
        ['bcftools', 'query', '-f', '%CHROM\n', vcf_file],
        capture_output=True, text=True, check=False
    )
    return sorted(set(result.stdout.strip().split('\n')))


def get_conda_bin_path():
    """Get the conda bin directory from the current Python interpreter"""
    python_path = sys.executable
    bin_dir = os.path.dirname(python_path)
    return bin_dir


def normalize_vcf_chunk(args):
    """
    Normalize a single chromosome chunk.
    Runs: vcfallelicprimitives | bcftools norm | vcfcreatemulti | bgzip
    Uses shell pipeline with pipefail for proper error detection.
    """
    input_vcf, chrom, work_dir, conda_bin = args

    chunk_input = os.path.join(work_dir, f"chunk_{chrom}_input.vcf.gz")
    chunk_output = os.path.join(work_dir, f"chunk_{chrom}_normalized.vcf.gz")

    vcfallelicprimitives = os.path.join(conda_bin, 'vcfallelicprimitives')
    vcfcreatemulti = os.path.join(conda_bin, 'vcfcreatemulti')
    bcftools = os.path.join(conda_bin, 'bcftools')
    bgzip = os.path.join(conda_bin, 'bgzip')

    if not os.path.exists(bcftools):
        bcftools = shutil.which('bcftools') or 'bcftools'
    if not os.path.exists(bgzip):
        bgzip = shutil.which('bgzip') or 'bgzip'

    try:
        extract_result = subprocess.run([
            bcftools, 'view', '-r', chrom, '-Oz', '-o', chunk_input, input_vcf
        ], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True, check=False)

        if extract_result.returncode != 0:
            return (chrom, None, f"bcftools view failed: {extract_result.stderr}")

        if not os.path.exists(chunk_input):
            return (chrom, None, "chunk input not created")
        pipeline_cmd = (
            "set -o pipefail; "
            f"{shlex.quote(vcfallelicprimitives)} {shlex.quote(chunk_input)} 2>/dev/null | "
            f"{shlex.quote(bcftools)} norm -m- 2>/dev/null | "
            f"{shlex.quote(vcfcreatemulti)} 2>/dev/null | "
            f"{shlex.quote(bgzip)} -c > {shlex.quote(chunk_output)}"
        )

        result = subprocess.run(
            pipeline_cmd,
            shell=True,
            executable='/bin/bash',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )

        if result.returncode != 0 or not os.path.exists(chunk_output) or os.path.getsize(chunk_output) == 0:
            fallback_result = subprocess.run([
                bcftools, 'norm', '-m-', '-Oz', '-o', chunk_output, chunk_input
            ], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True, check=False)

            if fallback_result.returncode != 0:
                try:
                    os.remove(chunk_input)
                except OSError:
                    pass
                return (chrom, None, f"normalization failed: {result.stderr} | fallback: {fallback_result.stderr}")

        try:
            os.remove(chunk_input)
        except OSError:
            pass
        if not os.path.exists(chunk_output):
            return (chrom, None, "chunk output not created")

        if os.path.getsize(chunk_output) == 0:
            return (chrom, None, "chunk output is empty")

        return (chrom, chunk_output, None)
    except Exception as e: # pylint: disable=broad-exception-caught
        return (chrom, None, str(e))


def normalize_vcf_parallel(input_vcf, output_vcf, num_workers=None):
    """
    Parallel VCF normalization by chromosome.
    1. Split VCF by chromosome
    2. Run normalization pipeline on each chunk in parallel
    3. Merge normalized chunks
    """
    if num_workers is None:
        num_workers = cpu_count()
    if os.path.exists('/dev/shm') and os.access('/dev/shm', os.W_OK):
        work_dir = f"/dev/shm/vcf_norm_{uuid.uuid4().hex[:8]}"
    else:
        work_dir = f"/tmp/vcf_norm_{uuid.uuid4().hex[:8]}"

    os.makedirs(work_dir, exist_ok=True)

    step_start = time.time()
    chromosomes = get_chromosomes_from_vcf(input_vcf)
    chromosomes = [c for c in chromosomes if is_standard_chromosome(c)]

    if not chromosomes:
        print("No standard chromosomes found, using sequential normalization...")
        shutil.rmtree(work_dir, ignore_errors=True)
        return False

    print(f"Normalizing {len(chromosomes)} chromosomes with {min(num_workers, len(chromosomes))} parallel workers...")

    conda_bin = get_conda_bin_path()

    process_args = [(input_vcf, chrom, work_dir, conda_bin) for chrom in chromosomes]

    norm_start = time.time()
    chunk_files = []
    errors = []

    with ProcessPoolExecutor(max_workers=min(num_workers, len(chromosomes))) as executor:
        results = list(executor.map(normalize_vcf_chunk, process_args))
        for chrom, chunk_file, error in results:
            if error:
                errors.append(f"{chrom}: {error}")
            elif chunk_file:
                if os.path.exists(chunk_file):
                    chunk_files.append(chunk_file)
                else:
                    errors.append(f"{chrom}: output file missing after processing")

    print(f"[Timing] Parallel normalization: {time.time() - norm_start:.2f}s")
    print(f"DEBUG: Successfully created {len(chunk_files)} chunks, {len(errors)} errors")

    if errors:
        print(f"Warning: Errors in normalization: {errors[:5]}")  

    if not chunk_files:
        shutil.rmtree(work_dir, ignore_errors=True)
        return False

    merge_start = time.time()
    file_list = os.path.join(work_dir, "chunks.txt")
    def chrom_sort_key(filepath):
        basename = os.path.basename(filepath)
        match = re.search(r'chunk_(.+?)_normalized', basename)
        if match:
            chrom = match.group(1)
            chrom_num = chrom.replace('chr', '')
            if chrom_num.isdigit():
                return (0, int(chrom_num))
            elif chrom_num == 'X':
                return (1, 23)
            elif chrom_num == 'Y':
                return (1, 24)
            elif chrom_num in ['MT', 'M']:
                return (1, 25)
        return (2, filepath)

    sorted_chunks = sorted(chunk_files, key=chrom_sort_key)

    print(f"DEBUG: Found {len(sorted_chunks)} chunk files to merge")

    with open(file_list, 'w', encoding='utf-8') as f:
        for cf in sorted_chunks:
            if os.path.exists(cf):
                idx_result = subprocess.run(['tabix', '-f', '-p', 'vcf', cf],
                              stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True, check=False)
                if idx_result.returncode != 0:
                    print(f"Warning: tabix failed for {cf}: {idx_result.stderr}")
                f.write(cf + '\n')
            else:
                print(f"Warning: Chunk file not found: {cf}")

    concat_temp = os.path.join(work_dir, "concat_temp.vcf.gz")
    concat_result = subprocess.run([
        'bcftools', 'concat',
        '-f', file_list,
        '-Oz', '--threads', str(num_workers),
        '-o', concat_temp
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)

    if concat_result.returncode != 0:
        print(f"ERROR: bcftools concat failed: {concat_result.stderr}")
        shutil.rmtree(work_dir, ignore_errors=True)
        return False

    # CRITICAL: Sort the VCF to fix overlapping/out-of-order variants
    # This is required for vcf2fasta to work correctly
    print("Sorting VCF to fix overlapping variants...")
    sort_result = subprocess.run([
        'bcftools', 'sort',
        '-Oz', '-o', output_vcf,
        concat_temp
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)

    if sort_result.returncode != 0:
        print(f"Warning: bcftools sort failed: {sort_result.stderr}, using unsorted")
        shutil.move(concat_temp, output_vcf)
    else:
        os.remove(concat_temp)

    if not os.path.exists(output_vcf):
        print(f"ERROR: Output file not created: {output_vcf}")
        shutil.rmtree(work_dir, ignore_errors=True)
        return False

    idx_result = subprocess.run(['tabix', '-f', '-p', 'vcf', output_vcf],
                  stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True, check=False)
    if idx_result.returncode != 0:
        print(f"Warning: tabix failed for output: {idx_result.stderr}")

    print(f"[Timing] Merge chunks: {time.time() - merge_start:.2f}s")

    shutil.rmtree(work_dir, ignore_errors=True)

    print(f"[Timing] Total parallel normalization: {time.time() - step_start:.2f}s")

    return True


def create_single_chunk(args):
    """Create a single VCF chunk - runs in parallel"""
    vcf_file, chrom, work_dir, chunk_idx, conda_bin = args

    bcftools = os.path.join(conda_bin, 'bcftools')
    if not os.path.exists(bcftools):
        bcftools = shutil.which('bcftools') or 'bcftools'

    chunk_file = os.path.join(work_dir, f"chunk_{chunk_idx}_{chrom}.vcf.gz")

    try:
        subprocess.run([
            bcftools, 'view',
            '-r', chrom,
            '-Oz', '-o', chunk_file,
            vcf_file
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        subprocess.run(['tabix', '-f', '-p', 'vcf', chunk_file],
                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)

        return (chunk_idx, chunk_file, [chrom], None)
    except Exception as e:  # pylint: disable=broad-exception-caught
        return (chunk_idx, None, [chrom], str(e))


def split_vcf_into_chunks_parallel(vcf_file, work_dir, chrom_item, num_workers=None):
    """
    Split VCF into chunks by chromosome - PARALLEL version.
    Returns list of (chunk_file, [chromosomes]) tuples.
    """
    if num_workers is None:
        num_workers = cpu_count()

    conda_bin = get_conda_bin_path()

    split_args = [
        (vcf_file, chrom, work_dir, i, conda_bin)
        for i, chrom in enumerate(chrom_item)
    ]

    chunk_files = []
    errors = []
    with ProcessPoolExecutor(max_workers=min(num_workers, len(chrom_item))) as executor:
        results = list(executor.map(create_single_chunk, split_args))
        for _, chunk_file, chroms, error in results:
            if error:
                errors.append(f"{chroms[0]}: {error}")
            elif chunk_file and os.path.exists(chunk_file):
                chunk_files.append((chunk_file, chroms))

    if errors:
        print(f"Warning: {len(errors)} errors during splitting")

    return chunk_files


def process_vcf2fasta_chunk(args):
    """
    Process a single VCF chunk with vcf2fasta.
    This function runs in a separate process.
    """
    chunk_file, chroms, ref_path, vcf2fasta_path, output_prefix, _, conda_bin = args

    samtools = os.path.join(conda_bin, 'samtools')
    if not os.path.exists(samtools):
        samtools = shutil.which('samtools') or 'samtools'

    try:
        chunk_ref = f"{chunk_file}.ref.fa"
        with open(chunk_ref, 'w', encoding='utf-8') as f:
            subprocess.run(
                [samtools, 'faidx', ref_path] + chroms,
                stdout=f, stderr=subprocess.DEVNULL, check=False
            )
        subprocess.run([samtools, 'faidx', chunk_ref],
                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)

        chunk_output_prefix = f"{output_prefix}.{os.path.basename(chunk_file)}"
        result = subprocess.run(
            [vcf2fasta_path, '-f', chunk_ref, '-p', chunk_output_prefix, chunk_file],
            stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True, check=False
        )

        error_msg = None
        if result.returncode != 0:
            stderr = result.stderr.strip()
            if 'not phased' in stderr:
                error_msg = 'VCF not phased'
            elif 'unable to find FASTA index' in stderr:
                error_msg = 'FASTA index error'
            else:
                error_msg = stderr[:100] if stderr else 'Unknown error'

        for f in [chunk_file, f"{chunk_file}.tbi", chunk_ref, f"{chunk_ref}.fai"]:
            try:
                os.remove(f)
            except OSError:
                pass

        return (chroms, error_msg)

    except Exception as e:  # pylint: disable=broad-exception-caught
        return (chroms, str(e))


def vcf2fasta_parallel_chunked(result_file, ref_path, chrom_item, vcf2fasta_path, task_id, num_workers=None, work_dir=None):
    """
    Optimized vcf2fasta using chunk-based parallel processing.

    1. Splits VCF into N chunks (by chromosome) - PARALLEL
    2. Runs vcf2fasta on each chunk in parallel
    3. Collects all output FASTA files

    Returns: (list of fasta files, error message or None)
    """
    if num_workers is None:
        num_workers = cpu_count()
    if os.path.exists('/dev/shm') and os.access('/dev/shm', os.W_OK):
        temp_dir = f"/dev/shm/vcf2fasta_{task_id}"
        print(f"Using RAM disk: {temp_dir}")
    else:
        temp_dir = f"/tmp/vcf2fasta_{task_id}"
        print(f"Using temp directory: {temp_dir}")

    os.makedirs(temp_dir, exist_ok=True)

    step_start = time.time()
    output_dir = work_dir if work_dir else temp_dir
    output_prefix = os.path.join(output_dir, f"{os.path.basename(result_file)}.fasta")
    conda_bin = get_conda_bin_path()
    print(f"Splitting VCF into {len(chrom_item)} chromosome chunks (parallel)...")
    split_start = time.time()
    chunk_files = split_vcf_into_chunks_parallel(result_file, temp_dir, chrom_item, num_workers)

    if not chunk_files:
        shutil.rmtree(temp_dir, ignore_errors=True)
        return [], "No valid chromosomes found in VCF"

    print(f"[Timing] Parallel VCF splitting into {len(chunk_files)} chunks: {time.time() - split_start:.2f}s")

    process_args = [
        (chunk_file, chroms, ref_path, vcf2fasta_path, output_prefix, temp_dir, conda_bin)
        for chunk_file, chroms in chunk_files
    ]
    effective_workers = min(num_workers, len(chunk_files))

    vcf2fasta_start = time.time()
    print(f"Running vcf2fasta on {len(chunk_files)} chunks with {effective_workers} parallel workers...")

    errors = []
    completed = 0
    with ProcessPoolExecutor(max_workers=effective_workers) as executor:
        futures = {executor.submit(process_vcf2fasta_chunk, args): args for args in process_args}
        for future in as_completed(futures):
            chroms, error = future.result()
            completed += 1
            if error:
                errors.append(f"{','.join(chroms)}: {error}")
            if completed % 5 == 0 or completed == len(chunk_files):
                print(f"  Progress: {completed}/{len(chunk_files)} chunks completed")

    print(f"[Timing] Parallel vcf2fasta execution: {time.time() - vcf2fasta_start:.2f}s")

    collect_start = time.time()
    fasta_pattern = os.path.join(output_dir, "*.fa")
    generated_fastas = glob.glob(fasta_pattern)

    final_fastas = generated_fastas

    print(f"[Timing] File collection: {time.time() - collect_start:.2f}s")

    shutil.rmtree(temp_dir, ignore_errors=True)

    print(f"[Timing] Total vcf2fasta (chunked parallel): {time.time() - step_start:.2f}s")
    print(f"Generated {len(final_fastas)} FASTA files")

    error_message = None
    if errors:
        for err in errors:
            if 'not phased' in err.lower():
                error_message = 'Error: your vcf file is not phased. Only Phased and single sample vcf is allowed.'
                break
            elif 'fasta index' in err.lower():
                error_message = 'Error: Wrong target organism selection.'
                break
        if not error_message and errors:
            error_message = f"Errors in some chunks: {'; '.join(errors)}"

    return final_fastas, error_message


def compress_and_index(file_path, ref_path, query_input, device_id):
    """Process VCF file: normalize, convert to FASTA, and run cas-offinder."""
    created_at = time.time()
    task_id = str(uuid.uuid4())
    file_name_1 = os.path.basename(file_path)

    work_dir = f"work_{task_id}"
    os.makedirs(work_dir, exist_ok=True)
    print(f"Created work directory: {work_dir}")

    file_name = os.path.join(work_dir, f"{task_id}{file_name_1}")

    step_start = time.time()
    try:
        os.symlink(os.path.abspath(file_name_1), file_name)
    except OSError:
        shutil.copy2(file_name_1, file_name)
    print(f"[Timing] File copy/symlink: {time.time() - step_start:.2f}s")

    output_vcf = file_name if file_name.endswith(".gz") else f"{file_name}.gz"
    error_message = ''
    tabix_result = subprocess.run(
        ['tabix', '-p', 'vcf', file_name],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
        check=False
    )
    if "is not BGZF" in tabix_result.stderr:
        if file_name.endswith(".gz"):
            print("File is gzipped but not BGZF. Decompressing and recompressing...")
            subprocess.run(['gunzip', file_name], check=False)
            uncompressed_file = file_name[:-3]
            subprocess.run(["bgzip", "-c", uncompressed_file], stdout=open(output_vcf, "wb"), check=False)
            subprocess.run(tabix_result, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        else:
            print("File is not compressed. Compressing with BGZF...")
            subprocess.run(["bgzip", "-c", file_name], stdout=open(output_vcf, "wb"), check=False)
            subprocess.run(['tabix', '-p', 'vcf', output_vcf], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
            print(f"File compressed and indexed as: {output_vcf}")
    else:
        print(f"File is already BGZF-compressed and indexed: {file_name}")

    step_start = time.time()
    result_file = os.path.join(work_dir, "output_" + os.path.basename(output_vcf))

    print(f'\n{"="*50}')
    print('Running PARALLEL VCF normalization by chromosome...')
    print(f'{"="*50}')
    chrom_result = subprocess.run(
        ['bcftools', 'query', '-f', '%CHROM\n', output_vcf],
        capture_output=True, text=True, check=False
    )
    vcf_chroms = sorted(set(chrom_result.stdout.strip().split('\n')))
    standard_chroms = [c for c in vcf_chroms if is_standard_chromosome(c)]

    print(f"Processing {len(standard_chroms)} chromosomes in parallel...")

    if os.path.exists('/dev/shm') and os.access('/dev/shm', os.W_OK):
        norm_work_dir = f"/dev/shm/vcf_norm_{task_id}"
    else:
        norm_work_dir = f"/tmp/vcf_norm_{task_id}"
    os.makedirs(norm_work_dir, exist_ok=True)

    def normalize_single_chrom(chrom):
        """Run full normalization pipeline on a single chromosome"""
        chunk_output = os.path.join(norm_work_dir, f"norm_{chrom}.vcf.gz")
        try:
            cmd = (
                f"bcftools view -r {shlex.quote(chrom)} {shlex.quote(output_vcf)} | "
                "vcfallelicprimitives | "
                "bcftools norm -m- | "
                "vcfcreatemulti | "
                f"bgzip -c > {shlex.quote(chunk_output)}"
            )
            result = subprocess.run(cmd, shell=True, executable='/bin/bash',
                                   stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, check=False)
            if result.returncode == 0 and os.path.exists(chunk_output) and os.path.getsize(chunk_output) > 0:
                return (chrom, chunk_output, None)
            return (chrom, None, result.stderr.decode() if result.stderr else "Unknown error")
        except Exception as e:  # pylint: disable=broad-exception-caught
            return (chrom, None, str(e))

    chunk_files = []
    with ThreadPoolExecutor(max_workers=cpu_count()) as executor:
        results = list(executor.map(normalize_single_chrom, standard_chroms))
        for chrom, chunk_file, error in results:
            if chunk_file:
                chunk_files.append((chrom, chunk_file))
            elif error:
                print(f"Warning: {chrom} normalization failed: {error[:100]}")

    def chrom_sort_key(item):
        chrom = item[0]
        c = chrom.replace('chr', '') if chrom.startswith('chr') else chrom
        if c.isdigit():
            return (0, int(c))
        elif c == 'X':
            return (1, 23)
        elif c == 'Y':
            return (1, 24)
        return (2, chrom)

    chunk_files.sort(key=chrom_sort_key)

    if chunk_files:
        for _, chunk_file in chunk_files:
            subprocess.run(['tabix', '-f', '-p', 'vcf', chunk_file],
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)

        file_list = os.path.join(norm_work_dir, "chunks.txt")
        with open(file_list, 'w', encoding='utf-8') as f:
            for _, chunk_file in chunk_files:
                f.write(chunk_file + '\n')

        subprocess.run([
            'bcftools', 'concat', '-f', file_list, '-Oz', '-o', result_file
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)

        subprocess.run(['bcftools', 'index', result_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        subprocess.run(['tabix', '-p', 'vcf', result_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)

    # Cleanup
    shutil.rmtree(norm_work_dir, ignore_errors=True)

    print(f"[Timing] VCF normalization pipeline: {time.time() - step_start:.2f}s")

    step_start = time.time()
    header_cmd = ['bcftools', 'query', '-f', '%CHROM\n', result_file]
    result = subprocess.run(header_cmd, stdout=subprocess.PIPE, text=True, check=False)
    unique_s_str = sorted(set(result.stdout.strip().split('\n')))

    chrom_item = [item for item in unique_s_str if is_standard_chromosome(item)]
    print(f'Found standard chromosomes: {chrom_item}')

    err_response = ''
    for item in chrom_item:
        if item not in unique_s_str:
            err_response = "Error: #CHROM name mismatch between your vcf file and target organism reference genome."

    vcf2fasta_path = shutil.which('vcf2fasta')
    if not vcf2fasta_path:
        conda_bin = os.path.dirname(os.path.realpath('/home/abyot/miniconda3/envs/vcflibnew/bin/python'))
        vcf2fasta_path = os.path.join(conda_bin, 'vcf2fasta')

    if not os.path.exists(vcf2fasta_path):
        return {'success': False, 'error': 'vcf2fasta not found', 'off_target result': '', 'Process completed in (Seconds)': 0}

    print(f'\n{"="*50}')
    print('Running OPTIMIZED Python vcf2fasta (parallel)...')
    print(f'{"="*50}')

    fasta_files, vcf2fasta_error = vcf2fasta_python_chunked(
        result_file, ref_path, chrom_item, task_id, work_dir=work_dir
    )
    def fasta_sort_key(filename):
        match = re.search(r'chr(\d+):(\d+)', filename)
        if match:
            return (int(match.group(1)), int(match.group(2)))
        return (999, 0)
    fasta_files = sorted(fasta_files, key=fasta_sort_key)

    if vcf2fasta_error:
        error_message = vcf2fasta_error
    combined_content = f"{task_id}{file_name_1}_off_target_result.txt"
    uploadedfile = ''

    with open(query_input, 'r', encoding='utf-8') as file:
        original_lines = file.readlines()
    if original_lines and original_lines[0].startswith('./'):
        original_lines = original_lines[1:]

    print(f'Running cas-offinder on {len(fasta_files)} FASTA files (parallel)...')
    step_start = time.time()

    def run_cas_offinder(fasta_file):
        """Run cas-offinder on a single FASTA file"""
        target_path = fasta_file  
        off_target_output = fasta_file + '.txt'

        temp_input = os.path.join(work_dir, f"cas_input_{os.path.basename(fasta_file)}.tmp")
        with open(temp_input, 'w', encoding='utf-8') as f:
            f.write(target_path + '\n')
            f.writelines(original_lines)

        result = subprocess.run(
            ['./cas-offinder', temp_input, device_id, off_target_output],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False
        )

        try:
            os.remove(temp_input)
        except OSError:
            pass

        if result.returncode != 0:
            print(f"Error: {device_id} failed for {os.path.basename(fasta_file)}")

        return off_target_output

    if len(fasta_files) == 0:
        allelic_off_target_files = []
    else:
        if device_id.startswith('G'):
            optimal_gpu_workers = estimate_optimal_gpu_workers(device_id)
            max_workers = min(optimal_gpu_workers, len(fasta_files))
        else:
            max_workers = min(cpu_count(), len(fasta_files))

        print(f"Running cas-offinder with {max_workers} parallel workers...")
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            allelic_off_target_files = list(executor.map(run_cas_offinder, fasta_files))

    print(f"[Timing] cas-offinder execution: {time.time() - step_start:.2f}s")
    try:
        with open(combined_content, 'w', encoding='utf-8') as outfile:
            for file in allelic_off_target_files:
                with open(file, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
    except FileNotFoundError:
        uploadedfile = f"Error: {device_id} failed."
        combined_content = ''

    if len(fasta_files) == 0:
        try:
            single_multi_sample = subprocess.run(
                ["bcftools", "query", "-l", output_vcf],
                capture_output=True, text=True, check=True
            )
            num_samples = len(single_multi_sample.stdout.splitlines())
            if num_samples != 1:
                uploadedfile = f"Error: {output_vcf} is multi-sample file with {num_samples} samples. Only Phased and single sample vcf is allowed."
        except (subprocess.CalledProcessError, OSError):
            pass

    shutil.rmtree(work_dir, ignore_errors=True)
    print(f"Cleaned up work directory: {work_dir}")

    if not uploadedfile:
        if err_response:
            uploadedfile = err_response
        elif error_message:
            uploadedfile = error_message

    finished_at = time.time()
    execution_time = finished_at - created_at
    return {'success': True, 'error': {uploadedfile}, 'off_target result': {combined_content}, 'Process completed in (Seconds)': {execution_time}}


def main():
    """CLI entry point for variant-aware off-target identification."""
    parser = argparse.ArgumentParser(description="Identify potential off-target sites based on VCF files.")
    parser.add_argument('-i', '--input', type=str, required=True, help="input file name (Phased and single sample VCF file")
    parser.add_argument('-r', '--ref_path', type=str, required=True, help="Full Path to the target organism reference genome")
    parser.add_argument('-t', '--query_input', type=str, required=True, help="target sequence in the target organism genome (input.txt file)")
    parser.add_argument('-d', '--device_id', type=str, required=True, help="device_id(s): C for CPU and G for GPU, G0 for GPU device id=0")
    parser.add_argument('-w', '--workers', type=int, default=None, help="Number of parallel workers (default: CPU count)")
    args = parser.parse_args()

    output_vcf = compress_and_index(args.input, args.ref_path, args.query_input, args.device_id)
    print(f"status: {output_vcf}")

    print("Finished successfully.")


if __name__ == "__main__":
    main()
