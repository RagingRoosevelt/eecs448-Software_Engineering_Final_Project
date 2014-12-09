#!/usr/bin/python
# Tkinter documentation:
# http://www.tutorialspoint.com/python/python_gui_programming.htm

class GUI:
    def __init__(self):
        #from Tkinter import *
        #import tkMessageBox
        import tkinter as TK # v3.0 and above
        from tkinter import W
        #import Tkinter as TK # v2.9 and below
        
        self.window_height = 500
        self.window_width = 500
        self.button_buffer = 10
        self.button_height = 30
        self.button_width = 100
        
        # Tk root widget: window with titlebar, etc
        self.root = TK.Tk()
        
        # Tk buttons frame (left hand side)
        buttonsFrame = TK.Frame(self.root)
        #buttonsFrame.grid(row=4, column=0, columnspan=1)
        buttonsFrame.pack()
        
        # Tk buttons:
        self.buttonLoad = TK.Button(buttonsFrame, text="Load Recipes", command=self.actionLoad).grid(row=0, column=0, sticky=W)
        self.buttonAdd = TK.Button(buttonsFrame, text="Add Recipe", command=self.actionAdd).grid(row=1, column=0, sticky=W)
        self.buttonModify = TK.Button(buttonsFrame, text="Modify Recipe", command=self.actionModify).grid(row=2, column=0, sticky=W)
        self.buttonRemove = TK.Button(buttonsFrame, text="Remove Recipe", command=self.actionRemove).grid(row=3, column=0, sticky=W)
        self.buttonQuit = TK.Button(buttonsFrame, text="Quit", command=self.actionQuit).grid(row=4, column=0, sticky=W)
        

        
        
        
        self.root.mainloop()
        
    def actionLoad(self):
        print("\"Load Recipes\" pressed")
    def actionAdd(self):
        print("\"Add Recipe\" pressed")
    def actionRemove(self):
        print("\"Remove Recipe\" pressed")
    def actionModify(self):
        print("\"Modify Recipe\" pressed")
    def actionQuit(self):
        self.root.destroy()
        
        
gui = GUI()