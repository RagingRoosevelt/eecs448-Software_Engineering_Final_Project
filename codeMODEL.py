## You can use these commands to test these functions:
##    loadRecipes()
##    tree = getXML('TestRecipe.xml')
##    recipe = readRecipe(tree)
##    writeRecipe(filename, recipe)

import os, sys
from xml.etree import ElementTree as ET
from subprocess import call

class Model:
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
    def writeRecipe(self, directory, filename, recipe):    
        
        if not os.path.isdir(directory):
            os.makedirs(directory)
        
        file = open(directory + filename, 'w')

        file.write('<?xml version ="1.0"?>\n')

        recipeString1 = '<data>\n\t<recipe name="' + str(recipe[0]) + '">'\
                        '\n\t\t<servings>' + str(recipe[4]) + '</servings>'\
                        '\n\t\t<baketime>\n\t\t\t<time>' + str(recipe[2][0]) + '</time>'\
                        '\n\t\t\t<unit>' + str(recipe[2][1]) + '</unit>\n\t\t</baketime>'\
                        '\n\t\t<baketemp>\n\t\t\t<temp>' + str(recipe [3][0]) + '</temp>'\
                        '\n\t\t\t<unit>' + str(recipe[3][1]) + '</unit>\n\t\t</baketemp>'

        recipeString2 = '\n\t\t<ingredients>'

        i = 0
        
        for ingred in recipe[5]:
            recipeString2 += '\n\t\t\t<ingredient name="' + str(recipe[5][i][0]) + \
            '" quantity="' + str(recipe[5][i][1]) + '" unit="' + str(recipe[5][i][2]) + \
            '"/>'
            i += 1

        recipeString2 += '\n\t\t</ingredients>'

        recipeString3 = '\n\t\t<procedure>\n\t\t\t' + str(recipe[6]) + '\n\t\t</procedure>\n\t</recipe>\n</data>'

        recipeString = recipeString1 + recipeString2 + recipeString3
        
        file.write(recipeString)
        
        file.close()
        
    def writeLaTeX(self, directory, filename, recipeList):
        print(directory)
        if not os.path.isdir(directory):
            os.makedirs(directory)
        
        file = open(directory + filename + ".tex", 'w')
        
        file.write("\\documentclass{article}\n"+\
            "\\usepackage{makeidx}\n"+\
            "\\usepackage[nonumber,index]{cuisine}\n"+\
            "\\RecipeWidths{\\textwidth}{3cm}{0cm}{6cm}{.75cm}{2cm}\n"+\
            "\n\\usepackage{xcolor}\n"+\
            "\\renewcommand*{\\recipestepnumberfont}{\\color[HTML]{FFFFFF}}\n\n"+\
            "\\begin{document}\n\n")
        
        for recipe in recipeList:
            file.write("\n\\begin{recipe}{" + recipe[0] + "}{" + str(recipe[4]) + " servings}{")

            if (recipe[2][0]!=0) and (recipe[3][0]!=0):
                file.write(str(recipe[2][0]) + " " + str(recipe[2][1]) + " at " + str(recipe[3][0]) + "$^{\circ}$" + str(recipe[3][1]) )
            
            file.write("}")
            for ingredient in recipe[5]:
                file.write("\n\t\\ingredient[" + str(ingredient[1]) + "]{" + ingredient[2] + "}{" + ingredient[0] + "}")
            file.write("\n\t\\freeform " + recipe[6])
            file.write("\n\\end{recipe}\n\pagebreak\n")
        
        
        
        
        file.write("\n\\printindex\n\\end{document}")
        print("Wrote to " + directory + filename + ".tex")
        file.close()
        
        call(['pdflatex', "-output-directory="+directory , directory + filename + ".tex"], shell=False)
        #os.remove(directory+filename+".aux")
        #os.remove(directory+filename+".log")
        
        
        
        
        
        
