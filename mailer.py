import os
import random
import smtplib
import ssl

from dotenv import load_dotenv
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load local environment
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

sender_email = os.environ.get('MAIL_SENDER_EMAIL', '')
password = os.environ.get('MAIL_SENDER_PASSWORD', '')
receiver_email = os.environ.get('MAIL_RECIPIENTS_EMAILS', '').split(';')

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["Subject"] = os.environ.get('MAIL_SUBJECT', "")
message["Bcc"] = ", ".join(receiver_email)

# Add body to email
message.attach(MIMEText(os.environ.get('MAIL_CONTENT', ""), "plain"))

# Retrieve random file from folder data
filename = random.choice(os.listdir('./data'))
filepath = f"data/{filename}"  # In same directory as script

# Open file in binary mode
with open(filepath, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
