def focus_mode():
    # import back end
    import EquationQuest

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

    #back button
    backtomenu = tkinter.Tk()
    backtomenu.geometry("100x100+1400+680")
    def back():
        top.withdraw()
        root.withdraw()
        backtomenu.withdraw()
        import MainMenu
        MainMenu.menu()

    backbutton = Tk.Button(backtomenu, text= "Back", command = back)
    backbutton.place(x=5,y=5)

    #making comicsans
    myFont = font.Font(family = "Comic Sans MS")

    #Create Progress bar and button GUI
    label = ttk.Label(root, text = "Progress")
    label.pack(padx = 5, pady = 5)
    root.geometry("275x770+1+1")
    top.geometry("930x250+590+1")

    #define problem box one
    def problem_box_one():
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)
        
        while progressBar["value"] < 100:
            problem = EquationQuest.generate_problem(1)
            num = askinteger("Input", f"Input the Answer to {problem}")
            
            if num == EquationQuest.ans:
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
            problem = EquationQuest.generate_problem(2)
            num = askinteger("Input", f"Input the Answer to {problem}")
            
            if num == EquationQuest.ans:
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
            problem = EquationQuest.generate_problem(3)
            num = askinteger("Input", f"Input the Answer to {problem}")
            
            if num == EquationQuest.ans:
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
            problem = EquationQuest.generate_problem(4)
            num = askinteger("Input", f"Input the Answer to {problem}")
            
            if num == EquationQuest.ans:
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
            problem = EquationQuest.generate_problem(5)
            num = askinteger("Input", f"Input the Answer to {problem}")
            
            if num == EquationQuest.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        
        label = ttk.Label(root, text = "Congratulations, you have passed level five!")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    #define problem box 6
    def problem_box_six():
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)
        
        while progressBar["value"] < 100:
            problem = EquationQuest.generate_problem(6)
            num = askinteger("Input", f"Input the Answer to {problem}")
            
            if num == EquationQuest.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        
        label = ttk.Label(root, text = "Congratulations, you have passed level six!")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    #define problem box 7
    def problem_box_seven():
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)
        
        while progressBar["value"] < 100:
            problem = EquationQuest.generate_problem(7)
            num = askinteger("Input", f"Input the Answer to {problem}")
            
            if num == EquationQuest.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        
        label = ttk.Label(root, text = "Congratulations, you have passed level seven!")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    #define problem box 8
    def problem_box_eight():
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)
        
        while progressBar["value"] < 100:
            problem = EquationQuest.generate_problem(8)
            num = askinteger("Input", f"Input the Answer to {problem}")
            
            if num == EquationQuest.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        
        label = ttk.Label(root, text = "Congratulations, you have passed level eight!")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    #define problem box 9
    def problem_box_nine():
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)
        
        while progressBar["value"] < 100:
            problem = EquationQuest.generate_problem(9)
            num = askinteger("Input", f"Input the Answer to {problem}")
            
            if num == EquationQuest.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        
        label = ttk.Label(root, text = "Congratulations, you have passed level nine!")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    #define problem box 10
    def problem_box_ten():
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)
        
        while progressBar["value"] < 100:
            problem = EquationQuest.generate_problem(10)
            num = askinteger("Input", f"Input the Answer to {problem}")
            
            if num == EquationQuest.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        
        label = ttk.Label(root, text = "Congratulations, you have passed level ten!")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    #define problem box 11
    def problem_box_eleven():
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)
        
        while progressBar["value"] < 100:
            problem = EquationQuest.generate_problem(11)
            num = askinteger("Input", f"Input the Answer to {problem}")
            
            if num == EquationQuest.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        
        label = ttk.Label(root, text = "Congratulations, you have passed level eleven!")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    #define problem box 12
    def problem_box_tweleve():
        progressBar= ttk.Progressbar(frame, mode='indeterminate')
        progressBar.pack(padx = 10, pady = 10)
        frame.pack(padx = 5, pady = 5)
        
        while progressBar["value"] < 100:
            problem = EquationQuest.generate_problem(12)
            num = askinteger("Input", f"Input the Answer to {problem}")
            
            if num == EquationQuest.ans:
                progressBar.step(20)
            elif num == None:
                return 0
        
        label = ttk.Label(root, text = "Congratulations, you have passed level tweleve!")
        label.pack(padx = 5, pady = 5)
        label.after(3000, label.destroy)

    # Generate Buttons
    def generate_buttons():
    # Generate Buttons
        one = Tk.Button(top, text ="Start Level 1 ",fg = 'white', bg = 'red', font=myFont ,command = problem_box_one)
        one.place(x=50,y=50)
        two = Tk.Button(top, text ="Start Level 2 ",fg = 'white', bg = '#ff7417',font=myFont, command = problem_box_two)
        two.place(x=200,y=50)
        three = Tk.Button(top, text ="Start Level 3 ",fg = 'white',bg = '#ffcc00',font=myFont, command = problem_box_three)
        three.place(x=350,y=50)
        four = Tk.Button(top, text ="Start Level 4 ",fg = 'white', bg = 'green',font=myFont ,command = problem_box_four)
        four.place(x=500,y=50)
        five = Tk.Button(top, text ="Start Level 5 ",fg = 'white', bg = 'blue',font=myFont ,command = problem_box_five)
        five.place(x=650,y=50) 
        six = Tk.Button(top, text ="Start Level 6 ",fg = 'white', bg = 'purple',font=myFont ,command = problem_box_six)
        six.place(x=800,y=50) 
        seven = Tk.Button(top, text ="Start Level 7 ",fg = 'white', bg = 'red', font=myFont ,command = problem_box_seven)
        seven.place(x=50,y=150)
        eight = Tk.Button(top, text ="Start Level 8 ",fg = 'white', bg = '#ff7417',font=myFont, command = problem_box_eight)
        eight.place(x=200,y=150)
        nine = Tk.Button(top, text ="Start Level 9 ",fg = 'white',bg = '#ffcc00',font=myFont, command = problem_box_nine)
        nine.place(x=350,y=150)
        ten = Tk.Button(top, text ="Start Level 10",fg = 'white', bg = 'green',font=myFont ,command = problem_box_ten)
        ten.place(x=500,y=150)
        eleven = Tk.Button(top, text ="Start Level 11",fg = 'white', bg = 'blue',font=myFont ,command = problem_box_eleven)
        eleven.place(x=650,y=150) 
        twelve = Tk.Button(top, text ="Start Level 12",fg = 'white', bg = 'purple',font=myFont ,command = problem_box_tweleve)
        twelve.place(x=800,y=150) 

    # generate the buttons to be used
    generate_buttons()

    top.mainloop()

#focus_mode()
