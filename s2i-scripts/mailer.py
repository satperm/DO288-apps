import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up email details
sender = "your_username@localhost"
recipient = "leonidsokurov@localhost"
subject = "Test Email"
body = "This is a test email sent from a Python script."

# Create the email
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Send the email
try:
    with smtplib.SMTP('localhost') as server:
        server.sendmail(sender, recipient, msg.as_string())
    print("Email sent successfully.")
except Exception as e:
    print(f"Failed to send email: {e}")
