def play_time_attack(name="Player",level=1,timer=30):
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
    # Introduction Sequence
    def count_down():
        three = ttk.Label(root, text = "3")
        three.pack()

        #three.after(1000, three.pack_forget)

        two = ttk.Label(root, text = "2")
        two.pack_forget()
        two.after(1000, two.pack)

        one = ttk.Label(root, text = "1")
        one.pack_forget()
        one.after(2000, one.pack)

        GO = ttk.Label(root, text = "GO!!!")
        GO.after(3000, GO.pack)

    #countdown button
    countdown = Tk.Button(root, text ="Start Game",fg ='white', bg = 'red', command = count_down)
    countdown.place(x=50,y=45)

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
      #  user_ans = int(input(EquationQuest.generate_problem(level) + " = "))
        
        # increment the user's score if they get a problem right 
       # if(user_ans == EquationQuest.ans):
        #    total_correct += 1
        #print()
        
    #print("End!")
    #print(f"{name} got {total_correct} level {level} questions correct in {timer} seconds!")
    root.mainloop()
#play_time_attack()
