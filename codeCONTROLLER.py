from codeVIEW import GUI
from codeMODEL import Model

# The list of all recipes is stored as
#   recipesList = [["recipe name", 
#                      "filepath", 
#                       [bake time, "units"],
#                       [bake temp, "units"],
#                       servings,
#                       [["ingredient name", quantity, "units"],
#                           [...],  ...
#                         [...]],
#                       "procedure"],
#                   [...],
#                   [...]]
#
# By index, we have
#   recipesList[i][0] = "recipe name"
#   recipesList[i][1] = "filepath"
#   recipesList[i][2] = [bake time, "units"]
#   recipesList[i][3] = [bake temp, "units"]
#   recipesList[i][4] = servings
#   recipesList[i][5] = [["ingredient name", quantity, "units"],  [...],  ...,  [...]]
#   recipesList[i][6] = "procedure"
#
# recipesList.sort() will sort the recipes by name and should be performed whenever a recipe is added


class Controller:
    def __init__(self):
    
        self.model = Model()
    
        self.recipesList=[]
        
        self.currentIngredientList = []
        self.currentRecipeIndex = []
        self.currentRecipe = []
        self.currentIngredientIndex = []
        self.currentIngredientList = []

        self.gui = GUI()
        self.gui.buildGUI()
        
        self.gui.setRecipesList(self.recipesList)
        self.gui.setIngredientList(self.currentIngredientList)
        
        self.gui.root.update()

        
    def main(self):
        while True:
            self.gui.root.update()
            
            # get most recent buttonpress
            action = self.gui.getRecentAction()
            
            # print most recent action
            if action!=None:
                print(str(action))
                
            
            # decide what to do based on most recent action
            #########################
            # DELETE RECIPES ACTION #
            #########################
            if action=="delR":
                self.currentRecipeIndex = self.gui.getSelectedRecipies()
                print(self.currentRecipeIndex)
                
                if len(self.currentRecipeIndex)==0:
                    self.gui.errorMessage("No recipe was selected. Please try again.")
                else:
                    print("The following recipe indices were selected to be removed: " + str(self.currentRecipeIndex))
                
                    self.recipesList = self.model.removeRecipes(self.recipesList, self.currentRecipeIndex)
                    self.gui.setRecipesList(self.recipesList)
                    self.gui.root.update()
                    
                    self.currentRecipeIndex = []
            
            
            ############################
            # DELETE INGREDIENT ACTION #
            ############################
            elif action=="delI":
                self.currentIngredientIndex = self.gui.getSelectedIngredient()
                
                if len(self.currentIngredientIndex)==0:
                    self.gui.errorMessage("No ingredient was selected. Please try again.")
                else:
                    self.currentIngredientIndex = self.currentIngredientIndex[0]
                    print("The following ingredient index was selected to be removed: " + str(self.currentIngredientIndex))
                    self.currentIngredientList = self.model.removeIngredient(self.currentIngredientList, self.currentIngredientIndex)
                    self.gui.setIngredientList(self.currentIngredientList)
                    self.gui.root.update()
            
            
            ##########################
            # EDIT INGREDIENT ACTION #
            ##########################
            elif action=="modI":
                self.currentIngredientIndex = self.gui.getSelectedIngredient()
                print(self.currentIngredientIndex)
                self.currentIngredient = self.currentIngredientIndex
                
                if len(self.currentIngredientIndex)==0:
                    self.gui.errorMessage("No ingredient was selected. Please try again.")
                else:
                    print("The following ingredient index was selected to be modified: " + str(self.currentIngredientIndex[0]))
                    
                    self.gui.setIngredientInfo(self.currentIngredientList[self.currentIngredientIndex[0]])
                    self.gui.root.update()
            
            
            ##########################
            # SAVE INGREDIENT ACTION #
            ##########################
            elif action=="savI":
                print(str(self.currentIngredientIndex))
                if len(self.currentIngredientIndex)==0:
                    self.gui.errorMessage("No ingredient is active. Please try again.")
                else:
                    self.currentIngredientList[self.currentIngredientIndex[0]] = self.gui.getIngredientInfo()
                    
                    print("Updated ingredient: " + str(self.currentIngredientList[self.currentIngredientIndex[0]]))
                    
                    self.currentIngredientList.sort()
                    self.currentIngredientIndex = []
                    
                    self.gui.setIngredientInfo(["","",""])
                    self.gui.setIngredientList(self.currentIngredientList)
                    self.gui.root.update()
                    
            
            #########################
            # ADD INGREDIENT ACTION #
            #########################
            elif action=="addI":
                self.currentIngredientIndex = [len(self.currentIngredientList)]
                self.currentIngredientList.append(["???", 0, ""])
                
                self.gui.setIngredientList(self.currentIngredientList)
                self.gui.setIngredientInfo(self.currentIngredientList[self.currentIngredientIndex[0]])
                self.gui.root.update()
                
                self.currentIngredientList[self.currentIngredientIndex[0]] = self.gui.getIngredientInfo()
                
                print("Added ingredient")
            
            
            #######################
            # EDIT RECIPES ACTION #
            #######################
            elif action=="modR":
                self.currentRecipeIndex  = self.gui.getSelectedRecipies()
                if len(self.currentRecipeIndex)==1:
                    print("The following recipe index was selected to be edited: " + str(self.currentRecipeIndex[0]) + "  (" + str(self.recipesList[self.currentRecipeIndex[0]][0]) + ")")
                    
                    self.currentRecipe = self.recipesList[self.currentRecipeIndex[0]]
                    self.currentRecipeSelection = self.currentRecipeIndex[0] 
                    
                    self.currentIngredientList = self.currentRecipe[5]
                    
                    self.gui.setDisplayRecipe(self.currentRecipe)
                    self.gui.setProcedure(self.currentRecipe[6])
                    self.gui.setBaketime(self.currentRecipe[2])
                    self.gui.setBaketemp(self.currentRecipe[3])
                    
                elif len(self.currentRecipeIndex)==0:
                    self.gui.errorMessage("No recipe was selected. Please try again.")
                else:
                    self.gui.errorMessage("Too many recipes selected. Please try again.")
            
            
            #######################
            # SAVE RECIPES ACTION #
            #######################
            elif action=="savR":
                if len(self.currentRecipeIndex) == 0:
                    self.gui.errorMessage("No recipe is active. Please try again.")
                elif len(self.currentRecipeIndex) > 1:
                    self.gui.errorMessage("Too many active recipes. Please try again.")
                else:
                    print("Saving recipe")
                    
                    self.currentRecipe[0] = self.gui.getRecipeName()
                    self.currentRecipe[6] = self.gui.getProcedure()
                    self.currentRecipe[2] = self.gui.getBaketime()
                    self.currentRecipe[3] = self.gui.getBaketemp()
                    
                    self.recipesList[self.currentRecipeIndex[0]] = self.currentRecipe
                    self.recipesList.sort()
                    self.gui.setRecipesList(self.recipesList)
                    self.gui.setIngredientInfo([])
                    self.gui.setIngredientList([])
                    self.gui.setRecipeName("")
                    self.gui.setProcedure("")
                    self.gui.root.update()
                    self.gui.setBaketime([])
                    self.gui.setBaketemp([])
                    
                    print(self.recipesList[self.currentRecipeIndex[0]])
                    
                    self.currentIngredientList = []
                    self.currentRecipeIndex = []
                    self.currentRecipe = []
                    self.currentIngredientIndex = []
                    self.currentIngredientList = []
                    
                    
                    
            #####################
            # ADD RECIPE ACTION #
            #####################
            elif action=="addR":
                self.currentRecipeIndex = [len(self.recipesList)]
                
                self.recipesList.append(["???","",[0,""],[0,""],0,[["", 0, ""]],""])
                self.recipesList.sort()
                self.gui.setRecipesList(self.recipesList)
                self.gui.root.update()

                self.currentRecipeIndex = []
                
                print("New recipe entry created")
            
            
            ##################
            # FETCH FROM URL #
            ##################
            elif action=="URL":
                URL = self.gui.getInfo("URL")
                self.currentRecipeIndex = [len(self.recipesList)]
                
                recipe = self.model.urlLoad(URL)
                
                self.recipesList.append(recipe)
                self.gui.setRecipesList(self.recipesList)
                self.gui.root.update()
                
                print("New recipe added at index: " + str(self.currentRecipeIndex[0]))
                
                
            #######################
            # LOAD RECIPES ACTION #
            #######################
            elif action=="load":
                # Ask user for directory
                directory = self.gui.getInfo("source")
                if directory == "":
                    self.gui.errorMessage("Using current working directory for source directory")
                
                # Build recipe index
                self.recipesList = self.model.loadRecipes(directory)
                
                # Print result to console
                #print(self.recipesList)
                #print(directory)
                
                # Display recipe list
                self.gui.setRecipesList(self.recipesList)
                self.gui.root.update()
                
                
            #######################
            # SAVE RECIPES ACTION #
            #######################
            elif action=="save":
                # Ask user for directory
                directory = self.gui.getInfo("desDir")
                if directory == "":
                    self.gui.errorMessage("No directory provided.  Using current working directory for source directory")
                
                for recipe in self.recipesList:
                    directory = str(directory) + "/"
                    filename = recipe[0] + ".xml"
                    print("Writing to " + filename)
                    self.model.writeRecipe(directory, filename, recipe)
                    
                    
            ######################
            # COMPILE PDF ACTION #
            ######################
            elif action=="PDF":
                directory = self.gui.getInfo("desDir")
                filename = self.gui.getInfo("desFile")
                
                if directory == "":
                    self.gui.errorMessage("No directory provided.  Using current working directory for source directory")
                
                if filename == "":
                    self.gui.errorMessage("No filename provided.  Using \"output\" as filename.")
                    
                
                self.model.writeLaTeX(directory, filename, self.recipesList)
                    
                    
            ###############
            # QUIT ACTION #
            ###############
            elif action=="quit":
                self.gui.root.destroy()
                break
    
controller = Controller()
controller.main()
