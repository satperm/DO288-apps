import os
import subprocess

def send_email():
    recipient = os.environ.get("EMAIL_RECIPIENT", "default@example.com")
    subject = "Test Email"
    body = "This is a test email."

    # Create a temporary email message
    email_message = f"To: {recipient}\nSubject: {subject}\n\n{body}"

    # Use msmtp to send the email
    process = subprocess.run(
        ["msmtp", recipient],
        input=email_message,
        text=True
    )
    
    if process.returncode != 0:
        print("Failed to send email:", process.stderr)

if __name__ == "__main__":
    send_email()