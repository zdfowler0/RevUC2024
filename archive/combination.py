# import back end
import MathGame

#tkinter/GUI libraries
from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
import tkinter.font as font

#define things
top = Tk()
root = tkinter.Tk()
frame= ttk.Frame(root)

#making comicsans
myFont = font.Font(family = "Comic Sans MS")

#Create Progress bar and button GUI
label = ttk.Label(root, text = "Progress")
label.pack(padx = 5, pady = 5)
root.geometry("275x770+1+1")
top.geometry("920x250+600+1")

#define problem box one
def problem_box_one():
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
    label.after(3000, label.destroy)

#define problem box two
def problem_box_two():
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
    label.after(3000, label.destroy)

#define problem box 3
def problem_box_three():
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
    label.after(3000, label.destroy)

#define problem box 4
def problem_box_four():
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
    label.after(3000, label.destroy)

#define problem box 5
def problem_box_five():
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
    label.after(3000, label.destroy)

# Generate Buttons
def generate_buttons():
   # Generate Buttons
    one = Button(top, text ="Start Level 1",fg = 'white', bg = 'red', font=myFont ,command = problem_box_one)
    one.place(x=50,y=50)
    two = Button(top, text ="Start Level 2",fg = 'white', bg = '#ff7417',font=myFont, command = problem_box_two)
    two.place(x=200,y=50)
    three = Button(top, text ="Start Level 3",fg = 'white',bg = '#ffcc00',font=myFont, command = problem_box_three)
    three.place(x=350,y=50)
    four = Button(top, text ="Start Level 4",fg = 'white', bg = 'green',font=myFont ,command = problem_box_four)
    four.place(x=500,y=50)
    five = Button(top, text ="Start Level 5",fg = 'white', bg = 'blue',font=myFont ,command = problem_box_five)
    five.place(x=650,y=50) 

# generate the buttons to be used
generate_buttons()

top.mainloop()
