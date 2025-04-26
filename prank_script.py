import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "your_email@gmail.com"  # Replace with your Gmail address
receiver_email = "Mr.Lang65@gmail.com"
password = "kkff xhfi ibzn kxyc"
prank_url = "https://<ngrok-id>.ngrok.io/?user=friend123"  # Replace with ngrok URL

msg = MIMEMultipart('alternative')
msg['Subject'] = 'Be On Alert!'
msg['From'] = sender_email
msg['To'] = receiver_email

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Be On Alert!</title>
</head>
<body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">
    <div style="max-width: 600px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; text-align: center;">
        <h1 style="color: #ff5555;">Be On Alert!</h1>
        <p style="font-size: 16px; color: #333;">
            Hey there! Schlayballs wants to know your social security number? Don't worry - he won't hack you or nothin.
            Click below to accept or deny this totally legit request!
        </p>
        <a href="{prank_url}" style="display: inline-block; padding: 10px 20px; background-color: #55ff55; color: white; text-decoration: none; border-radius: 5px;">Click Here to Respond</a>
        <p style="font-size: 14px; color: #666; margin-top: 20px;">
            If you suspect this is a scam, you're probably right! Always be cautious with emails like this.
        </p>
    </div>
</body>
</html>
'''
text = f'''Hey there! Schlayballs wants your social security number? Just kidding! Click here to respond: {prank_url}
If you suspect this is a scam, you're probably right! Always be cautious.'''

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')
msg.attach(part1)
msg.attach(part2)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
