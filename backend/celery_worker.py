from celery_app import celery_task
import os
import subprocess
import shutil
import time
import glob
import re
from datetime import datetime
import duckdb
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


CLI_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'cli')


@celery_task.task
def off_target(ticket, file_name, output_vcf, ref_path, pam_line, target_lines, email):
    """Celery task to run variant-aware cas-offinder and store results in DuckDB."""
    time.sleep(5)

    db_dir = "result_data"
    os.makedirs(db_dir, exist_ok=True)
    db_path = os.path.join(db_dir, f"task_{ticket}.db")
    con = duckdb.connect(db_path)
    con.execute("""
        CREATE TABLE IF NOT EXISTS task_info (
            id VARCHAR PRIMARY KEY,
            created_at TIMESTAMP,
            finished_at TIMESTAMP,
            input_file VARCHAR,
            result_content TEXT
        )
    """)

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    uploadedfile = ''
    combined_content = ''

    base_name = os.path.basename(file_name)
    uuid_pattern = r'^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'
    original_name = re.sub(uuid_pattern, '', base_name)
    if not original_name:
        original_name = base_name  
    cli_input_file = os.path.join(CLI_DIR, original_name)
    shutil.copy2(file_name, cli_input_file)
    query_input = os.path.join(CLI_DIR, output_vcf + '_input.txt')
    with open(query_input, "w", encoding='utf-8') as f:
        f.write("./\n")  # Placeholder
        f.write(pam_line)
    with open(query_input, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lines[2:] = target_lines
    with open(query_input, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)

    result = subprocess.run(
        [
            'python3', 'vcf-cas-offinder.py',
            '-i', original_name,
            '-r', ref_path,
            '-t', os.path.basename(query_input),
            '-d', 'G'
        ],
        cwd=CLI_DIR,
        capture_output=True,
        text=True, check=False
    )

    print(f"vcf-cas-offinder stdout: {result.stdout}")
    if result.stderr:
        print(f"vcf-cas-offinder stderr: {result.stderr}")

    result_pattern = os.path.join(CLI_DIR, f"*{original_name}_off_target_result.txt")
    matching_files = glob.glob(result_pattern)

    if matching_files:
        matching_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    result_file_path = matching_files[0] if matching_files else None
    result_file_name = f"{ticket}{original_name}_off_target_result.txt"

    if result_file_path and os.path.exists(result_file_path):
        with open(result_file_path, 'r', encoding='utf-8') as f:
            combined_content = f.read()
        shutil.copy2(result_file_path, result_file_name)
    else:
        if 'Error:' in result.stdout:
            uploadedfile = result.stdout.split('Error:')[-1].strip().split('\n')[0]
        elif result.returncode != 0:
            uploadedfile = f"Error: vcf-cas-offinder failed with return code {result.returncode}"

    file_content = combined_content

    cli_files_to_remove = [
        os.path.join(CLI_DIR, original_name),  # Input VCF file
        os.path.join(CLI_DIR, os.path.basename(query_input)),  # Query input file
    ]
    
    if result_file_path:
        cli_files_to_remove.append(result_file_path)

    for f in cli_files_to_remove:
        if os.path.exists(f):
            try:
                os.remove(f)
            except OSError:
                pass

    backend_files_to_remove = [
        file_name,  # Uploaded file with UUID prefix
        result_file_name,  # Result file copy (content is in DuckDB)
    ]
    for f in backend_files_to_remove:
        if os.path.exists(f):
            try:
                os.remove(f)
            except OSError:
                pass

    # Record task completion with all data
    finished_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    con.execute(
        "INSERT INTO task_info (id, created_at, finished_at, input_file, result_content) VALUES (?, ?, ?, ?, ?)",
        (ticket, created_at, finished_at, uploadedfile, file_content)
    )
    con.close()

    # Email Notification
    smtp_host = os.getenv('SMTP_HOST', 'smtp.gmail.com')
    smtp_port = int(os.getenv('SMTP_PORT', '587'))
    smtp_email = os.getenv('SMTP_EMAIL')
    smtp_password = os.getenv('SMTP_PASSWORD')
    if not smtp_email or not smtp_password:
        print("SMTP credentials are missing! Set SMTP_EMAIL and SMTP_PASSWORD as environment variables.")
        return False

    msg = MIMEMultipart()
    msg['From'] = smtp_email
    msg['To'] = email
    msg['Subject'] = 'Variant-aware Cas-OFFinder Job Completion'
    body = f"""
        Dear User,

        Your searching job is done. You can view the results at the following address:
        https://rgetoolkit.com/var-cas-offinder/result/{ticket}

        Job Details:
        - Ticket: {ticket}
        - Created At: {created_at}
        - Finished At: {finished_at}

        Thank you for using RGE Toolkit.

        Best regards,
        RGE Toolkit Team
        """
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        server.login(smtp_email, smtp_password)
        server.send_message(msg)
        server.quit()
        print(f"Email successfully sent to {email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

    return {'success': True, 'created_at': created_at, 'finished_at': finished_at}
