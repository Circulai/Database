import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


def send_email(subject, body):
    SENDER_MAIL = os.environ["SENDER_MAIL"]
    SENDER_PASSWORD = os.environ["SENDER_PASSWORD"]
    RECEIVER_MAIL = os.environ["RECEIVER_MAIL"]

    message = MIMEMultipart()
    message["From"] = SENDER_MAIL
    message["To"] = RECEIVER_MAIL
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(SENDER_MAIL, SENDER_PASSWORD)

        server.sendmail(SENDER_MAIL, RECEIVER_MAIL, message.as_string())

    print("Email sent successfully!", "subject: " + subject, "body: " + body)


if __name__ == "__main__":
    print("Running sendEmail.py as main...")
    subject = "Database just updated"
    with open("answers.json", "r") as f:
        answers = f.read()
    with open("visitsLog.json", "r") as f:
        visitLogs = f.read()

    body = f"answers: {answers}\n\nvisitLogs: {visitLogs}"
    send_email(subject, body)

    # print("Starting to read or write to test log file...")
    # fileName = "testLog.txt"
    # if os.path.exists(fileName):
    #     with open(fileName, "a") as f:
    #         f.write("\nThis got appended!")
    # else:
    #     with open(fileName, "w") as f:
    #         f.write("This is the first line of the test log file.")

    # print("File not found!")
