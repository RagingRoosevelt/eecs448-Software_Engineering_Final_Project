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
    from tkinter import N, S, E, W, END, LEFT, RIGHT



class GUI:
    def buttonClicked(self, action):
        print("Button Pressed!")
        self.action = action
    
    
    def setRecipes(self, recipes):
        for recipe in recipes:
            self.recipeList.insert(TK.END, str(recipe))
            
    def setDisplayRecipe(self,recipe):
        # replace with "ingredients = recipe[xxx]"
        ingredients = ["ing 1", "ing 2", "ing 3"]
        
        # replace with "name = recipe[yyy]"
        name = "recipe name"
        
        self.recipeName.set(str(name))
        for ingredient in ingredients:
            self.ingredients.insert(TK.END, str(ingredient))
        
    def getRecentAction(self):
        temp = self.action
        self.action = None
        return temp
        
    def readRecipeName(self):
        name = self.recipeName._entry_value.get()
        return name
        
    #def read
    
    
    def __init__(self):
        self.action=None
        
        # Tk root widget: window with titlebar, etc
        self.root = TK.Tk()
        
    
    def buildGUI(self):
        print("main method")
        
        ###############
        # MAIN FRAMES #
        ###############
        # buttons frame (left hand side)
        buttonsFrame = TK.Frame(self.root)
        buttonsFrame.grid(row=0, column=0, sticky=N+S+E+W)
        # recipe list frame
        recipesFrame = TK.Frame(self.root)
        recipesFrame.grid(row=0, column=1, sticky=N+S+E+W)
        # spacer frame
        spacer = TK.Frame(self.root)
        spacer.grid(row=0, column=2, columnspan=2, sticky=N+S+E+W)
        # recipe frame
        recipeFrame = TK.Frame(self.root)
        recipeFrame.grid(row=0, column=4, sticky=N+S+E+W)
        # procedure frame
        procedureFrame = TK.Frame(self.root)
        procedureFrame.grid(row=1, column=0, columnspan=400, sticky=N+S+E+W)
        
        
        ################
        # MAIN BUTTONS #
        ################
        # Load recipes
        self.buttonLoad = TK.Button(buttonsFrame, text="Load Recipes", command=lambda: self.buttonClicked("load"))
        self.buttonLoad.grid(row=0, column=0, sticky=N+S+E+W)
        # Add recipe
        self.buttonAdd = TK.Button(buttonsFrame, text="Add Recipe", command=lambda: self.buttonClicked("add"))
        self.buttonAdd.grid(row=1, column=0, sticky=N+S+E+W)
        # Modify recipe
        self.buttonModify = TK.Button(buttonsFrame, text="Save Recipe", command=lambda: self.buttonClicked("sav"))
        self.buttonModify.grid(row=2, column=0, sticky=N+S+E+W)
        # Remove recipe
        self.buttonRemove = TK.Button(buttonsFrame, text="Remove Recipe", command=lambda: self.buttonClicked("del"))
        self.buttonRemove.grid(row=3, column=0, sticky=N+S+E+W)
        # Quit
        self.buttonQuit = TK.Button(buttonsFrame, text="Quit", command=lambda: self.buttonClicked("quit"))
        self.buttonQuit.grid(row=4, column=0, sticky=N+S+E+W)
        
        
        ################
        # RECIPE FRAME #
        ################
        # Recipe List
        self.recipeList = TK.Listbox(recipesFrame, selectmode=TK.EXTENDED)
        self.recipeList.grid(row=0, column=0, sticky=N+S+E+W, rowspan=10, columnspan=10)
        
        
        ####################
        # RECIPE DISPLAYER #
        ####################
        # Add Ingredient Button
        self.recipeAddIngredient = TK.Button(recipeFrame, text="Add Ingredient", command=lambda: self.buttonClicked("addI"))
        self.recipeAddIngredient.grid(row=0, column=0, sticky=N+S+E+W)
        # Save Ingredient Button
        self.recipeAddIngredient = TK.Button(recipeFrame, text="Save Ingredient", command=lambda: self.buttonClicked("savI"))
        self.recipeAddIngredient.grid(row=1, column=0, sticky=N+S+E+W)        
        # Remove Ingredient Button
        self.recipeRemoveIngredient = TK.Button(recipeFrame, text="Remove Ingredient", command=lambda: self.buttonClicked("delI"))
        self.recipeRemoveIngredient.grid(row=2, column=0, sticky=N+S+E+W)
        
        # Recipe name box
        label = TK.Label(recipeFrame, text="Recipe Name:", anchor=W)
        label.grid(row=0, column=1, sticky=N+S+E+W)
        self.recipeName = TK.Entry(recipeFrame)
        self.recipeName.insert(0, "test")
        self.recipeName.grid(row=1, column=1, rowspan=1, sticky=N+S+E+W)
        # Ingredient list
        label = TK.Label(recipeFrame, text="Ingredients:", anchor=W)
        label.grid(row=2, column=1, sticky=N+S+E+W)
        self.ingredients = TK.Listbox(recipeFrame, selectmode=TK.BROWSE)
        self.ingredients.grid(row=3, column=1, rowspan=100, sticky=N+S+E+W)
                
        # Ingredient entry:
        label = TK.Label(recipeFrame)
        label.grid(row=0, column=2, rowspan=3, sticky=N+S+E+W)
        label = TK.Label(recipeFrame, text="Ingredient:")
        label.grid(row=3, column=2, sticky=N+S+E+W)
        self.ingredientName = TK.Entry(recipeFrame)
        self.ingredientName.grid(row=4, column=2, sticky=N+S+E+W)
        # Ingredient quantity
        label = TK.Label(recipeFrame, text="Quantity:")
        label.grid(row=5, column=2, sticky=N+S+E+W)
        self.ingredientQuantity = TK.Entry(recipeFrame)
        self.ingredientQuantity.grid(row=6, column=2, sticky=N+S+E+W)
        # Ingredient units
        label = TK.Label(recipeFrame, text="Unit:")
        label.grid(row=7, column=2, sticky=N+S+E+W)
        self.ingredientUnit = TK.Entry(recipeFrame)
        self.ingredientUnit.grid(row=8, column=2, sticky=N+S+E+W)
        
        ##################
        # PROCEDURE AREA #
        ##################
        scrollbar = TK.Scrollbar(procedureFrame)
        scrollbar.grid(row=1, column=401, rowspan=301, sticky=N+S)
        label = TK.Label(procedureFrame, text="Procedure:", anchor=W)
        label.grid(row=0, column=1, sticky=N+S+E+W)
        self.procedure = TK.Text(procedureFrame, yscrollcommand=scrollbar.set)
        self.procedure.grid(row=1, column=0, columnspan=400, rowspan=300, sticky=N+S+E+W)
        
        self.procedure.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.procedure.yview)
        