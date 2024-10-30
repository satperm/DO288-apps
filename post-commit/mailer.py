import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    recipient = "recipient@example.com"  # Change to your localhost email
    subject = "Test Email from Container"
    body = "This is a test email sent from an OpenShift container."

    # Set up the email
    msg = MIMEMultipart()
    msg['From'] = 'your_email@example.com'  # Replace with your email
    msg['To'] = recipient
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Use your macOS IP address instead of localhost
        smtp_server = "192.168.1.47"  # Replace with your macOS IP address
        smtp_port = 25  # Default port for SMTP

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.send_message(msg)

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_email()
