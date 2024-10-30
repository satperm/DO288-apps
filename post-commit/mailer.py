import os
import smtplib
from email.message import EmailMessage

def send_email():
    recipient = os.getenv("EMAIL_RECIPIENT", "user@localhost")
    msg = EmailMessage()
    msg.set_content("Hello from the container!")
    msg["Subject"] = "Container Notification"
    msg["From"] = "container@example.com"
    msg["To"] = recipient

    with smtplib.SMTP("localhost") as server:
        server.send_message(msg)

if __name__ == "__main__":
    send_email()