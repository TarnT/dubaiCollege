import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

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

path_to_html = "email_template.html"
with open(path_to_html, "r") as html_file:
    html_content = html_file.read()

path_to_image = "/Users/tarntimmermans/Documents/nea_testing_docs/20230430_134103000_iOS.jpg"
with open(path_to_image, "rb") as photo_file:
    photo_image = MIMEImage(photo_file.read())
    photo_image.add_header("Content-ID", "watch")

# create the email message object
message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = sender_email
message["To"] = recipient_email

# attach the plain text and HTML versions
message.attach(MIMEText(email_body, "plain"))
message.attach(MIMEText(html_content, "html"))
message.attach(photo_image)

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