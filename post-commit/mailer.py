import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    recipient = os.environ.get("EMAIL_RECIPIENT", "default@example.com")
    subject = "Test Email"
    body = "This is a test email."

    # Set up the email
    msg = MIMEMultipart()
    msg['From'] = 'leonidsokurov@localhost'  # Replace with your email
    msg['To'] = recipient
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server and port
            server.starttls()  # Upgrade to a secure connection
            server.login('your_email@example.com', 'your_password')  # Replace with your login credentials
            server.send_message(msg)

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_email()
