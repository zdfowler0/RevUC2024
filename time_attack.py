def play_time_attack(name="Player",level=1,timer=30):
    import time
    import EquationQuest
    from tkinter.simpledialog import askinteger
    import tkinter as Tk
    import tkinter
    import tkinter.ttk as ttk
    import tkinter.font as font

    root = tkinter.Tk()
    numbercorrect = tkinter.Tk()


    #number correct
    numbercorrect.geometry("100x100+1400+1")
    #timer 

    #window
    root.geometry("300x105+1+1")
    root.title("Time Attack")
    instructions = ttk.Label(root, text="Answer as many quesitons as you can in 30 seconds")
    instructions.pack()


    #scoredisplay
    labelscore = Tk.Label(numbercorrect, text = "Score: ")
    labelscore.place(x=5, y=5)
    score = 0
    scoredisplay = Tk.Label(numbercorrect, text = f"{score}")
    scoredisplay.place(x=50,y=5)

    #timeer
    labeltimer =Tk.Label(numbercorrect, text = "Time left: ")
    labeltimer.place(x=5,y=50)
    timershow = 0 
    timerdisplay =Tk.Label(numbercorrect, text = f"{timershow}")
    timerdisplay.place(x=60, y= 50)

    def wait():
        score = 0
        start = time.time()
        timershow = int(abs(time.time() - start - 30))

        while(timer > time.time() - start):
            timershow = int(abs(time.time() - start - 30))
            timerdisplay =Tk.Label(numbercorrect, text = f"{timershow}")
            timerdisplay.place(x=60, y= 50)
            problem = EquationQuest.generate_problem(1)
            num = askinteger("Input", f"Input the Answer to {problem}")
            if num == EquationQuest.ans:
                    #scoredisplay
                    score += 1
                    scoredisplay = Tk.Label(numbercorrect, text = f"{score}")
                    scoredisplay.place(x=50,y=5)
            elif num == None:
                    return 0
    
       
        
    #start button
    start = Tk.Button(root, text ="GO",fg ='white', bg = 'red', command = wait)
    start.place(x=50,y=45)

    #back button
    backtomenu = tkinter.Tk()
    backtomenu.geometry("100x100+1400+680")
    def back():
        numbercorrect.withdraw()
        root.withdraw()
        backtomenu.withdraw()
        import MainMenu
        MainMenu.menu()

    backbutton = Tk.Button(backtomenu, text= "Back", command = back)
    backbutton.place(x=5,y=5)
    
    
    root.mainloop()
play_time_attack()
