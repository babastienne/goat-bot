import os
import random
import smtplib
import ssl

from dotenv import load_dotenv
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import mailing_list


def retrieve_and_encode_attachment(filepath, filename):
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

    return part


def create_mail(subject, content, recipients, path_to_data, sender_email, filename, filepath):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["Subject"] = subject
    # message["Bcc"] = ", ".join(recipients)

    # Add body to email
    message.attach(MIMEText(content, "plain"))

    attachment = retrieve_and_encode_attachment(filepath, filename)

    # Add attachment to message and convert message to string
    message.attach(attachment)

    return message.as_string()


def send_mails(sender_email, password, mails):
    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        for mail in mails:
            server.sendmail(
                from_addr=sender_email,
                to_addrs=mail[0],
                msg=mail[1]
            )


def main():
    # Load local environment
    basedir = os.path.abspath(os.path.dirname(__file__))
    load_dotenv(os.path.join(basedir, '.env'))

    sender_email = os.environ.get('MAIL_SENDER_EMAIL', '')
    password = os.environ.get('MAIL_SENDER_PASSWORD', '')
    path_to_data = os.environ.get('PATH_TO_DATA_FOLDER', '')
    path_to_used_data = os.environ.get('PATH_TO_OLD_DATA_FOLDER', '')
    languages = os.environ.get('LANGUAGES', "")
    languages = [str(t[1:-1]) for t in languages[1:-1].split(', ') if t]  # Yep, that's ugly, but I'm tired so it'll do the job.

    # Retrieve random file from folder data
    filename = random.choice(os.listdir(path_to_data))
    filepath = f"{path_to_data}/{filename}"

    mails = []

    if len(languages):
        for lang in languages:
            subject = os.environ.get(f'MAIL_SUBJECT_{lang.upper()}', "")
            content = os.environ.get(f'MAIL_CONTENT_{lang.upper()}', "")
            recipients = getattr(mailing_list, f"RECIPIENTS_{lang.upper()}")
            text = create_mail(subject, content, recipients, path_to_data, sender_email, filename, filepath)
            mails.append((recipients, text))

    else:
        subject = os.environ.get('MAIL_SUBJECT', "")
        content = os.environ.get('MAIL_CONTENT', "")
        recipients = getattr(mailing_list, "RECIPIENTS")
        text = create_mail(subject, content, recipients, path_to_data, sender_email, filename, filepath)
        mails.append((recipients, text))

    send_mails(sender_email, password, mails)

    # Move used picture to another folder to avoid using it again
    os.rename(f"{path_to_data}/{filename}", f"{path_to_used_data}/{filename}")


main()
