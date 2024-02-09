import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Read data from CSV
data = pd.read_csv(r'C:\', usecols=['receiver', 'name', 'description'])

# Email account details
smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587
username = 'example@outlook.com'
password = '1234'
sender_email = 'example@outlook.com'

# Compose email template
email_template = '''Dear {name},

Good Day to You!

Your email status for {description} has been sent successfully.

Thank you.

Best regards,
kimiey.dev

-----This is an auto-generated email, please do not reply to this message-----'''

# Set up the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(username, password)

# Send the emails
for index, row in data.iterrows():
    receiver = row['receiver']
    name = row['name']
    description = row['description']
    
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver
    msg['Subject'] = f"Mini Project Bulk Email Test: {description}"
    email_content = email_template.format(receiver=receiver, name=name, description=description)
    msg.attach(MIMEText(email_content, 'plain'))
    
    # Send the email
    server.send_message(msg)
    
# Close the SMTP server
server.quit()
print("Emails sent successfully!")