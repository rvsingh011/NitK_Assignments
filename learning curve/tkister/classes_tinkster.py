from tkinter import *

class Ravi:
    def __init__(self, master):
        frame = Frame(master).pack()
        self.print_button = Button(frame, text="hello", command=self.hello).pack()
        #frame.quit is depricated in pyhton 3.5. use master.destroy
        self.close_button = Button(frame, text="Quit", command=master.destroy).pack()

    def hello(self):
        print("hello I am Ravi Singh")

root = Tk()
r = Ravi(root)
root.mainloop()