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
    
        self.recipesList=[["cake","filepath",[3,"hours"],[350,"F"],4,\
                                [["granny smith apples", 2, "ct"], ["golden raisins", 8, "oz"], ["brown sugar", 6, "oz"], ["dried figs", 4, "oz"], ["dried cherries", 2, "oz"], ["beef suet", 2, "oz"], ["crystallized ginger", 1, "oz"], ["brandy", 1/2, "cup"], ["orange, zested and jusiced", 1, "ct"], ["lemon, zested and juiced", 1, "ct"], ["nutmeg", 1/2, "teaspoon"], ["allspice", 1/4, "teaspoon"], ["cloves", 1/4, "teaspoon"]],\
                                "cook it!"], \
                        ["pie","FILEPATH",[3,"hours"],[350,"F"],4,\
                                [["pie ingredients", 2, "ct"]],\
                                "cook it!"], \
                        ["pudding","FILEPATH",[3,"hours"],[0,""],4,\
                                [["pudding ingredients", 2, "ct"]],\
                                "pudding it!"], \
                        ["turkey","FILEPATH",[3,"hours"],[300,"F"],4,\
                                [["turkey ingredients", 2, "ct"]],\
                                "cook it!"], \
                        ["sandwich","FILEPATH",[3,"hours"],[0,""],4,\
                                [["sandwich ingredients", 2, "ct"]],\
                                "cook it!"], \
                        ["stew","FILEPATH",[3,"hours"],[350,"F"],4,\
                                [["stew ingredients", 2, "ct"]],\
                                "cook it!"], \
                        ["soda","FILEPATH",[3,"hours"],[350,"F"],4,\
                                [["soda ingredients", 2, "ct"]],\
                                "cook it!"]]
        self.recipesList.sort()
        
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
                self.gui.setRecipesList(self.recipesList)
                self.gui.root.update()
                
                print("New recipe entry created at index: " + str(self.currentRecipeIndex[0]))
            
            
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
                    self.gui.errorMessage("Using current working directory for source directory")
                
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
                
                self.model.writeLaTeX("E:\\Dropbox\\Documents (current)\\eecs 448 (F'14)\\eecs448fp\\test\\", "test", self.recipesList)
                    
                    
            ###############
            # QUIT ACTION #
            ###############
            elif action=="quit":
                self.gui.root.destroy()
                break
    
controller = Controller()
controller.main()
