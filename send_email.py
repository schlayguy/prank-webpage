import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "daveschleman@gmail.com"
password = "kkffxhfiibznkxyc"  # Your Gmail App Password
recipients = [
    "Mr.lang65@gmail.com",
    "daveschleman@gmail.com",
    "laschlemann@gmail.com",
    "bschlema@gmail.com"
]

# Email content
subject = "Mock Alert: Don't Get Banned and Scammed - Nigerian Phishing Study"
body = """
Schlayballs Security Check for GM, Squeebs, and Slippery banannas

As part of the Schlayballs Project, we're conducting a mock study on Nigerian phishing scams to keep you scam-smart. Click the link below to participate in this interactive exercise:

https://2930-70-231-13-118.ngrok-free.app/?user=friend123.

This is a safe, controlled prank to test your scam awareness. Enter any jumbo mumbo or deny the request, and stay sharp! Your response will help us analyze phishing behavior.

Stay scam-smart,
Schlayballs
"""

try:
    # Connect to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)

    # Send email to each recipient
    for recipient in recipients:
        # Create a new MIMEMultipart message for each recipient
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        server.sendmail(sender_email, recipient, msg.as_string())
        print(f"Email sent to {recipient}")

    server.quit()
    print("Email sent successfully to all recipients!")
except Exception as e:
    print(f"Error sending email: {e}")
