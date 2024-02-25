def menu():
    #import tkinter
    from tkinter.simpledialog import askinteger
    from tkinter import Tk
    import tkinter
    import tkinter.ttk as ttk
    import tkinter.font as font

    root = Tk()

    #fonts
    titleFont = font.Font(size=80)
    myFont = font.Font(family = "Comic Sans MS")
    buttonFonts = font.Font(size=30)

    #create window
    root.geometry("1520x800+1+1")
    root.title("Main Menu")

    #title
    welcometothe = tkinter.Label(root, text="Welcome to ", font = titleFont)
    welcometothe.pack()
    mathgame = tkinter.Label(root, text="Equation Quest!", font = titleFont)
    mathgame.pack()
    
    #functions
    def play_focus_mode():
        import focus_mode
        root.withdraw()
        focus_mode.focus_mode()
        

    def start_time_attack():
        import time_attack
        root.withdraw()
        time_attack.play_time_attack()

    def start_high_score():
        import high_score
        root.withdraw()
        high_score.play_high_score()


    #button
    focusmode = tkinter.Button(root, text ="Focus Mode",font = buttonFonts,fg = 'white', bg = 'blue',command = play_focus_mode)
    focusmode.place(x=300,y=300)

    timeattack = tkinter.Button(root, text = "Time Attack", font = buttonFonts, fg = 'white', bg = 'red', command = start_time_attack)
    timeattack.place(x= 600, y=300)

    highscore = tkinter.Button(root, text = "High Score", font = buttonFonts, fg = 'white', bg = 'green', command = start_high_score)
    highscore.place(x=900, y=300)

    root.mainloop()
menu()