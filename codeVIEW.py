#!/usr/bin/python
# Tkinter documentation:
# http://www.tutorialspoint.com/python/python_gui_programming.htm
# http://effbot.org/tkinterbook/


try:
    print("trying to load Tkinter")
    import Tkinter as TK
    from Tkinter import N, S, E, W, END
except ImportError:
    print("loading Tkinter failed, trying tkinter instead")
    import tkinter as TK
    from tkinter import N, S, E, W, END



class GUI:
    #import Tkinter # no underscore, uppercase 'T' for versions prior to V3.0
    #import tkinter # no underscore, lowercase 't' for V3.0 and later
    
    #from tkinter import N, S, E, W, END
    
    
    def __init__(self):
        print("Loading gui")
        
    def main(self):
        print("main method")
        # Tk root widget: window with titlebar, etc
        self.root = TK.Tk()
        
        # Tk buttons frame (left hand side)
        buttonsFrame = TK.Frame(self.root)
        buttonsFrame.grid(row=0, column=0, sticky=TK.N+TK.S+TK.E+TK.W)
        
        # Tk buttons:
        self.buttonLoad = TK.Button(buttonsFrame, text="Load Recipes", command=self.actionLoad)
        self.buttonAdd = TK.Button(buttonsFrame, text="Add Recipe", command=self.actionAdd)
        self.buttonModify = TK.Button(buttonsFrame, text="Modify Recipe", command=self.actionModify)
        self.buttonRemove = TK.Button(buttonsFrame, text="Remove Recipe", command=self.actionRemove)
        self.buttonQuit = TK.Button(buttonsFrame, text="Quit", command=self.actionQuit)
        # have to assign the layout via grid later because .grid doesn't return a type which messes up stuff like .insert()
        self.buttonLoad.grid(row=0, column=0, sticky=TK.N+TK.S+TK.E+TK.W)
        self.buttonAdd.grid(row=1, column=0, sticky=TK.N+TK.S+TK.E+TK.W)
        self.buttonModify.grid(row=2, column=0, sticky=TK.N+TK.S+TK.E+TK.W)
        self.buttonRemove.grid(row=3, column=0, sticky=TK.N+TK.S+TK.E+TK.W)
        self.buttonQuit.grid(row=4, column=0, sticky=TK.N+TK.S+TK.E+TK.W)
        
        # Tk recipe listbox (b/c of TK.EXTENDED, it supports selection of any combination of entries)
        self.recipeList = TK.Listbox(self.root, selectmode=TK.EXTENDED)
        # have to assign the layout via grid later because .grid doesn't return a type which messes up stuff like .insert()
        self.recipeList.grid(row=0, column=2, sticky=TK.N+TK.S+TK.E+TK.W, rowspan=10, columnspan=10)
        # populate listbox
        for option in range(0,5):
            self.recipeList.insert(TK.END, "option " + str(option))
        

        
        
        
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
        
        
