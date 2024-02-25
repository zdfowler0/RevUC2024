#import python files
import focus_mode
import time_attack
import high_score

#import tkinter
from tkinter.simpledialog import askinteger
from tkinter import *
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
welcometothe = Label(root, text="Welcome to the ", font = titleFont)
welcometothe.pack()
mathgame = Label(root, text="Math Game!", font = titleFont)
mathgame.pack()
 
#functions
def play_focus_mode():
    focus_mode.focus_mode()
def play_time_attack():
    time_attack
def play_high_score():
    high_score


#button
focusmode = Button(root, text ="Focus Mode",font = buttonFonts,fg = 'white', bg = 'blue',command = play_focus_mode)
focusmode.place(x=300,y=300)

timeattack = Button(root, text = "Time Attack", font = buttonFonts, fg = 'white', bg = 'red', command = play_time_attack)
timeattack.place(x= 600, y=300)

highscore = Button(root, text = "High Score", font = buttonFonts, fg = 'white', bg = 'green', command = play_high_score)
highscore.place(x=900, y=300)

root.mainloop()