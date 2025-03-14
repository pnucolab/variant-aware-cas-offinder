from fastapi import FastAPI, Query, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uuid
from celery_worker import off_target
from fastapi.responses import PlainTextResponse
from pam import Pam, pam_type
from target_genome import Target_Genome, ref_paths
import pandas as pd
from fastapi.responses import JSONResponse
from tabulate import tabulate
from typing import List, Optional
import duckdb
import os

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
tasks = {}
inputs = []

rofftarget = {}


@app.post('/cas_offinder_tasks', tags = ["cas_offinder"])
async def cas_offinder(Target_Genome: Target_Genome, Pam: Pam, 
                       query_seq: List[str]=Query(default="TTGTGAAATCTAAGTGTAG", title="Query Sequences without PAM from 5' to 3'"),
                         mismatches: int=Query(ge=0, le=9, default=0, title="Maximum number of mismatches between gRNA and the target genome"),
                         file:UploadFile = File(...), email: Optional[str] = Query(None)):
        #contents = await file.read()
        chunk_size = 1024 * 1024
        with open(file.filename, "wb") as f:
            while chunk := await file.read(chunk_size): 
              f.write(chunk)
         
        file_name = file.filename
        if file_name.endswith(".gz"):
           output_vcf = file.filename
        else:
           output_vcf = file.filename + ".gz"

        ref_path = ref_paths(Target_Genome) 

        PAM = pam_type(Pam)
        Target_sequence = []
        updated_data  = query_seq[0].split(' ')
        for item in updated_data:
            if item !='':
             line = item+'N'*len(PAM)+'\t'+str(mismatches)+'\n'
             Target_sequence.append(line)

        Target_sequence2= []
        for item in updated_data:
            if item != '':
             line = 'N'*len(PAM)+item+'\t'+str(mismatches)+'\n'
             Target_sequence2.append(line)

        #print(updated_data)
        #print(query_seq[0])
        if Pam == "AsCpf1 from Acidaminococcus or LbCpf1 from Lachnospiraceae: 5'-TTTV-3' (V = G or C or A)" or \
           Pam == "AsCpf1 from Acidaminococcus or LbCpf1 from Lachnospiraceae: 5'-TTTN-3'" or \
           Pam == "FnCpf1 from Francisella: 5'-KYTV-3'" or \
           Pam == "BhCas12b v4 from Bacillus hisashii: 5'-ATTN-3'" or \
           Pam == "BhCas12b v4 from Bacillus hisashii: 5'-DTTN-3'" or \
           Pam == "RR AsCpf1 from Acidaminococcus: 5'-TYCV-3'" or \
           Pam == "RVR AsCpf1 from Acidaminococcus: 5'-TATV-3'" or \
           Pam == "MAD7 nuclease: 5'-YTTV-3'" or \
           Pam == "Cas12f1 from Acidibacillus sulfuroxidans: 5'-TTTR-3'" or \
           Pam == "Cas12f1 from Acidibacillus sulfuroxidans: 5'-NTTR-3'" or \
           Pam == "DpbCasX (Cas12e) from Deltaproteobacteria: 5'-TTCN-3'" or \
           Pam == "FnCpf1 from Francisella: 5'-TTN-3'" or \
           Pam == "BhCas12b from Bacillus hisashii: 5'-TTN-3'" or \
           Pam == "LtCas12a from Cas12a family: 5'-TTNA-3'":
           pam_line = PAM+'N'*(len(updated_data[0]))+'\n'
           target_line  = Target_sequence2

        if Pam == "SpCas9 from Streptococcus pyogenes: 5'-NRG-3' (R = A or G)" or \
           Pam == "SpCas9 from streptococcus pyogenes: 5'-NGG-3'" or \
           Pam == "VQR SpCas9 from Streptococcus pyogenes: 5'-NGA-3'" or \
           Pam == "XCas9 3.7 (TLIKDIV SpCas9) from Streptococcus pyogenes: 5'-NGT-3'" or \
           Pam == "Complementary SpCas9 from Streptococcus pyogenes: 5'-NCC-3'" or \
           Pam == "SpRY Cas9 from Streptococcus pyogenes: 5'-NNN-3'" or \
           Pam == "SpRY Cas9 from Streptococcus pyogenes: 5'-NRN-3'" or \
           Pam == "NmCas9 from Neisseria meningitidis: 5'-NNNNGMTT-3' (M = A or C)" or \
           Pam == "CjCas9 from Campylobacter jejuni: 5'-NNNVRYAC-3' (V = G or C or A, R = A or G, Y = C or T)" or \
           Pam == "ThermoCas9 from Geobacillus thermodenitrificans T1: 5'-NNNNCNAA-3'" or \
           Pam == "XCas9 3.7 (TLIKDIV SpCas9) from Streptococcus pyogenes: 5'-NG-3'" or \
           Pam == "Nme2Cas9 from Neisseria meningitidis: 5'-NNNNCC-3'" or \
           Pam == "SaCas9 from Staphylococcus aureus: 5'-NNNRRT-'3 (R=A or G)" or \
           Pam == "SaCas9 from Staphylococcus aureus: 5'-NNNRRT-'3 (R=A or G)" or \
           Pam == "SpCas9 from Streptococcus pasteurianus: 5'-NNGTGA-3'" or \
           Pam == "SaCas9 from Staphylococcus aureus: 5'-NNGRRT-'3 (R=A or G)" or \
           Pam == "CcCas9 from Clostridium cellulolyticum: 5'-NNNNGNA-3'" or \
           Pam == "ThermoCas9 from Geobacillus thermodenitrificans T1: 5'-NNNNCNR-3'" or \
           Pam == "StCas9 from Streptococcus thermophilus: 5'-NNAGAAW-3' (W = A or T)" or \
           Pam == "Cas12f1 from Acidibacillus sulfuroxidans: 5'-TTTR-3'" or \
           Pam == "Cas12f1 from Acidibacillus sulfuroxidans: 5'-NTTR-3'" or \
           Pam == "Cas12f1 from Acidibacillus sulfuroxidans: 5'-NTTR-3'" or \
           Pam == "DpbCasX (Cas12e) from Deltaproteobacteria: 5'-TTCN-3'" or \
           Pam == "DpbCasX (Cas12e) from Deltaproteobacteria: 5'-TTCN-3'" or \
           Pam == "SpCas9 Variant (TAT.P5-1) from Streptococcus pyogenes: 5'-NRTH-3' (R=G or A, H=A or C orT)" or \
           Pam == "SpCas9 from Staphylococcus Auricularis: 5'-NNGG-3'" or \
           Pam == "Frcas9 from Faecalibaculum rodentium: 5'-NRTA-3' for target (R=A or G)" or \
           Pam == "Frcas9 from Faecalibaculum rodentium: 5'-NNNA-3'" or \
           Pam == "VRER SpCas9 from Streptococcus pyogenes: 5'-NGCG-3'" or \
           Pam == "Spy-macCas9 from Streptococcus pyogenes and Streptococcus macacae: 5'-NAAN-3'" or \
           Pam == "St3Cas9 from Streptococcus Thermophilus: 5'-NGGNG-3'" or\
           Pam == "SpCas9 Variant from Streptococcus pyogenes: 5'-NGC-3'":
           pam_line = 'N'*(len(updated_data[0]))+PAM+'\n'
           target_line = Target_sequence
        global rofftarget
        task_id = str(uuid.uuid4())
        output_file_name = 'off_target_allele_' + str(task_id)
        tasks[task_id] = output_file_name
        ticket = task_id
        rofftarget=off_target.apply_async([ticket, output_file_name, file_name, output_vcf, ref_path, pam_line, target_line, email], task_id=task_id)
        
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
            #task_status = rofftarget.get()
           
        existance = 'task_id exists'
        results= tasks.get(ticket)
   else:
        status = '  '
        existance = 'No such task_id'
        results= " "
        res_status = ''
            #result.info
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
    