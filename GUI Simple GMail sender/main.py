import smtplib
from tkinter import *

root = Tk()
root.geometry("300x200")

def send():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls
    try:
        server.login(sender,password)
        server.send_message(sender,receiver,mesage)
    except smtplib.SMTPAuthenticationError:
        print("unable to login")
        label.config("Unable to login")
    except smtplib.SMTPNotSupportedError:
        print("check credientials")
        label.config(text="Check credientials")

frame=Frame()

Label(root,text="TO").grid(row=0,column=0,padx=20)
sender = Entry(root,font=("bell mt",10))
sender.grid(row=0,column=1)

Label(root,text="From").grid(row=1,column=0,padx=20)
receiver = Entry(root,font=("bell mt",10))
receiver.grid(row=1,column=1)

Label(root,text="Password").grid(row=2,column=0,padx=20)
password = Entry(root,font=("bell mt",10))
password.grid(row=2,column=1)

Label(root,text="Subject").grid(row=3,column=0,padx=20)
subject = Entry(root,font=("bell mt",10))
subject.grid(row=3,column=1)

Label(root,text="Body").grid(row=4,column=0,padx=20)
body = Entry(root,font=("bell mt",10))
body.grid(row=4,column=1)


Button(root,text="Send",command=send).grid(row=5,column=1)

label = Label(root,text="",font="consolas")
label.grid(row=6,column=1)

mesage =f"""From:{sender.get}
To:{receiver.get}
Subject:{subject.get}\n
{body.get}
"""

root.mainloop()