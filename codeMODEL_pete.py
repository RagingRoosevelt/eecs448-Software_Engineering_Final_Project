def scanForRecipes(directory):

    import os, sys
    recipeList = []

    recipeList += [each for each in os.listdir(directory) if each.endswith('.xml')]

    return recipeList

def readRecipe(string):
    
    from xml.etree import ElementTree as ET
    tree = ET.parse(string)
    root = tree.getroot()

    # Get recipe data
    name = root[0].get('name')
    servings = root[0][0].text
    bakeTime = root[0][1][0].text
    timeUnits = root[0][1][1].text
    bakeTemp = root[0][2][0].text
    tempUnits = root[0][2][1].text
    procedure = root[0][4].text

    # Mx3 array of ingredients
    ingredients = []
    ingredients.append([])
    ingredients.append([])
    ingredients.append([])

    # The following strings may be used to access the arrays columns
    names = 0
    quantities = 1
    units = 2

    # There is likely a better way to implement the ingredient array. I'm open to suggestions!
    for ingredient in root[0][3].findall('ingredient'):
        ingredients[names].append(ingredient.get('name'))
        ingredients[quantities].append(ingredient.get('quantity'))
        ingredients[units].append(ingredient.get('unit'))
