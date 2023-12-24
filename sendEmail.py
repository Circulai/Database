import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os 


def send_email(subject, body):
    SENDER_MAIL = os.environ["SENDER_MAIL"]
    SENDER_PASSWORD = os.environ["SENDER_PASSWORD"]
    RECEIVER_MAIL = os.environ["RECEIVER_MAIL"]

    message = MIMEMultipart()
    message['From'] = SENDER_MAIL
    message['To'] = RECEIVER_MAIL
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(SENDER_MAIL, SENDER_PASSWORD)

        server.sendmail(SENDER_MAIL, RECEIVER_MAIL, message.as_string())

    print('Email sent successfully!',"subject: "+subject,"body: "+body)
    
if __name__ == "__main__":
    subject = 'Test Email'
    body = 'This is a test email sent from Python.'
    send_email(subject, body)

