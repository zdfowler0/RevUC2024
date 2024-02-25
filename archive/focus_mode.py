'''
This is the code that creats the GUI and plays focus mode.
Focus mode is a learning environment where the user can 
practice as many questions they want by selecting the 
correct button. A progress bar will be made on the side for
each level that the user attempts. Each level wants them to
go five questions correct.
'''
def focus_mode():
    # import back end
    import MathGame

    #tkinter/GUI libraries
    from tkinter.simpledialog import askinteger
    import tkinter as Tk
    import tkinter
    import tkinter.ttk as ttk
    import tkinter.font as font

    #define things
    top = tkinter.Tk()
    root = tkinter.Tk()
    frame= ttk.Frame(root)

    #making comicsans
    myFont = font.Font(family = "Comic Sans MS")

    #Create Progress bar and button GUI
    label = ttk.Label(root, text = "Progress")
    label.pack(padx = 5, pady = 5)
    root.geometry("275x770+1+1")
    top.geometry("930x250+590+1")

    #define problem box one
    def problem_box_one():
        # progress bar for level
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)

        # ask questions and update progress bar
        while progressBar["value"] < 100:
            problem = MathGame.generate_problem(1)
            num = askinteger("Input", f"Input the Answer to {problem}")
            #print(num)
            #update progress bar
            if num == MathGame.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        # let user know they passed the level
        label = ttk.Label(root, text = "Congratulations, You have passed level one")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    #define problem box two
    def problem_box_two():
        # progress bar for level
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)

        # ask questions and update progress bar
        while progressBar["value"] < 100:
            problem = MathGame.generate_problem(2)
            num = askinteger("Input", f"Input the Answer to {problem}")
            print(num)
            if num == MathGame.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        # let user know they passed the level
        label = ttk.Label(root, text = "Congratulations, you have passed level two!")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    #define problem box 3
    def problem_box_three():
        # progress bar for level
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)

        # ask questions and update progress bar
        while progressBar["value"] < 100:
            problem = MathGame.generate_problem(3)
            num = askinteger("Input", f"Input the Answer to {problem}")
            print(num)
            if num == MathGame.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        # let user know they passed the level
        label = ttk.Label(root, text = "Congratulations, you have passed level three!")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    #define problem box 4
    def problem_box_four():
        # progress bar for level
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)

        # ask questions and update progress bar
        while progressBar["value"] < 100:
            problem = MathGame.generate_problem(4)
            num = askinteger("Input", f"Input the Answer to {problem}")
            print(num)
            if num == MathGame.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        # let user know they passed the level
        label = ttk.Label(root, text = "Congratulations, you have passed level four!")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    #define problem box 5
    def problem_box_five():
        # progress bar for level
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)

        # ask questions and update progress bar
        while progressBar["value"] < 100:
            problem = MathGame.generate_problem(5)
            num = askinteger("Input", f"Input the Answer to {problem}")
            print(num)
            if num == MathGame.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        # let user know they passed the level
        label = ttk.Label(root, text = "Congratulations, you have passed level five!")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    #define problem box 6
    def problem_box_six():
        # progress bar for level
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)

        # ask questions and update progress bar
        while progressBar["value"] < 100:
            problem = MathGame.generate_problem(6)
            num = askinteger("Input", f"Input the Answer to {problem}")
            print(num)
            if num == MathGame.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        # let user know they passed the level
        label = ttk.Label(root, text = "Congratulations, you have passed level six!")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    #define problem box 7
    def problem_box_seven():
        # progress bar for level
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)

        # ask questions and update progress bar
        while progressBar["value"] < 100:
            problem = MathGame.generate_problem(7)
            num = askinteger("Input", f"Input the Answer to {problem}")
            print(num)
            if num == MathGame.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        # let user know they passed the level
        label = ttk.Label(root, text = "Congratulations, you have passed level seven!")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    #define problem box 8
    def problem_box_eight():
        # progress bar for level
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)

        # ask questions and update progress bar
        while progressBar["value"] < 100:
            problem = MathGame.generate_problem(8)
            num = askinteger("Input", f"Input the Answer to {problem}")
            print(num)
            if num == MathGame.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        # let user know they passed the level
        label = ttk.Label(root, text = "Congratulations, you have passed level eight!")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    #define problem box 9
    def problem_box_nine():
        # progress bar for level
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)

        # ask questions and update progress bar
        while progressBar["value"] < 100:
            problem = MathGame.generate_problem(9)
            num = askinteger("Input", f"Input the Answer to {problem}")
            print(num)
            if num == MathGame.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        # let user know they passed the level
        label = ttk.Label(root, text = "Congratulations, you have passed level nine!")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    #define problem box 10
    def problem_box_ten():
        # progress bar for level
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)

        # ask questions and update progress bar
        while progressBar["value"] < 100:
            problem = MathGame.generate_problem(10)
            num = askinteger("Input", f"Input the Answer to {problem}")
            print(num)
            if num == MathGame.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        # let user know they passed the level
        label = ttk.Label(root, text = "Congratulations, you have passed level ten!")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    #define problem box 11
    def problem_box_eleven():
        # progress bar for level
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)

        # ask questions and update progress bar
        while progressBar["value"] < 100:
            problem = MathGame.generate_problem(11)
            num = askinteger("Input", f"Input the Answer to {problem}")
            print(num)
            if num == MathGame.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        # let user know they passed the level
        label = ttk.Label(root, text = "Congratulations, you have passed level eleven!")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    # define problem box 12
    def problem_box_tweleve():
        # progress bar for level
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)

        # ask questions and update progress bar
        while progressBar["value"] < 100:
            problem = MathGame.generate_problem(12)
            num = askinteger("Input", f"Input the Answer to {problem}")
            print(num)
            if num == MathGame.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        # let user know they passed the level
        label = ttk.Label(root, text = "Congratulations, you have passed level tweleve!")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    # This function generates all the buttons that correspond with each level
    def generate_buttons():
        # initialize buttons
        one = Tk.Button(top, text ="Start Level 1 ",fg = 'white', bg = 'red', font=myFont ,command = problem_box_one)
        two = Tk.Button(top, text ="Start Level 2 ",fg = 'white', bg = '#ff7417',font=myFont, command = problem_box_two)
        three = Tk.Button(top, text ="Start Level 3 ",fg = 'white',bg = '#ffcc00',font=myFont, command = problem_box_three)
        four = Tk.Button(top, text ="Start Level 4 ",fg = 'white', bg = 'green',font=myFont ,command = problem_box_four)
        five = Tk.Button(top, text ="Start Level 5 ",fg = 'white', bg = 'blue',font=myFont ,command = problem_box_five)
        six = Tk.Button(top, text ="Start Level 6 ",fg = 'white', bg = 'purple',font=myFont ,command = problem_box_six)
        seven = Tk.Button(top, text ="Start Level 7 ",fg = 'white', bg = 'red', font=myFont ,command = problem_box_seven)
        eight = Tk.Button(top, text ="Start Level 8 ",fg = 'white', bg = '#ff7417',font=myFont, command = problem_box_eight)
        nine = Tk.Button(top, text ="Start Level 9 ",fg = 'white',bg = '#ffcc00',font=myFont, command = problem_box_nine)
        ten = Tk.Button(top, text ="Start Level 10",fg = 'white', bg = 'green',font=myFont ,command = problem_box_ten)
        eleven = Tk.Button(top, text ="Start Level 11",fg = 'white', bg = 'blue',font=myFont ,command = problem_box_eleven)
        twelve = Tk.Button(top, text ="Start Level 12",fg = 'white', bg = 'purple',font=myFont ,command = problem_box_tweleve)
        
        # Aligns buttons in a 6x2 grid
        # first row of 6
        one.place(x=50,y=50)
        two.place(x=200,y=50)
        three.place(x=350,y=50)
        four.place(x=500,y=50)
        five.place(x=650,y=50)
        six.place(x=800,y=50)
        
        # second row of 6
        seven.place(x=50,y=150)
        eight.place(x=200,y=150)
        nine.place(x=350,y=150)
        ten.place(x=500,y=150)
        eleven.place(x=650,y=150)
        twelve.place(x=800,y=150)
        
    # generate the buttons to be used
    generate_buttons()

    # run main loop of focus mode
    top.mainloop()

#focus_mode()
