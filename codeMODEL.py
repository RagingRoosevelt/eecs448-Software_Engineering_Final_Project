## You can use these commands to test these functions:
##    loadRecipes()
##    tree = getXML('TestRecipe.xml')
##    recipe = readRecipe(tree)
##    writeRecipe(filename, recipe)

import os, sys
from xml.etree import ElementTree as ET

class Model:
    # Removes user-selected ingredient from list
    # Returns the resulting ingredient list
    def removeIngredient(self, incredientList, ingredientSelection):
        print("Removed ingredient #" + str(ingredientSelection) + " (" + incredientList[ingredientSelection][0] + ")")
        del incredientList[ingredientSelection]
        return incredientList

    
    # Removes user-selected recipes from the list
    # Returns the resulting recipes list
    def removeRecipes(self, recipesList, recipeSelection):
        for i in range(0,len(recipeSelection)):
            # remove from the end to avoid messing up indices
            j=len(recipeSelection)-i-1
            print("Removed recipe #" + str(recipeSelection[j]) + " (" + recipesList[recipeSelection[j]][0] + ")")
            del recipesList[recipeSelection[j]]
        return recipesList
        
        
    # Searches directory for .xml recipe files
    # Returns a list of strings of recipe filenames
    def loadRecipes(self, directory):
        self.fileList = []

        # If function is executed without arguments, use current working directory
        if directory is '':
            self.fileList += [each for each in os.listdir(os.getcwd()) if each.endswith('.xml')]
            self.directory = os.getcwd()
        else:
            self.fileList += [each for each in os.listdir(directory) if each.endswith('.xml')]
            self.directory = directory

        recipesList = []
        for file in self.fileList:
            tree = self.getXML(file)
            recipe = self.readRecipe(tree, file)
            recipesList.append(recipe)
        return recipesList
    
    
    # Converts given .xml file into tree structure
    # Returns tree
    def getXML(self, string):

        #from xml.etree import ElementTree as ET
        tree = ET.parse(string)

        return tree
    
    
    # Converts tree structure into list of lists
    # Returns list of lists that represents the recipe
    def readRecipe(self, tree, file):

        root = tree.getroot()

        # Array for ingredients
        ingredients = []
        i = 0

        for ingredient in root[0][3].findall('ingredient'):
            ingredients.append([])
            ingredients[i].append(ingredient.get('name'))
            ingredients[i].append(ingredient.get('quantity'))
            ingredients[i].append(ingredient.get('unit'))
            i += 1

#        ["recipe name", 
#                      "filepath", 
#                       [bake time, "units"],
#                       [bake temp, "units"],
#                       servings,
#                       [["ingredient name", quantity, "units"],
#                           [...],  ...
#                         [...]],
#                       "procedure"] 
        recipe = []
        # name
        recipe.append(root[0].get('name'))
        # filepath
        recipe.append(str(self.directory) + "/" + str(file))
        # time, units
        recipe.append([root[0][1][0].text,root[0][1][1].text])
        # temp, units
        recipe.append([root[0][2][0].text, root[0][2][1].text])
        # servings
        recipe.append(root[0][0].text)
        # ingredients
        recipe.append(ingredients)
        # procedure
        recipe.append(root[0][4].text)

        return recipe
    
    
    # Converts list of lists to string and writes to file
    # Returns nothing
    def writeRecipe(self, filename, recipe):    
        
        file = open(filename, 'w')

        file.write('<?xml version ="1.0"?>')

        recipeString1 = '<data><recipe name="' + recipe[0] + '">'\
                        '<servings>' + recipe[1] + '</servings>'\
                        '<baketime><time>' + recipe[2][0] + '</time>'\
                        '<unit>' + recipe[2][1] + '</unit></baketime>'\
                        '<baketemp><temp>' + recipe [3][0] + '</temp>'\
                        '<unit>' + recipe[3][1] + '</unit></baketemp>'

        recipeString2 = '<ingredients>'

        i = 0
        
        for ingred in recipe[4]:
            recipeString2 += '<ingredient name="' + recipe[4][i][0] + \
            '" quantity="' + recipe[4][i][1] + '" unit="' + recipe[4][i][2] + \
            '"/>'
            i += 1

        recipeString2 += '</ingredients>'

        recipeString3 = '<procedure>' + recipe[5] + '</procedure></recipe></data>'

        recipeString = recipeString1 + recipeString2 + recipeString3
        
        file.write(recipeString)
        
        file.close()
