from tkinter import *
import random
import string

def generate_password():
    password=[]
    for i in range(8):
        alpha=random.choice(string.ascii_letters)
        symbol=random.choice(string.punctuation)
        numbers=random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(numbers)
    password_string="".join(str(x) for x in password)
    label.config(text=password_string)


root=Tk()
root.geometry("300x400")
button=Button(root,text="Generate Password",command=generate_password)
button.grid(row=4,column=4)
label=Label(root,font=("times",24,"bold"))
label.grid(row=6,column=8)
root.mainloop()
