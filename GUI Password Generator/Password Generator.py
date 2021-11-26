import string
from random import *
from tkinter import *

root = Tk()

root.geometry("350x100")

def spin():
    character = string.ascii_letters+string.digits+string.punctuation
    password = "".join(choice(character) for x in range(randint(12,12)))
    print(password)
    label.config(text=password)


frame = Frame(root)
frame.pack()

lbl = Label(frame,text="PASSWORD:",font=("bell mt",20))
lbl.grid(row=0,column=0)

label = Label(frame,text="                   ",font=("ariak",15),bg="#b4d86c")
label.grid(row=0,column=1)

button = Button(root,text="Generate",font =("bell mt",15),command=spin)
button.pack(padx=30)

root.mainloop()
