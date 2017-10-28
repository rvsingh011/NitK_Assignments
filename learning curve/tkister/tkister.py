import sys
from tkinter import *
root = Tk()

def hello(variable1, variable2):
    print("hello")
    print(variable1)
    print(variable2)

username = StringVar()
password = StringVar()
label1 = Label(root, text="Name: ").grid(row=0, column=0, sticky=E)
label2 = Label(root, text="Password: ").grid(row=1, column=0, sticky=E)
input1 = Entry(root, textvariable=username).grid(row=0, column=1)
input2 = Entry(root, textvariable=password).grid(row=1, column=1)
c = Checkbutton(root, text="Keep Me Logged In").grid(columnspan=2, sticky=E)
button = Button(root, text="Login", command=lambda : hello(username.get(),password.get())).grid(columnspan=2, sticky=S)

root.mainloop()




root.mainloop()