def play_time_attack(name="Player",level=1,timer=30):
    import time
    import MathGame
    from tkinter.simpledialog import askinteger
    import tkinter as Tk
    import tkinter
    import tkinter.ttk as ttk
    import tkinter.font as font

    root = tkinter.Tk()
    numbercorrect = tkinter.Tk()

    #number correct
    numbercorrect.geometry("100x100+1400+1")
    #window
    root.geometry("300x105+1+1")
    root.title("Time Attack")
    instructions = ttk.Label(root, text="Answer as many quesitons as you can in 30 seconds")
    instructions.pack()


    #scoredisplay
    score = 0
    scoredisplay = Tk.Label(numbercorrect, text = f"{score}")
    scoredisplay.place(x=5,y=5)

    def wait():
        score = 0
        start = time.time()

        while(timer > time.time() - start):
            problem = MathGame.generate_problem(1)
            num = askinteger("Input", f"Input the Answer to {problem}")
            if num == MathGame.ans:
                    #scoredisplay
                    score += 1
                    scoredisplay = Tk.Label(numbercorrect, text = f"{score}")
                    scoredisplay.place(x=5,y=5)
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
    
    

    

    # set the start of the timer
    #start = time.time()

    #total_correct = 0

    # timer
    #while(timer > time.time() - start):
        # let the user know how much time is left
     #   print("Time left: {0}".format(int(abs((time.time() - start) - timer))))

        # get user input and generate question
      #  user_ans = int(input(MathGame.generate_problem(level) + " = "))
        
        # increment the user's score if they get a problem right 
       # if(user_ans == MathGame.ans):
        #    total_correct += 1
        #print()
        
    #print("End!")
    #print(f"{name} got {total_correct} level {level} questions correct in {timer} seconds!")
    root.mainloop()
play_time_attack()