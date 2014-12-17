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

        self.gui = GUI()
        self.gui.buildGUI()
        self.gui.setRecipesList(self.recipesList)

        
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
                print(selection)
                recipeSelection = []
                for item in range(0,len(selection)):
                    recipeSelection.append(int(selection[item]))
                if len(recipeSelection)==0:
                    self.gui.errorMessage("No recipe was selected. Please try again.")
                else:
                    print("The following recipe indices were selected to be removed: " + str(recipeSelection))
                
                self.model.removeRecipes(self.recipesList, recipeSelection)
                self.gui.setRecipesList(self.recipesList)
                self.gui.root.update()
                
                print(self.recipesList)
            
            
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
