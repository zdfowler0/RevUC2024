def play_high_score(name="Player"):
    import random
    import EquationQuest

    from tkinter.simpledialog import askinteger
    import tkinter as Tk
    import tkinter
    import tkinter.ttk as ttk
    import tkinter.font as font

    
    #open gui
    highscorewindow = tkinter.Tk()
    highscorewindow.geometry("250x150+1+1")
    scorewindow = tkinter.Tk()
    scorewindow. geometry("100x100+1400+1")

    #create fonts
    instructionfont = font.Font(size=20)
    scorefont = font.Font(size = 20)

    #display instructions
    title = Tk.Label(highscorewindow, text = "Mode: High Score", font = instructionfont)
    title.place(x=5,y=5)
    instructions = Tk.Label(highscorewindow, text = "Play until you lose!", font = instructionfont)
    instructions.place(x=5, y=50)

    #define score
    score = 0

    #display score
    scoredisplay = Tk.Label(scorewindow, text = f"{score}")
    scoredisplay.place(x=50,y=30)

    
    def play_game():
        score = 0
        #display score
        scoredisplay = Tk.Label(scorewindow, text = f"{score}")
        scoredisplay.place(x=50,y=30)
        
        while(True):
            # generate question level
            level = random.randint(1, 12)

            # chance for a 1.5x bonus
            bonus15 = random.randint(1, 100)

            # chance for a 2x bonus
            bonus2 = random.randint(1, 100)
            
            # calculate total bonus
            if(bonus15 < 15):
                bonus15 = 1.5
            else:
                bonus15 = 1

            if(bonus2 < 5):
                bonus2 = 2
            else:
                bonus2 = 1
            total_bonus = bonus15 * bonus2

            problem = EquationQuest.generate_problem(level)

            if(total_bonus > 1):
                num = askinteger("Input", f"Input the Answer to {problem} ({total_bonus} bonus)")
                if num == EquationQuest.ans:
                    score += int(level * 100 * total_bonus)
                    #display score
                    scoredisplay = Tk.Label(scorewindow, text = f"{score}")
                    scoredisplay.place(x=50,y=30)
                elif num == None:
                    return 0
            else:
                num = askinteger("Input", f"Input the Answer to {problem}")
                if num == EquationQuest.ans:
                    score += int(level * 100 * total_bonus)
                    #display score
                    scoredisplay = Tk.Label(scorewindow, text = f"{score}")
                    scoredisplay.place(x=50,y=30)
                elif num == None:
                    return 0

    #create start button
    startbutton = Tk.Button(highscorewindow, text = "Start Game", fg = 'white', bg = 'green',command = play_game)
    startbutton.place(x=90, y=100)

    #back button
    backtomenu = tkinter.Tk()
    backtomenu.geometry("100x100+1400+680")
    def back():
        scorewindow.withdraw()
        highscorewindow.withdraw()
        backtomenu.withdraw()
        import MainMenu
        MainMenu.menu()
    
    backbutton = Tk.Button(backtomenu, text= "Back", command = back)
    backbutton.place(x=5,y=5)

    #print(f"{name} got {score} points!")
#play_high_score()
