#!/usr/bin/python
# Tkinter documentation:
# http://www.tutorialspoint.com/python/python_gui_programming.htm
# http://effbot.org/tkinterbook/


try: # python v2.X
    print("trying to load Tkinter")
    import Tkinter as TK
    from Tkinter import N, S, E, W, END	
    import tkMessageBox as messagebox
except ImportError: # python v3.X
    print("loading Tkinter failed, trying tkinter instead")
    import tkinter as TK
    from tkinter import N, S, E, W, END, LEFT, RIGHT
    from tkinter import messagebox



class popupWindow(object):
    def __init__(self, master, message):
        top = self.top = TK.Toplevel(master)
        self.l = TK.Label(top, text=message, anchor=W)
        self.l.pack()
        self.e = TK.Entry(top, width=75)
        self.e.pack()
        self.b = TK.Button(top, text='Ok', command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.value = self.e.get()
        self.top.destroy()


class GUI:
    # Get single string of user input via popup
    def getInfo(self, infoType):
        if infoType == "URL":
            message = "Please input the URL."
        if infoType == "dir":
            message = "Please input the directory."
            
        popup = popupWindow(self.root, message)
        self.root.wait_window(popup.top)
        return popup.value
    
    
    # Retrieve the most-recent action, reset most-recent action tracking
    def getRecentAction(self):
        temp = self.action
        self.action = None
        return temp
    
    
    # Read and return recipe name from input box
    def getRecipeName(self):
        name = self.recipeName.get()
        return name
    
    
    # Read ingredient name, quantity, unit, currently selected ingredient
    def getIngredientInfo(self):
        ingredient = [str(self.ingredientName.get()),\
                        float(self.ingredientQuantity.get()),\
                        str(self.ingredientUnit.get())]
        return ingredient
        
    
    # Read currently selected recipes and return as tupple
    def getSelectedRecipies(self):
        selection = self.recipeList.curselection()
        
        recipeSelection = []
        
        for item in range(0,len(selection)):
            recipeSelection.append(int(selection[item]))
            
        return recipeSelection
        
    
    # Read currently selected ingredient and return as 
    def getSelectedIngredient(self):
        selection = self.ingredientsList.curselection()
        if len(selection)==1:
            selection = [int(self.ingredientsList.curselection()[0])]
            print("Currently selected is ingredient #" + str(selection))
        else:
            selection=[]
        return selection
    
    
    # Read ingredient name, quantity, unit, currently selected ingredient
    def setIngredientInfo(self, ingredient):
        name = str(ingredient[0])
        quantity = str(ingredient[1])
        unit = str(ingredient[2])
        
        self.ingredientName.delete(0,END)
        self.ingredientName.insert(0, name)
        self.ingredientQuantity.delete(0,END)
        self.ingredientQuantity.insert(0, quantity)
        self.ingredientUnit.delete(0,END)
        self.ingredientUnit.insert(0, unit)
    
    
    # Set the displayed list of recipes
    def setRecipesList(self, recipesList):
        self.recipesList = recipesList
        self.recipeList.delete(0, END)
        for i in range(0,len(recipesList)):
            name = str(recipesList[i][0])
            self.recipeList.insert(END, name)
    
    
    # Set the displayed list of ingredients
    def setIngredientList(self, ingredientList):
        self.ingredientsList.delete(0, END)
        print(ingredientList)
        for ingredient in range(0,len(ingredientList)):
            self.ingredientsList.insert(END,str(ingredientList[ingredient][0]) + ", " + str(ingredientList[ingredient][1]) + " " + str(ingredientList[ingredient][2]))
        
    
    # Set the displayed individual recipe
    def setDisplayRecipe(self,recipe):
        # replace with "ingredients = recipe[xxx]"
        ingredients = ["ing 1", "ing 2", "ing 3"]
        ingredients = recipe[5]
        
        # replace with "name = recipe[yyy]"
        name = recipe[0]
        
        self.recipeName.delete(0,END)
        self.recipeName.insert(0,str(name))
        
        self.setIngredientList(ingredients)
    
    
    # Initialize the GUI
    def __init__(self):
        self.action=None
        
        # Tk root widget: window with titlebar, etc
        self.root = TK.Tk()
    
    
    # Display provided error message to user, print error message to console
    def errorMessage(self, message):
        print(str(message))
        try: 
            TK.messagebox.showinfo("Warning", str(message))
        except:
            messagebox.showinfo("Warning", str(message))
    
    
    # Set most-recent action, announce button press to console
    def buttonClicked(self, action):
        print("\nA button was pressed:")
        self.action = action
    
    
    # Place GUI items
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
        spacer.grid(row=0, column=2, sticky=N+S+E+W)
        label = TK.Label(spacer, text="     ")
        label.grid(row=0, column=0, sticky=N+S+E+W)
        # recipe frame
        recipeFrame = TK.Frame(self.root)
        recipeFrame.grid(row=0, column=4, sticky=N+S+E+W)
        # procedure frame
        procedureFrame = TK.Frame(self.root)
        procedureFrame.grid(row=1, column=0, columnspan=400, sticky=N+S+E+W)
        
        
        ################
        # MAIN BUTTONS #
        ################
        # spacer
        label = TK.Label(buttonsFrame)
        label.grid(row=0, column=0, sticky=N+S+E+W)
        # Load recipes
        self.buttonLoad = TK.Button(buttonsFrame, text="Load Recipes", command=lambda: self.buttonClicked("load"), anchor=W)
        self.buttonLoad.grid(row=1, column=0, sticky=N+S+E+W)
        # Add recipe
        self.buttonAdd = TK.Button(buttonsFrame, text="Add Recipe", command=lambda: self.buttonClicked("addR"), anchor=W)
        self.buttonAdd.grid(row=2, column=0, sticky=N+S+E+W)
        # Modify recipe
        self.buttonModify = TK.Button(buttonsFrame, text="Edit Recipe", command=lambda: self.buttonClicked("modR"), anchor=W)
        self.buttonModify.grid(row=3, column=0, sticky=N+S+E+W)
        # Remove recipe
        self.buttonRemove = TK.Button(buttonsFrame, text="Remove Recipe", command=lambda: self.buttonClicked("delR"), anchor=W)
        self.buttonRemove.grid(row=4, column=0, sticky=N+S+E+W)
        # Quit
        self.buttonQuit = TK.Button(buttonsFrame, text="Quit", command=lambda: self.buttonClicked("quit"), anchor=W)
        self.buttonQuit.grid(row=5, column=0, sticky=N+S+E+W)
        
        
        ################
        # RECIPES LIST #
        ################
        # Scrollbar setup
        scrollbar = TK.Scrollbar(recipesFrame)
        scrollbar.grid(row=1, column=11, rowspan=15, sticky=N+S)
        # Recipe List
        label = TK.Label(recipesFrame, text="Recipes:", anchor=W)
        label.grid(row=0, column=0,  sticky=N+S+E+W)
        self.recipeList = TK.Listbox(recipesFrame, selectmode=TK.EXTENDED)
        self.recipeList.grid(row=1, column=0, sticky=N+S+E+W, rowspan=15, columnspan=10)
        # Scrollbar config
        self.recipeList.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.recipeList.yview)
        
        
        ####################
        # RECIPE DISPLAYER #
        ####################
        # vertical spacer
        label = TK.Label(recipeFrame)
        label.grid(row=0, column=0, sticky=N+S+E+W)
        # Save Recipe button
        self.recipeAddIngredient = TK.Button(recipeFrame, text="Save Recipe", command=lambda: self.buttonClicked("savR"), anchor=W)
        self.recipeAddIngredient.grid(row=1, column=0, sticky=N+S+E+W)
        # Add Ingredient Button
        self.recipeAddIngredient = TK.Button(recipeFrame, text="Add Ingredient", command=lambda: self.buttonClicked("addI"), anchor=W)
        self.recipeAddIngredient.grid(row=3, column=0, sticky=N+S+E+W)
        # Edit Ingredient Button
        self.recipeEditIngredient = TK.Button(recipeFrame, text="Edit Ingredient", command=lambda: self.buttonClicked("modI"), anchor=W)
        self.recipeEditIngredient.grid(row=4, column=0, sticky=N+S+E+W)
        # Save Ingredient Button
        self.recipeAddIngredient = TK.Button(recipeFrame, text="Save Ingredient", command=lambda: self.buttonClicked("savI"), anchor=W)
        self.recipeAddIngredient.grid(row=5, column=0, sticky=N+S+E+W)        
        # Remove Ingredient Button
        self.recipeRemoveIngredient = TK.Button(recipeFrame, text="Remove Ingredient", command=lambda: self.buttonClicked("delI"), anchor=W)
        self.recipeRemoveIngredient.grid(row=6, column=0, sticky=N+S+E+W)
        
        # Recipe name box
        label = TK.Label(recipeFrame, text="Recipe Name:", anchor=W)
        label.grid(row=0, column=1, columnspan=2, sticky=N+S+E+W)
        self.recipeName = TK.Entry(recipeFrame)
        self.recipeName.insert(0, "")
        self.recipeName.grid(row=1, column=1, columnspan=2, rowspan=1, sticky=N+S+E+W)
        # Ingredient list scrollbar setup
        scrollbar = TK.Scrollbar(recipeFrame)
        scrollbar.grid(row=3, column=3, rowspan=100, sticky=N+S)
        # Ingredient list
        label = TK.Label(recipeFrame, text="Ingredients:", anchor=W)
        label.grid(row=2, column=1, columnspan=2, sticky=N+S+E+W)
        self.ingredientsList = TK.Listbox(recipeFrame, selectmode=TK.BROWSE)
        self.ingredientsList.grid(row=3, column=1, columnspan=2, rowspan=100, sticky=N+S+E+W)
        # Ingredient list scrollbar config
        self.ingredientsList.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.ingredientsList.yview)
                
        # Ingredient entry:
        label = TK.Label(recipeFrame)
        label.grid(row=0, column=4, rowspan=3, sticky=N+S+E+W)
        label = TK.Label(recipeFrame, text="Ingredient:", anchor=W)
        label.grid(row=3, column=4, sticky=N+S+E+W)
        self.ingredientName = TK.Entry(recipeFrame)
        self.ingredientName.grid(row=4, column=4, sticky=N+S+E+W)
        # Ingredient quantity
        label = TK.Label(recipeFrame, text="Quantity:", anchor=W)
        label.grid(row=5, column=4, sticky=N+S+E+W)
        self.ingredientQuantity = TK.Entry(recipeFrame)
        self.ingredientQuantity.grid(row=6, column=4, sticky=N+S+E+W)
        # Ingredient units
        label = TK.Label(recipeFrame, text="Unit:", anchor=W)
        label.grid(row=7, column=4, sticky=N+S+E+W)
        self.ingredientUnit = TK.Entry(recipeFrame)
        self.ingredientUnit.grid(row=8, column=4, sticky=N+S+E+W)
        
        ##################
        # PROCEDURE AREA #
        ##################
        # Scrollbar setup
        scrollbar = TK.Scrollbar(procedureFrame)
        scrollbar.grid(row=1, column=401, rowspan=301, sticky=N+S)
        # Procedure
        label = TK.Label(procedureFrame, text="Procedure:", anchor=W)
        label.grid(row=0, column=1, sticky=N+S+E+W)
        self.procedure = TK.Text(procedureFrame, yscrollcommand=scrollbar.set)
        self.procedure.grid(row=1, column=0, columnspan=400, rowspan=300, sticky=N+S+E+W)
        # Scrollbar config
        self.procedure.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.procedure.yview)
        
