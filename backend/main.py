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
from collections import OrderedDict

app = FastAPI(root_path="/api/v1")
origins = [
    os.environ.get("ALLOWED_ORIGIN", "http://localhost",),
  ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

task_id_lists = []
tasks = {}
inputs = []

def load_yaml(p, root_key):
    with open(p, "r") as f:
        data = yaml.safe_load(f)
    return data[root_key]

def load_pams(p):
    pams = OrderedDict()
    y = load_yaml(p, "pams")
    for p in y:
        pams[p['value']] = p
    return pams

def load_genomes(p):
    genomes = OrderedDict()
    y = load_yaml(p, "organisms")
    for g in y:
        if g['name'] == 'Favourites':
            continue
        for t in g['organismtype']:
            for v in t['versions']:
                genomes[v['value']] = v
    return genomes

pams = load_pams("./config/pams.yml")
genomes = load_genomes("./config/organisms.yml")

@app.post('/cas_offinder_tasks', tags = ["cas_offinder"])
async def cas_offinder( target_genome: str = Query(list(genomes.keys())[0], description="Select target genome", enum=list(genomes.keys())),
                        pam: str = Query(list(pams.keys())[0], description="Select PAM type", enum=list(pams.keys())), 
                        query_seq: str=Query(default="TTGTGAAATCTAAGTGTAG", title="Query Sequences without PAM from 5' to 3'"),
                        mismatches: int=Query(ge=0, le=9, default=3, title="Maximum number of mismatches between gRNA and the target genome"),
                        file:UploadFile = File(...), email: Optional[str] = Query(None)):
        chunk_size = 1024 * 1024
        with open(file.filename, "wb") as f:
            while chunk := await file.read(chunk_size): 
              f.write(chunk)
         
        file_name = file.filename
        if file_name.endswith(".gz"):
           output_vcf = file.filename
        else:
           output_vcf = file.filename + ".gz"
        ref_path = genomes[target_genome]['path']
        if not ref_path:
            raise HTTPException(status_code=400, detail="Invalid genome version selected.")
        query_lines = query_seq.split('\n')
        query_lines = query_seq.split('\n')
        if pams[pam]['reversed']:
            pam_line = pams[pam]['pam']+'N'*(len(query_lines[0]))+'\n'
        else:
            pam_line = 'N'*(len(query_lines[0]))+pams[pam]['pam']+'\n'

        target_lines = []
        for item in query_lines:
            if item !='':
                if pams[pam]['reversed']:
                    target_lines.append('N'*len(pams[pam]['pam'])+item+'\t'+str(mismatches)+'\n')
                else:
                    target_lines.append(item+'N'*len(pams[pam]['pam'])+'\t'+str(mismatches)+'\n')
        task_id = str(uuid.uuid4())
        output_file_name = 'off_target_allele_' + str(task_id)
        tasks[task_id] = output_file_name
        ticket = task_id
        off_target.apply_async([ticket, output_file_name, file_name, output_vcf, ref_path, pam_line, target_lines, email], task_id=task_id)
        
        task_id_lists.append(ticket)     
        
        return {'success': True, 'ticket': task_id}

@app.get('/result', tags = ['result_status'])
async def result(ticket:str):
   created_at = ''
   finished_at = ''
   input_file = ''
   result_summary = off_target.AsyncResult(ticket)
   if ticket in task_id_lists:
        status = result_summary.state
        if status == "PENDING":
            res_status = 1                 
        else:
            res_status = 0
            con = duckdb.connect(f"task_time_{ticket}.db")
            specific_id = ticket
            query = "SELECT created_at, finished_at, input_file FROM task_times WHERE id = ?"
            time_result = con.execute(query, (specific_id,)).fetchdf()
            if not time_result.empty:
               created_at = time_result.iloc[0, 0].strftime("%Y-%m-%d %H:%M:%S")
               finished_at = time_result.iloc[0, 1].strftime("%Y-%m-%d %H:%M:%S")
               input_file = time_result.iloc[0,2]
            else:
               created_at = ''
               finished_at = ''
               input_file = ''
            con.close()
           
           
        existance = 'task_id exists'
        results= tasks.get(ticket)
   else:
        status = '  '
        existance = 'No such task_id'
        results= " "
        res_status = ''
            
   return {'status': res_status, 'uploaded_file': input_file,'created_at': created_at, 'finished_at': finished_at} 

@app.get('/result_detail',  response_class =  PlainTextResponse, tags = ['result_detail'])
async def summary(output_file_name: str):
      try:
          con = duckdb.connect(f'off_target_result_{output_file_name}.db')
          id_no = output_file_name
          query = "SELECT content FROM off_target_result WHERE id = ? "
          pd.set_option('display.max_colwidth', None) 
          result = con.execute(query, (id_no,)).fetchdf()
          if result.empty:
              raise HTTPException(status_code=404, detail="No records found for the given id")
          contents = result.iloc[0, 0]
          lines = contents.splitlines()
          data = [line.split('\t') for line in lines]
          names=["crRNA", "Chromosome", "Position", "DNA", "Direction", "Mismatches"]
          df_content = pd.DataFrame(data, columns=names)
          for dna_seq in df_content['DNA']: 
           df_content['GC'] = round((df_content['DNA'].apply(lambda x: x.count('G') + x.count('C') + x.count('c') + x.count('g')))/(len(dna_seq))*100,2)

          chromosome = df_content['Chromosome'].str.split(':').str[0]
          allele = df_content['Chromosome'].str.split(':').str[1]
          df_content['Chromosome'] =chromosome
   
          df_content = pd.concat([df_content.iloc[:, :2], allele, df_content.iloc[:, 2:]], axis =1)
    
          new_headers = ["crRNA", "Chromosome", "Allele", "Position", "DNA", "Direction", "Mismatches", "GC"]
          def generate_output(table_str):
           return table_str
     
          table_str = tabulate(df_content, headers=new_headers, tablefmt="jira", showindex=False)
     
          output_final = generate_output(table_str)
          return JSONResponse(content = {'output': output_final})
      except:
        error_message = 'Please wait until the result is ready.'
        return JSONResponse(content = {'output': error_message})
    