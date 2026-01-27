from fastapi import FastAPI, Query, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uuid
from celery_worker import off_target
from fastapi.responses import PlainTextResponse
import pandas as pd
from fastapi.responses import JSONResponse
from tabulate import tabulate
from typing import List, Optional
import duckdb
import os
import yaml
import aiofiles
from collections import OrderedDict

app = FastAPI(root_path="/api/v1")
origins = [
    os.environ.get("ALLOWED_ORIGIN", "http://localhost"),
  ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

task_id_lists = []

def load_yaml(p, root_key):
    """Load and parse a YAML file, returning the value for the specified root key."""
    with open(p, "r", encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data[root_key]

def load_pams(filepath):
    """Load PAM sequences from a YAML configuration file."""
    pam_dict = OrderedDict()
    pam_list = load_yaml(filepath, "pams")
    for pam_entry in pam_list:
        pam_dict[pam_entry['value']] = pam_entry
    return pam_dict

def load_genomes(filepath):
    """Load genome configurations from a YAML file."""
    genome_dict = OrderedDict()
    organisms = load_yaml(filepath, "organisms")
    for organism in organisms:
        if organism['name'] == 'Favourites':
            continue
        for org_type in organism['organismtype']:
            for version in org_type['versions']:
                genome_dict[version['value']] = version
    return genome_dict

pams = load_pams("./config/pams.yml")
genomes = load_genomes("./config/organisms.yml")

@app.post('/cas_offinder_tasks', tags=["cas_offinder"])
async def cas_offinder(
    target_genome: str = Query(list(genomes.keys())[0], description="Select target genome", enum=list(genomes.keys())),
    pam: str = Query(list(pams.keys())[0], description="Select PAM type", enum=list(pams.keys())),
    query_seq: List[str] = Query(default="GTGAAATCTAAGTGTAGAG\nTTGTGAAATCTAAGTGTAG\nCTTCACAATTATTCGCCCA\nAGATTCAAGAATTGGTACG\nAACCTTCAGTTAGTCGCTA\nCACCATAGCGACTAACTGA", title="Query Sequences without PAM from 5' to 3'"),
    mismatches: int = Query(ge=0, le=9, default=3, title="Maximum number of mismatches between gRNA and the target genome"),
    file: UploadFile = File(...),
    email: Optional[str] = Query(None)
):
    """Submit a variant-aware cas-offinder task for off-target analysis."""
    task_id = str(uuid.uuid4())
    file_name_1 = file.filename

    # Use shared uploads directory
    uploads_dir = "uploads"
    os.makedirs(uploads_dir, exist_ok=True)
    file_name = os.path.join(uploads_dir, f"{task_id}{file_name_1}")

    async with aiofiles.open(file_name, "wb") as f:
        while True:
            chunk = await file.read(10*1024*1024)
            if not chunk:
                break
            await f.write(chunk)

    # output_vcf is just the base filename (used for naming in CLI)
    base_filename = f"{task_id}{file_name_1}"
    if base_filename.endswith(".gz"):
        output_vcf = base_filename
    else:
        output_vcf = base_filename + ".gz"
    ref_path = genomes[target_genome]['path']
    if not ref_path:
        raise HTTPException(status_code=400, detail="Invalid genome version selected.")
    updated_data = [seq.strip() for seq in query_seq[0].replace('\r\n', '\n').replace('\r', '\n').split('\n') if seq.strip()]
    if pams[pam]['reversed']:
        pam_line = pams[pam]['pam']+'N'*(len(updated_data[0]))+'\n'
    else:
        pam_line = 'N'*(len(updated_data[0]))+pams[pam]['pam']+'\n'

    target_lines = []
    for item in updated_data:
        if item != '':
            if pams[pam]['reversed']:
                target_lines.append('N'*len(pams[pam]['pam'])+item+'\t'+str(mismatches)+'\n')
            else:
                target_lines.append(item+'N'*len(pams[pam]['pam'])+'\t'+str(mismatches)+'\n')

    ticket = task_id
    off_target.apply_async([ticket, file_name, output_vcf, ref_path, pam_line, target_lines, email], task_id=task_id)
    task_id_lists.append(ticket)

    return {'success': True, 'ticket': task_id}

@app.get('/result', tags=['result_status'])
async def result(ticket: str):
    """Get the status of a cas-offinder task by ticket ID."""
    created_at = ''
    finished_at = ''
    input_file = ''
    res_status = ''

    # First check if job exists in database (handles completed jobs after server restart)
    db_path = os.path.join("result_data", f"task_{ticket}.db")
    if os.path.exists(db_path):
        try:
            con = duckdb.connect(db_path)
            query = "SELECT created_at, finished_at, input_file FROM task_info WHERE id = ?"
            time_result = con.execute(query, (ticket,)).fetchdf()
            con.close()
            if not time_result.empty:
                finished_at_val = time_result.iloc[0, 1]
                if finished_at_val is not None:
                    # Job is complete
                    res_status = 0
                    created_at = time_result.iloc[0, 0].strftime("%Y-%m-%d %H:%M:%S")
                    finished_at = finished_at_val.strftime("%Y-%m-%d %H:%M:%S")
                    input_file = time_result.iloc[0, 2]
                else:
                    # Job started but not finished - check Celery state
                    res_status = 1
        except Exception:  # pylint: disable=broad-exception-caught
            pass

    # If not found in database, check if it's a new job in task_id_lists
    if res_status == '' and ticket in task_id_lists:
        result_summary = off_target.AsyncResult(ticket)
        status = result_summary.state
        if status == "PENDING":
            res_status = 1
        else:
            res_status = 0

    return {'status': res_status, 'uploaded_file': input_file, 'created_at': created_at, 'finished_at': finished_at} 

@app.get('/result_detail', response_class=PlainTextResponse, tags=['result_detail'])
async def summary(
    ticket: str,
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(50, ge=1, le=500, description="Items per page"),
    crRNA: str = Query(None, description="Filter by crRNA sequence"),
    mismatches: str = Query(None, description="Filter by mismatch count"),
    gc: str = Query(None, description="Filter by GC content value")
):
    """Retrieve detailed off-target results for a completed task with pagination and filtering."""
    try:
        db_path = os.path.join('result_data', f'task_{ticket}.db')
        if not os.path.exists(db_path):
            return JSONResponse(content={'output': 'Please wait until the result is ready.'})

        con = duckdb.connect(db_path)
        query = "SELECT result_content, finished_at FROM task_info WHERE id = ?"
        pd.set_option('display.max_colwidth', None)
        query_result = con.execute(query, (ticket,)).fetchdf()
        con.close()

        if query_result.empty:
            return JSONResponse(content={'output': 'Please wait until the result is ready.'})

        # Check if task is finished (finished_at is not null)
        finished_at = query_result.iloc[0, 1]
        if finished_at is None:
            return JSONResponse(content={'output': 'Please wait until the result is ready.'})

        contents = query_result.iloc[0, 0]
        # Task is complete but no results found
        if not contents:
            return JSONResponse(content={'output': 'COMPLETED_NO_RESULTS', 'status': 'completed'})

        lines = contents.splitlines()

        # Parse all data first for filtering
        data = [line.split('\t') for line in lines]
        names = ["crRNA", "Chromosome", "Position", "DNA", "Direction", "Mismatches"]
        df_all = pd.DataFrame(data, columns=names)

        # Calculate GC content for filtering
        if not df_all.empty:
            df_all['GC'] = df_all['DNA'].apply(
                lambda x: round((x.count('G') + x.count('C') + x.count('c') + x.count('g')) / len(x) * 100, 2) if x else 0
            )

        # Apply filters
        if crRNA:
            df_all = df_all[df_all['crRNA'].str.contains(crRNA, case=False, na=False)]
        if mismatches:
            df_all = df_all[df_all['Mismatches'] == mismatches]
        if gc:
            df_all = df_all[df_all['GC'] == float(gc)]

        # Calculate pagination after filtering
        total_count = len(df_all)
        total_pages = (total_count + limit - 1) // limit if total_count > 0 else 0

        # Apply pagination
        start_idx = (page - 1) * limit
        end_idx = start_idx + limit
        df_content = df_all.iloc[start_idx:end_idx].copy()

        if not df_content.empty:

            # Split Chromosome column into Chromosome and Allele
            df_content['Allele'] = df_content['Chromosome'].str.split(':').str[1]
            df_content['Chromosome'] = df_content['Chromosome'].str.split(':').str[0]

            # Extract chromosome identifier from formats like "FORWARD_chr1", "REVERSE_1", or just "chr1"/"1"
            def extract_chrom(chrom):
                if chrom is None:
                    return chrom
                chrom = str(chrom)
                # Check if there's an underscore (e.g., FORWARD_chr1, REVERSE_1)
                if '_' in chrom:
                    # Take the part after the last underscore
                    chrom = chrom.split('_')[-1]
                return chrom
            df_content['Chromosome'] = df_content['Chromosome'].apply(extract_chrom)

            # Reorder columns: crRNA, Chromosome, Allele, Position, DNA, Direction, Mismatches, GC
            df_content = df_content[['crRNA', 'Chromosome', 'Allele', 'Position', 'DNA', 'Direction', 'Mismatches', 'GC']]

        # Return JSON data instead of tabulated string for better frontend handling
        records = df_content.to_dict(orient='records')

        return JSONResponse(content={
            'status': 'completed',
            'data': records,
            'pagination': {
                'page': page,
                'limit': limit,
                'total_count': total_count,
                'total_pages': total_pages
            }
        })
    except Exception:  # pylint: disable=broad-exception-caught
        return JSONResponse(content={'output': 'Please wait until the result is ready.'})

@app.get('/result_summary', tags=['result_summary'])
async def result_summary(ticket: str):
    """Get summary statistics for off-target results grouped by crRNA."""
    try:
        db_path = os.path.join('result_data', f'task_{ticket}.db')
        if not os.path.exists(db_path):
            return JSONResponse(content={'output': 'Please wait until the result is ready.'})

        con = duckdb.connect(db_path)
        query = "SELECT result_content, finished_at FROM task_info WHERE id = ?"
        query_result = con.execute(query, (ticket,)).fetchdf()
        con.close()

        if query_result.empty:
            return JSONResponse(content={'output': 'Please wait until the result is ready.'})

        finished_at = query_result.iloc[0, 1]
        if finished_at is None:
            return JSONResponse(content={'output': 'Please wait until the result is ready.'})

        contents = query_result.iloc[0, 0]
        if not contents:
            return JSONResponse(content={'output': 'COMPLETED_NO_RESULTS', 'status': 'completed', 'summary': []})

        lines = contents.splitlines()
        data = [line.split('\t') for line in lines]
        names = ["crRNA", "Chromosome", "Position", "DNA", "Direction", "Mismatches"]
        df = pd.DataFrame(data, columns=names)

        # Split Chromosome into Chromosome and Allele
        df['Allele'] = df['Chromosome'].str.split(':').str[1]
        df['Chromosome'] = df['Chromosome'].str.split(':').str[0]

        # Extract chromosome identifier from formats like "FORWARD_chr1", "REVERSE_1", or just "chr1"/"1"
        def extract_chrom(chrom):
            if chrom is None:
                return chrom
            chrom = str(chrom)
            # Check if there's an underscore (e.g., FORWARD_chr1, REVERSE_1)
            if '_' in chrom:
                # Take the part after the last underscore
                chrom = chrom.split('_')[-1]
            return chrom
        df['Chromosome'] = df['Chromosome'].apply(extract_chrom)

        # Get unique alleles to determine which ones exist
        unique_alleles = sorted(df['Allele'].dropna().unique().tolist())

        # Natural sort key for chromosomes (chr1, chr2, ..., chr10, chr11, ..., chrX, chrY)
        def chrom_sort_key(chrom):
            if chrom is None:
                return (2, 0, '')
            chrom = str(chrom)
            # Remove 'chr' prefix if present for sorting
            chrom_id = chrom[3:] if chrom.lower().startswith('chr') else chrom
            # Try to convert to int for numeric chromosomes
            try:
                return (0, int(chrom_id), '')
            except ValueError:
                # Non-numeric chromosomes (X, Y, M, MT) come after numeric
                return (1, 0, chrom_id)

        # Group by crRNA and Chromosome to get allele counts per chromosome
        summary_data = []
        for (crrna, chrom), group in df.groupby(['crRNA', 'Chromosome']):
            # Count each unique allele
            allele_counts = group['Allele'].value_counts().to_dict()
            # Get counts for first two alleles (usually '1' and '2', or '0' and '1')
            allele_1_val = unique_alleles[0] if len(unique_alleles) > 0 else '1'
            allele_2_val = unique_alleles[1] if len(unique_alleles) > 1 else '2'
            allele_1_count = allele_counts.get(allele_1_val, 0)
            allele_2_count = allele_counts.get(allele_2_val, 0)
            summary_data.append({
                'crRNA': crrna,
                'length': len(crrna),
                'chromosome': chrom,
                'allele_1_count': allele_1_count,
                'allele_2_count': allele_2_count,
                'allele_1_label': allele_1_val,
                'allele_2_label': allele_2_val
            })

        # Sort by crRNA first, then by chromosome in natural order
        summary_data.sort(key=lambda x: (x['crRNA'], chrom_sort_key(x['chromosome'])))

        return JSONResponse(content={
            'status': 'completed',
            'summary': summary_data
        })
    except Exception:  # pylint: disable=broad-exception-caught
        return JSONResponse(content={'output': 'Please wait until the result is ready.'})

@app.get('/result_filter_options', tags=['result_filter_options'])
async def result_filter_options(ticket: str):
    """Get available filter options (unique mismatches and GC values) for a completed task."""
    try:
        db_path = os.path.join('result_data', f'task_{ticket}.db')
        if not os.path.exists(db_path):
            return JSONResponse(content={'output': 'Please wait until the result is ready.'})

        con = duckdb.connect(db_path)
        query = "SELECT result_content, finished_at FROM task_info WHERE id = ?"
        query_result = con.execute(query, (ticket,)).fetchdf()
        con.close()

        if query_result.empty:
            return JSONResponse(content={'output': 'Please wait until the result is ready.'})

        finished_at = query_result.iloc[0, 1]
        if finished_at is None:
            return JSONResponse(content={'output': 'Please wait until the result is ready.'})

        contents = query_result.iloc[0, 0]
        if not contents:
            return JSONResponse(content={'status': 'completed', 'mismatches': [], 'gc_values': []})

        lines = contents.splitlines()
        data = [line.split('\t') for line in lines]
        names = ["crRNA", "Chromosome", "Position", "DNA", "Direction", "Mismatches"]
        df = pd.DataFrame(data, columns=names)

        # Get unique mismatches values
        unique_mismatches = sorted(df['Mismatches'].dropna().unique().tolist(), key=lambda x: int(x) if x.isdigit() else 999)

        # Calculate GC content for each DNA sequence and get unique values
        def calc_gc(dna):
            if not dna:
                return 0
            gc_count = dna.count('G') + dna.count('C') + dna.count('c') + dna.count('g')
            return round(gc_count / len(dna) * 100, 2)

        df['GC'] = df['DNA'].apply(calc_gc)
        unique_gc_values = sorted(df['GC'].dropna().unique().tolist())

        return JSONResponse(content={
            'status': 'completed',
            'mismatches': unique_mismatches,
            'gc_values': unique_gc_values
        })
    except Exception:  # pylint: disable=broad-exception-caught
        return JSONResponse(content={'output': 'Please wait until the result is ready.'})