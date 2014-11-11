#!/usr/bin/python
# Tkinter documentation:
# http://www.tutorialspoint.com/python/python_gui_programming.htm
from Tkinter import *
import tkMessageBox
import Tkinter

window_height = 500
window_width = 500
button_buffer = 10
button_height = 30
button_width = 100

root = Tkinter.Tk()
fButtons = Frame(root, width=window_width, height=window_height)
fButtons.pack()
# Code to add widgets goes here:


# Button: Add recipe
def cAddRecipe():
    tkMessageBox.showinfo("title","message")
bAddRecipe = Tkinter.Button(fButtons, text="Add Recipe", command = cAddRecipe)   
button_x = button_buffer
button_y = 0 + button_buffer + 0*button_height
bAddRecipe.place(bordermode=OUTSIDE, height=button_height, width=button_width, x=button_x, y=button_y)



# Button: Fetch recipe from *.com
def cFetchRecipe():
    tkMessageBox.showinfo("Fetch Recipe","message")
bFetchRecipe = Tkinter.Button(fButtons, text="Fetch Recipe", command = cFetchRecipe)
button_x = button_buffer
button_y = 0 + button_buffer + 1*(button_height + button_buffer)
bFetchRecipe.place(bordermode=OUTSIDE, height=button_height, width=button_width, x=button_x, y=button_y)



# Button: Quit
def cQuit():
    quit()
bQuit = Tkinter.Button(fButtons, text="Quit", command = cQuit)
button_x = button_buffer
button_y = window_height - button_buffer - button_height
bQuit.place(bordermode=OUTSIDE, height=button_height, width=button_width, x=button_x, y=button_y)




root.mainloop()
