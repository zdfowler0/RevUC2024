# import back end
import MathGame

#tkinter/GUI libraries
from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter

#define
top = Tk()
root = tkinter.Tk()
frame= ttk.Frame(root)

#Create Progress bar and button GUI

root.geometry("275x150+1+200")
top.geometry("1520x100+1+1")

#def increment():
   #progressBar.step(20)

#define problem box one
def problem_box_one():
    label = ttk.Label(root, text = "Progress")
    label.pack(padx = 5, pady = 5)
    progressBar= ttk.Progressbar(frame, mode='indeterminate')
    progressBar.pack(padx = 10, pady = 10)
    frame.pack(padx = 5, pady = 5)
    
    while progressBar["value"] < 100:
        problem = MathGame.generate_problem(1)
        num = askinteger("Input", f"Input the Answer to {problem}")
        print(num)
        if num == MathGame.ans:
            progressBar.step(20)
        elif num == None:
            return 0
    
    label = ttk.Label(root, text = "Congratulations, You have passed level one")
    label.pack(padx = 5, pady = 5)

#define problem box two
def problem_box_two():
    label = ttk.Label(root, text = "Progress")
    label.pack(padx = 5, pady = 5)
    progressBar= ttk.Progressbar(frame, mode='indeterminate')
    progressBar.pack(padx = 10, pady = 10)
    frame.pack(padx = 5, pady = 5)
    
    while progressBar["value"] < 100:
        problem = MathGame.generate_problem(2)
        num = askinteger("Input", f"Input the Answer to {problem}")
        print(num)
        if num == MathGame.ans:
           progressBar.step(20)
        elif num == None:
            return 0
    
    label = ttk.Label(root, text = "Congratulations, you have passed level two!")
    label.pack(padx = 5, pady = 5)


#define problem box 3
def problem_box_three():
    label = ttk.Label(root, text = "Progress")
    label.pack(padx = 5, pady = 5)
    progressBar= ttk.Progressbar(frame, mode='indeterminate')
    progressBar.pack(padx = 10, pady = 10)
    frame.pack(padx = 5, pady = 5)
    
    while progressBar["value"] < 100:
        problem = MathGame.generate_problem(3)
        num = askinteger("Input", f"Input the Answer to {problem}")
        print(num)
        if num == MathGame.ans:
            progressBar.step(20)
        elif num == None:
            return 0
    
    label = ttk.Label(root, text = "Congratulations, you have passed level three!")
    label.pack(padx = 5, pady = 5)

#define problem box 4
def problem_box_four():
    label = ttk.Label(root, text = "Progress")
    label.pack(padx = 5, pady = 5)
    progressBar= ttk.Progressbar(frame, mode='indeterminate')
    progressBar.pack(padx = 10, pady = 10)
    frame.pack(padx = 5, pady = 5)
    
    while progressBar["value"] < 100:
        problem = MathGame.generate_problem(4)
        num = askinteger("Input", f"Input the Answer to {problem}")
        print(num)
        if num == MathGame.ans:
            progressBar.step(20)
        elif num == None:
            return 0
    
    label = ttk.Label(root, text = "Congratulations, you have passed level four!")
    label.pack(padx = 5, pady = 5)

#define problem box 5
def problem_box_five():
    label = ttk.Label(root, text = "Progress")
    label.pack(padx = 5, pady = 5)
    progressBar= ttk.Progressbar(frame, mode='indeterminate')
    progressBar.pack(padx = 10, pady = 10)
    frame.pack(padx = 5, pady = 5)
    
    while progressBar["value"] < 100:
        problem = MathGame.generate_problem(5)
        num = askinteger("Input", f"Input the Answer to {problem}")
        print(num)
        if num == MathGame.ans:
            progressBar.step(20)
        elif num == None:
            return 0
    
    label = ttk.Label(root, text = "Congratulations, you have passed level five!")
    label.pack(padx = 5, pady = 5)

# Generate Buttons
def generate_buttons():
   # Generate Buttons
    one = Button(top, text ="Start Level 1", command = problem_box_one)
    one.place(x=50,y=50)
    two = Button(top, text ="Start Level 2", command = problem_box_two)
    two.place(x=150,y=50)
    three = Button(top, text ="Start Level 3", command = problem_box_three)
    three.place(x=250,y=50)
    four = Button(top, text ="Start Level 4", command = problem_box_four)
    four.place(x=350,y=50)
    five = Button(top, text ="Start Level 5", command = problem_box_five)
    five.place(x=450,y=50) 

# generate the buttons to be used
generate_buttons()

top.mainloop()
