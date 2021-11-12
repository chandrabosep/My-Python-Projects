from tkinter import *
from tkinter import  ttk
from random import *

root = Tk()

list = ["rock","paper","scissors"]

pick_number = randint(0,2)

label = Label(root,text=list[pick_number],font=("arial",15))
label.pack()


def spin():
    pick_number = randint(0, 2)
    label.config(text=list[pick_number]) # changing label

    if user_input.get() == "Rock":
        user_input_value = 0
        print(0)
    elif user_input.get() == "Paper":
        user_input_value = 1
        print(1)
    elif user_input.get() == "Scissors":
        user_input_value = 2
        print(2)

    if user_input_value == 0:
        if pick_number == 0:
            wl_label.config(text="tie")
        elif pick_number == 1:
            wl_label.config(text="lose")
        elif pick_number == 2:
            wl_label.config(text="won")

    elif user_input_value == 1:
        if pick_number == 1:
            wl_label.config(text="tie")
        elif pick_number == 0:
            wl_label.config(text="won")
        elif pick_number == 2:
            wl_label.config(text="lose")

    elif user_input_value == 2:
        if pick_number == 2:
            wl_label.config(text="tie")
        elif pick_number == 0:
            wl_label.config(text="lose")
        elif pick_number == 1:
            wl_label.config(text="won")





user_input = ttk.Combobox(root,value=["Rock","Paper","Scissor"])
user_input.current(0)
user_input.pack()

wl_label = Label(root,text="",font=("castellar",15),bg="red",width=5)
wl_label.pack()

button = Button(root,text="spin",font=("castellar",15),command=spin)
button.pack()

root.mainloop()