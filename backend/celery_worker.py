from celery_app import celery_task
import os
import subprocess
import time
from datetime import datetime
from io import StringIO
import pandas as pd
import duckdb
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


@celery_task.task
def off_target(ticket,output_file_name, file_name, output_vcf, ref_path,  pam_line, target_line, email):
  time.sleep(5)
  con = duckdb.connect(f"task_time_{ticket}.db")
  con.execute("CREATE TABLE IF NOT EXISTS task_times (id VARCHAR, created_at TIMESTAMP, finished_at TIMESTAMP, input_file VARCHAR)")

  created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      
  allelic_off_target_files = [] 
  combined_content = ''
  uploadedfile = ''
  string_id = ticket
  error_message = ''
  tab_index = ['tabix', '-p', 'vcf', output_vcf]
  tab_result = subprocess.run(['tabix', '-p', 'vcf', file_name], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,text=True )
  errmessage = tab_result.stderr
  single_multi_sample = subprocess.run(
                    ["bcftools", "query", "-l", file_name], 
                    capture_output=True,
                    text=True,
                    check=True
                )  
  num_samples = len(single_multi_sample.stdout.splitlines())
  if num_samples ==1:
     if "is not BGZF" in errmessage:
          if ".gz" in file_name:
               subprocess.run(['gunzip', file_name])
               unzip_file = file_name[:-3]
               subprocess.run(["bgzip", "-c", unzip_file], stdout=open(output_vcf, "wb"))
               subprocess.run(tab_index, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
               
          else:
           subprocess.run(["bgzip", "-c", file_name], stdout=open(output_vcf, "wb"))
           subprocess.run(['tabix', '-p', 'vcf', output_vcf], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
     

     vcfallelic = ["vcfallelicprimitives", output_vcf]
     norm = ["bcftools", "norm", "-m-"]
     vcfcreatemulti = ["vcfcreatemulti"]
     bgzip = ["bgzip", "-c"]
     result_file = "output_"+output_vcf
     bcftools_index = ["bcftools", "index", result_file]
     with open(result_file, 'wb') as output_file:
           vcfallelic_process = subprocess.Popen(vcfallelic, stdout=subprocess.PIPE)
           norm_process = subprocess.Popen(norm, stdin=vcfallelic_process.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
           vcfcreatemulti_process = subprocess.Popen(vcfcreatemulti, stdin=norm_process.stdout, stdout=subprocess.PIPE)
           bgzip_process = subprocess.Popen(bgzip, stdin=vcfcreatemulti_process.stdout, stdout=output_file)
     bgzip_process.communicate()
     subprocess.run(bcftools_index, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
     tab_index2 = ['tabix', '-p', 'vcf', result_file]
     subprocess.run(tab_index2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
     vcf2tsv_cmd = ['vcf2tsv', result_file]
     result  = subprocess.run(vcf2tsv_cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text = True)
     output = result.stdout
     output_file = StringIO(output)
     dtype = {
       'INFO': str,
       'FORMAT': str,
      }   
     df = pd.read_csv(output_file, sep ='\t', dtype=dtype, low_memory=False)
     unique_s = df['#CHROM'].unique()
     unique_s_str = [str(item) for item in unique_s]
   
     parent_directory = ref_path
     components = parent_directory.split(os.sep)
     first_two_components = os.sep.join(components[:-1])
     fai_files = [f for f in os.listdir(first_two_components) if f.endswith('.fai')]
     if fai_files:
          for fai_file in fai_files:
               fai_file_path = os.path.join(first_two_components, fai_file)
               with open(fai_file_path, 'r') as file:
                    lines = file.readlines()
                    if len(lines) >= 2:
                         chrom_id = lines[1][:2] 
                    else:
                         chrom_id = ''     
     chrom_item = [item for item in unique_s_str if chrom_id in item or item[0].isdigit()]
     err_response = ''
             
     if chrom_item:       
       for column_name in chrom_item:
         command = ["bcftools", "view", result_file, column_name ]
         output = f"{output_vcf}{column_name}.vcf"
         with open(output, 'w') as output:
               process = subprocess.Popen(command, stdout=output)
               process.communicate()
     else:
         err_response = "Error: #CHROM name mismatch. Please make sure you select the right target organism or modify #CHROM name in your indexed reference genome (.fai file) and try again. \
               Visit Ensembl website to check chromosomes name of your target organism reference genome." 
     input_files = [output_vcf+item + '.vcf' for item in chrom_item]
     allfastafiles = output_vcf+'.fasta'     
     def process_input_file(input_file):
         global error_message
         try:  
           vcf2fasta_cmd = ['vcf2fasta', '-f', ref_path, '-p', allfastafiles, '-n', 'NAN', input_file]
           subprocess.run(vcf2fasta_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, check = True, text=True)
           time.sleep(2)
         except subprocess.CalledProcessError as e:
            stderr_message = e.stderr.strip()
            if 'not phased' in stderr_message:
                error_message = 'Error: your vcf file is not phased. Only Phased and single sample vcf is allowed.'
            elif 'unable to find FASTA index' in stderr_message:
                error_message = 'Error: Wrong target organism selection.'
            else:
                error_message = f'Error: {stderr_message}'    

     def process_input_files(input_files):
          for input_file in input_files:
               process_input_file(input_file)
     
     process_input_files(input_files)    
         
     fasta_files = [f for f in os.listdir() if f.startswith(allfastafiles)]
     
     query_input = output_vcf+'_input.txt'
     for i in range(len(fasta_files)):
            target_path = "/app/"+fasta_files[i]+"\n"
            
            with open(query_input, "w") as file:
                 pass   

            with open(query_input, "w") as file:
                file.write(target_path)
                file.write(pam_line)
            with open(query_input, 'r') as file:
                  lines = file.readlines()
                  lines[2:] = target_line
            with open(query_input, 'w') as file:
                  for line in lines:
                       file.write(line)
            off_target_output = fasta_files[i]+'.txt'

            off_target_allele = ['/app/cas-offinder', query_input, 'G', off_target_output] # G0 -GPU id 0
            cas_result = subprocess.run(off_target_allele, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if cas_result.returncode != 0:
               off_target_allele = ['/app/cas-offinder', query_input, 'G0', off_target_output]
               cas_result = subprocess.run(off_target_allele, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
               if cas_result.returncode != 0:
                  off_target_allele = ['/app/cas-offinder', query_input, 'G1', off_target_output]
                  cas_result = subprocess.run(off_target_allele, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                  if cas_result.returncode != 0:
                     uploadedfile = "Error: Cas-OFFinder failed to run. Server error."
            allelic_off_target_files.append(off_target_output)
            try:
              with open(off_target_output, 'r') as file: 
                     combined_content += file.read()
            except FileNotFoundError:
                 uploadedfile = f"Error: server error."
                 combined_content = ''

     file_content = combined_content
     id_no = output_file_name
     db_con = duckdb.connect(f"off_target_result_{id_no}.db")
     db_con.execute("""
     CREATE TABLE IF NOT EXISTS off_target_result (
     id VARCHAR ,
     content TEXT
     )
     """)
     
     db_con.execute("INSERT INTO off_target_result (id, content) VALUES (?, ?)", (id_no, file_content))
     result_df = db_con.execute("SELECT * FROM  off_target_result").fetchdf()
     pd.set_option('display.max_colwidth', None)
     #print(result_df)
     db_con.close()

     files_to_erase =  allelic_off_target_files + fasta_files + input_files + [query_input]
    
     for file in files_to_erase:
         try:
           os.remove(file)
         except FileNotFoundError:
           single_multi_sample = subprocess.run(
                    ["bcftools", "query", "-l", output_vcf],  # List sample names in the VCF file
                    capture_output=True,
                    text=True,
                    check=True
                )  
           num_samples = len(single_multi_sample.stdout.splitlines())
           if num_samples != 1:
               uploadedfile = f"Error: {output_vcf} is multi-sample file with {num_samples} samples. \
                      Only Phased and single sample vcf is allowed."
              
           else:
               if err_response =='':
                  if error_message !='':
                      uploadedfile = error_message
               else:
                 uploadedfile = err_response
  else:
     uploadedfile = f"Error: {output_vcf} is multi-sample file with {num_samples} samples. Only Phased and single sample vcf is allowed."  
  finished_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")    
  con.execute("INSERT INTO task_times (id, created_at, finished_at, input_file) VALUES (?, ?, ?, ?)", (string_id, created_at, finished_at, uploadedfile))
  dft = con.execute("SELECT * FROM task_times").fetchdf()
  con.close()
     
  files_to_clear = [file_name, output_vcf]
  for file in files_to_clear:
     if os.path.exists(file):
          os.remove(file)
  indexed_files = [f for f in os.listdir() if f.startswith(f'output_{file_name}') or f.startswith(file_name)]
  for file in indexed_files:
          if os.path.exists(file):
               os.remove(file)
  
  smtp_host = os.getenv('SMTP_HOST', 'smtp.gmail.com')
  smtp_port = int(os.getenv('SMTP_PORT', '587'))
  smtp_email = os.getenv('SMTP_EMAIL')
  smtp_password = os.getenv('SMTP_PASSWORD')
  if not smtp_email or not smtp_password:
        print("❌ SMTP credentials are missing! Set SMTP_EMAIL and SMTP_PASSWORD as environment variables.")
        return False

    # Create email message
  msg = MIMEMultipart()
  msg['From'] = smtp_email
  msg['To'] =  email
  msg['Subject'] = 'Variant-aware Cas-OFFinder Job Completion'
  body = f"""
        Dear User,

        Your searching job is done. You can view the results at the following address:
        https://crispr.pnucolab.com/result/{ticket}

        Job Details:
        - Ticket: {ticket}
        - Created At: {created_at}
        - Finished At: {finished_at}

        Thank you for using Variant-aware Cas-OFFinder.

        Best regards,
        Variant-aware Cas-OFFinder Team
        """
  msg.attach(MIMEText(body, 'plain'))

  try:
        # Connect to SMTP server
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()  # Secure the connection
        server.login(smtp_email, smtp_password)

        # Send email
        server.send_message(msg)
        server.quit()
        
        print(f"✅ Email successfully sent to {email}")
  except Exception as e:
        print(f"❌ Failed to send email: {e}")

     
  return  {'success': True, 'created_at':created_at, 'finished_at': finished_at}