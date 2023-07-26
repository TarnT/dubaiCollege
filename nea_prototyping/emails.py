import smtplib
import getpass
import json

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

# connect to the SMTP server using TLS and send the email
try:

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # activate TLS encryption for security
        server.login(sender_email, sender_password)

        # create the email message
        message = f"Subject: {subject}\nFrom: {sender_email}\nTo: {recipient_email}\n\n{email_body}"
        # two new lines create seperation from headers and body
        
        # send the email
        server.sendmail(sender_email, recipient_email, message)

    print("Email sent successfully!")

except Exception as e:
    print(f"Error: {e}")