import smtplib
from email.message import EmailMessage

from receiving_input import initialize_all_data

# vars:
EMAIL_ADDRESS = "travelyahel@gmail.com"
RECEIVER_MAIL = "travelyahel@gmail.com" #"dugma.travels@gmail.com"
EMAIL_PASSWORD = "fqts pzvw ojns fnyd"
email_subject = "Information about cancellation of client"  # FIRST NAME + SECOND NAME
body = """ this message is about the flight cancellation """  # + ALL INFO

# creating message
msg = EmailMessage()
msg["Subject"] = email_subject
msg["From"] = EMAIL_ADDRESS
msg["To"] = RECEIVER_MAIL
msg.set_content(body)

# connecting to server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.ehlo()

# login in and sending the email message, run this code every 30 days
server.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
server.send_message(msg)

all_data = initialize_all_data()
for row in all_data:


