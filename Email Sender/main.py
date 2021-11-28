import smtplib

sender = "chandrabosep3112@gmail.com"
receiver = "chandrabosep3112@gmail.com"
password = "passwordfield"
subject = "sending email through pyhton"
body = "writing an email"

mesage =f"""From:{sender}
To:{receiver}
Subject:{subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls
try:
    server.login(sender,password)
    server.send_message(sender,receiver,mesage)
except smtplib.SMTPAuthenticationError:
    print("unable to login")
except smtplib.SMTPNotSupportedError:
    print("check credientials")