## You can use these commands to test these functions:
##    scanForRecipes()
##    tree = getXML('TestRecipe.xml')
##    recipe = readRecipe(tree)
##    writeRecipe(filename, recipe)

import os, sys
from xml.etree import ElementTree as ET

class Model:
	# Searches directory for .xml recipe files
	# Returns a list of strings of recipe filenames
	def scanForRecipes(self, directory = None):
		
		recipeList = []

		# If function is executed without arguments, use current working directory
		if directory is None:
			recipeList += [each for each in os.listdir(os.getcwd()) if each.endswith('.xml')]
		else:
			recipeList += [each for each in os.listdir(directory) if each.endswith('.xml')]

		return recipeList

	# Converts given .xml file into tree structure
	# Returns tree
	def getXML(self, string):

		#from xml.etree import ElementTree as ET
		tree = ET.parse(string)

		return tree

	# Converts tree structure into list of lists
	# Returns list of lists that represents the recipe
	def readRecipe(self, tree):

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

		recipe = []
		recipe.append(root[0].get('name'))
		recipe.append(root[0][0].text)
		recipe.append([])
		recipe[2].append(root[0][1][0].text)
		recipe[2].append(root[0][1][1].text)
		recipe.append([])
		recipe[3].append(root[0][2][0].text)
		recipe[3].append(root[0][2][1].text)
		recipe.append(ingredients)
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
