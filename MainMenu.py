#import python files
import focus_mode

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
 
#function
def play_focus_mode():
    focus_mode.focus_mode()


#button
focusmode = Button(root, text ="Focus Mode",font = buttonFonts,fg = 'white', bg = 'red',command = play_focus_mode)
focusmode.place(x=500,y=300)


root.mainloop()