import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email(ticket, created_at, finished_at, to_email):
    try:
        # Get SMTP configuration from environment variables
        from_email = os.environ.get('SMTP_EMAIL', 'your_email@example.com')
        smtp_server = os.environ.get('SMTP_HOST', 'smtp.example.com')
        smtp_port = int(os.environ.get('SMTP_PORT', 587))
        login = os.environ.get('SMTP_EMAIL', 'your_email@example.com')
        password = os.environ.get('SMTP_PASSWORD', 'your_password')
        use_tls = os.environ.get('SMTP_USE_TLS', 'True').lower() in ['true', '1', 't', 'y', 'yes']

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = 'Variant-aware Cas-OFFinder Job Completion'

        # Create the message
        message = f"""
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
        msg.attach(MIMEText(message, 'plain'))

        # Connect to the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        if use_tls:
            server.starttls()
        server.login(login, password)

        # Send the email
        server.send_message(msg)
        server.quit()

        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Example usage
# send_email('12345', '2023-10-01 10:00:00', '2023-10-01 12:00:00', 'recipient@example.com')