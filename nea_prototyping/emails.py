import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

password_file_route = "/Users/tarntimmermans/Documents/nea_passwords/nea_passwords.py"
with open(password_file_route, "r") as password_file:
    password_data = json.load(password_file)

# set up the SMTP server and login credentials
smtp_server = "smtp.gmail.com" 
smtp_port = 587  # used for TLS with google SMTP server
sender_email = password_data["poxyglue"]["email"]
sender_password = password_data["poxyglue"]["password"]

# create the email message content
subject = "Testing"
recipient_email = "tsquaredevelopment@gmail.com" 

email_body = """\
Hi me,

This is an email sent using Python.

Cheers,

Me.
"""

html_email_body = """\
<html>
<body>
    <p>Hi,</p>
    <p>This is the <b>HTML</b> version of the email.</p>
    <p>Tarn</p>
</body>
</html>
"""

# create the email message object
message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = sender_email
message["To"] = recipient_email

# attach the plain text and HTML versions
message.attach(MIMEText(email_body, "plain"))
message.attach(MIMEText(html_email_body, "html"))

# connect to the SMTP server using TLS and send the email
try:

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # activate TLS encryption for security
        server.login(sender_email, sender_password)
        
        # send the email
        server.sendmail(sender_email, recipient_email, message.as_string())

    print("Email sent successfully!")

except Exception as e:
    print(f"Error: {e}")