from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
top = Tk()
root = tkinter.Tk()
frame= ttk.Frame(root)

progressBar= ttk.Progressbar(frame, mode='indeterminate')
root.geometry("100x100+1+200")
top.geometry("165x100+1+1")
def increment():
   progressBar.step(20)


def show():
    label = ttk.Label(root, text = "Progress")
    label.pack(padx = 5, pady = 5)
    progressBar.pack(padx = 10, pady = 10)
    frame.pack(padx = 5, pady = 5)
    while progressBar["value"] < 100:
        num = askinteger("Input", "Input the Answer")
        print(num)
        increment()

B = Button(top, text ="Start Level", command = show)
B.place(x=50,y=50)




top.mainloop()
