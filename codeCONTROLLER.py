from codeVIEW import GUI

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
        recipesList=["cake", "pie", "pudding", "turkey", "sandwich", "stew", "soda", "chilli", "salad", "pizza", "curry", "pasta", "danish"]
        recipesList.sort()

        self.gui = GUI()
        self.gui.buildGUI()
        self.gui.setRecipesList(recipesList)

        
    def main(self):
        while True:
            self.gui.root.update()
            
            # get most recent buttonpress
            action = self.gui.getRecentAction()
            
            # print most recent action
            if action!=None:
                print(action)
                
            # decide what to do based on most recent action
            if action=="del":
                selection = self.gui.getSelectedRecipies()
                if len(selection)==0:
                    print("No recipe was selected")
                    # tell GUI to display corresponding error message
                    # self.gui.errorMessage("No recipe was selected")
                else:
                    print("The following recipe indices were selected to be removed: " + str(selection))
                    # delete recipes with indices in "selection"
                
            elif action=="mod":
                selection = self.gui.getSelectedRecipies()
                if len(selection)==1:
                    selection = selection[0]
                    print("The following recipe index was selected to be edited: " + str(selection))
                elif len(selection)==0:
                    print("No recipe was selected")
                    # tell GUI to display corresponding error message
                    # self.gui.errorMessage("No recipe was selected")
                else:
                    print("Too many recipes selected")
                    # tell GUI to display corresponding error message
                    # self.gui.errorMessage("Too many recipes selected")
                    
            elif action=="add":
                index = 123123
                print("New recipe entry created at index: " + str(index))
                    
            
            elif action=="quit":
                self.gui.root.destroy()
                break
    
controller = Controller()
controller.main()