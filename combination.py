# import libraries
import random
import math

#tkinter/GUI libraries
from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter

ans = 0

#define
top = Tk()
root = tkinter.Tk()
frame= ttk.Frame(root)

#Create Progress bar and button GUI

root.geometry("275x150+1+200")
top.geometry("1520x100+1+1")

#def increment():
   #progressBar.step(20)


# list of valid operations
operations = ["+", "-", "*", "/", "^", "^-"]

# function to generate level 1 problems
def generate_level_1_problem(lower=0, upper=5):
    num1 = random.randint(lower, upper)
    num2 = random.randint(lower, upper)

    print(f"{num1} + {num2}")

    result = num1 + num2
    print(result)
    global ans
    ans = result

    return(f"{num1} + {num2}")


# function to generate level 2 problems
def generate_level_2_problem(lower=0, upper=5):
    num1 = random.randint(lower, upper)
    num2 = random.randint(lower, num1)

    print(f"{num1} - {num2}")

    result = num1 - num2
    print(result)
    global ans
    ans = result

    return(f"{num1} - {num2}")

# function to generate level 3 problems
def generate_level_3_problem():
    # determine operation
    operation = random.randint(0, 1)
    
    if(operation == 0): # Addition
        return generate_level_1_problem()
    else: # Subtraction
        return generate_level_2_problem()

# function to generate level 4 problems
def generate_level_4_problem():
    # determine operation
    operation = random.randint(0, 1)
    
    lower = 0
    upper = 20

    if(operation == 0): # Addition
        upper /= 2
        return generate_level_1_problem(lower=lower, upper=upper)
    else: # Subtraction
        return generate_level_2_problem(lower=lower, upper=upper)

# function to generate level 5 problems
def generate_level_5_problem():
    # determine operation
    operation = random.randint(0, 1)
    
    # bounds for operation
    lower = 0
    upper = 100

    if(operation == 0): # Addition
        upper /= 2
        return generate_level_1_problem(lower=lower, upper=upper)
    else: # Subtration
        return generate_level_2_problem(lower=lower, upper=upper)

# generate a problem with a specified level
def generate_problem(level):
    print(f"Level {level} problem:")
    
    # determine which level problem to generate
    match level:
        case 1:
            return generate_level_1_problem()
        case 2:
            return generate_level_2_problem()
        case 3:
            return generate_level_3_problem()
        case 4:
            return generate_level_4_problem()
        case 5:
            return generate_level_5_problem()
        case _:
            return ("ERROR: NO LEVEL 0 PROBLEMS")

#define problem box one
def problem_box_one():
    label = ttk.Label(root, text = "Progress")
    label.pack(padx = 5, pady = 5)
    progressBar= ttk.Progressbar(frame, mode='indeterminate')
    progressBar.pack(padx = 10, pady = 10)
    frame.pack(padx = 5, pady = 5)
    
    while progressBar["value"] < 100:
        problem = generate_problem(1)
        num = askinteger("Input", f"Input the Answer to {problem}")
        print(num)
        if num == ans:
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
        problem = generate_problem(2)
        num = askinteger("Input", f"Input the Answer to {problem}")
        print(num)
        if num == ans:
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
        problem = generate_problem(3)
        num = askinteger("Input", f"Input the Answer to {problem}")
        print(num)
        if num == ans:
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
        problem = generate_problem(4)
        num = askinteger("Input", f"Input the Answer to {problem}")
        print(num)
        if num == ans:
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
        problem = generate_problem(5)
        num = askinteger("Input", f"Input the Answer to {problem}")
        print(num)
        if num == ans:
            progressBar.step(20)
        elif num == None:
            return 0
        
    
    label = ttk.Label(root, text = "Congratulations, you have passed level five!")
    label.pack(padx = 5, pady = 5)

#Generate Button
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

top.mainloop()