import sys
from tkinter import *
root = Tk()

def hello(variable1, variable2):
    print("hello")
    print(variable1)
    print(variable2)

username = StringVar()
password = StringVar()
Label(root, text="Number of Vm's ").grid(row=0, column=0, sticky=E)
Label(root, text="Enter the number of Memory ").grid(row=1, column=0, sticky=E)
Entry(root, textvariable=username).grid(row=0, column=1)
Entry(root, textvariable=password).grid(row=1, column=1)
button = Button(root, text="Login", command=lambda : hello(username.get(),password.get())).grid(columnspan=2, sticky=S)

root.mainloop()




root.mainloop()