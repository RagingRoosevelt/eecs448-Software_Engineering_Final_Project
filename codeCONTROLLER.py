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
#   recipesList[i][2] = [bake temp, "units"]
#   recipesList[i][3] = servings
#   recipesList[i][4] = [["ingredient name", quantity, "units"],  [...],  ...,  [...]]
#   recipesList[i][5] = "procedure"
#
# recipesList.sort() will sort the recipes by name and should be performed whenever a recipe is added


class Controller:
    def __init__(self):
        self.model = Model()
    
        self.recipesList=[["cake","..."], ["pie","..."], ["pudding","..."], ["turkey","..."], ["sandwich","..."], ["stew","..."], ["soda","..."], ["chilli","..."], ["salad","..."], ["pizza","..."], ["curry","..."], ["pasta","..."], ["danish","..."]]
        self.recipesList.sort()
        
        self.ingredientList = [["granny smith apples", 2, "ct"], ["golden raisins", 8, "oz"], ["brown sugar", 6, "oz"], ["dried figs", 4, "oz"], ["dried cherries", 2, "oz"], ["beef suet", 2, "oz"], ["crystallized ginger", 1, "oz"], ["brandy", 1/2, "cup"], ["orange, zested and jusiced", 1, "ct"], ["lemon, zested and juiced", 1, "ct"], ["nutmeg", 1/2, "teaspoon"], ["allspice", 1/4, "teaspoon"], ["clove", 1/4, "teaspoon"]]

        self.gui = GUI()
        self.gui.buildGUI()
        
        self.gui.setRecipesList(self.recipesList)
        self.gui.setIngredientList(self.ingredientList)
        
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
            if action=="del":
                selection = self.gui.getSelectedRecipies()
                
                if len(selection)==0:
                    self.gui.errorMessage("No recipe was selected. Please try again.")
                else:
                    print("The following recipe indices were selected to be removed: " + str(selection))
                
                    self.recipesList = self.model.removeRecipes(self.recipesList, selection)
                    self.gui.setRecipesList(self.recipesList)
                    self.gui.root.update()
                    
                    print(self.recipesList)
                
            ############################
            # DELETE INGREDIENT ACTION #
            ############################
            elif action=="delI":
                selection = self.gui.getSelectedIngredient()
                
                if len(selection)==0:
                    self.gui.errorMessage("No ingredient was selected. Please try again.")
                else:
                    selection = selection[0]
                    print("The following ingredient index was selected to be removed: " + str(selection))
                    self.ingredientList = self.model.removeIngredient(self.ingredientList, selection)
                    self.gui.setIngredientList(self.ingredientList)
                    self.gui.root.update()
                
            ##########################
            # EDIT INGREDIENT ACTION #
            ##########################
            elif action=="modI":
                selection = self.gui.getSelectedIngredient()
                
                if len(selection)==0:
                    self.gui.errorMessage("No ingredient was selected. Please try again.")
                else:
                    selection = selection[0]
                    print("The following ingredient index was selected to be modified: " + str(selection))
                    
                    self.gui.setIngredientInfo(self.ingredientList[selection])
                    self.gui.root.update()
            
            
            #######################
            # EDIT RECIPES ACTION #
            #######################
            elif action=="mod":
                selection = self.gui.getSelectedRecipies()
                if len(selection)==1:
                    selection = int(selection[0])
                    print("The following recipe index was selected to be edited: " + str(selection) + "  (" + str(self.recipesList[selection][0]) + ")")
                elif len(selection)==0:
                    self.gui.errorMessage("No recipe was selected. Please try again.")
                else:
                    self.gui.errorMessage("Too many recipes selected. Please try again.")
                    
                    
            #####################
            # ADD RECIPE ACTION #
            #####################
            elif action=="add":
                index = 123123
                print("New recipe entry created at index: " + str(index))
                
                
            #######################
            # LOAD RECIPES ACTION #
            #######################
            elif action=="load":
                # Ask user for directory
                directory = self.gui.getInfo("dir")
                
                # Build recipe index
                self.recipesList = self.model.loadRecipes(directory)
                
                # Print result to console
                print(self.recipesList)
                print(directory)
                
                # Display recipe list
                self.gui.setRecipesList(self.recipesList)
                self.gui.root.update()
                    
                    
            ###############
            # QUIT ACTION #
            ###############
            elif action=="quit":
                self.gui.root.destroy()
                break
    
controller = Controller()
controller.main()
