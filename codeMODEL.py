## You can use these commands to test these functions:
##    loadRecipes()
##    tree = getXML('TestRecipe.xml')
##    recipe = readRecipe(tree)
##    writeRecipe(filename, recipe)

# for main Model
import os, sys
from xml.etree import ElementTree as ET
from subprocess import call

# for URL fetch
import re
import urllib.request

class Model:
    def __init__(self):
        self.fetch = urlFetch()
        
    def urlLoad(self, URL):
        return self.fetch.main(URL)
        
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
            file = self.directory + "\\" + file
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

        if directory == "":
            directory = os.getcwd()
        
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
        
        if directory == "":
            directory = os.getcwd() + "\\"
        if filename == "":
            filename = "output"
            
        print(directory)
        print(filename)
        
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
            procedurelist = recipe[6].split("\n\n")
            procedure = ""
            for i in range(0,len(procedurelist)):
                procedure += procedurelist[i]
                procedure += "\n\n\t\\\n\n\t"
        
            file.write("\n\\begin{recipe}{" + recipe[0] + "}{" + str(recipe[4]) + " servings}{")

            print(str(recipe[2][0]) + " and " + str(recipe[3][0]))
            if (recipe[2][1]!="") and (recipe[3][1]!=None):
                file.write(str(recipe[2][0]) + " " + str(recipe[2][1]) + " at " + str(recipe[3][0]) + "$^{\circ}$" + str(recipe[3][1]) )
            
            file.write("}")
            for ingredient in recipe[5]:
                file.write("\n\t\\ingredient[" + str(ingredient[1]) + "]{" + ingredient[2] + "}{" + ingredient[0] + "}")
            file.write("\n\n\t\\freeform \\newline " + procedure)
            file.write("\n\\end{recipe}\n\pagebreak\n")
        
        
        
        
        file.write("\n\\printindex\n\\end{document}")
        print("Wrote to " + directory + filename + ".tex")
        file.close()
        
        call(['pdflatex', "-output-directory="+directory , directory + filename + ".tex"], shell=False)
        os.remove(directory+filename+".aux")
        os.remove(directory+filename+".log")
        
        
        
        
        
        
class urlFetch:
    def __init__(self):
        #some strings I'm using to extract text (from allrecipes)
        self.title_beg_tag = 'property="og:title" content="'
        self.title_end_tag = '"></meta>'
        self.serv_beg_tag = 'data-originalservings="'
        self.serv_end_tag = '" data'
        self.ing_amnt_tag = '<span id="lblIngAmount" class="ingredient-amount">'
        self.ing_name_tag = '<span id="lblIngName" class="ingredient-name">'
        self.end_tag = '</span>'

    def main(self, uchoice):
        #htmlstr = htmlinstring
        htmlstr = self.gethtml(uchoice)
        #title_string = findtitle(htmlstr)
        #print ('The recipe title is: ' + title_string + '\n')
        #writerecipe(title_string, htmlstr)
        recipe = self.getrecipeparts(htmlstr)
        print(recipe)
        return recipe
        
        
    def gethtml(self, page_to_get):
        #getting the html (in byte form)
        response = urllib.request.urlopen(page_to_get)
        htmlinbytes = response.read()
        response.close()
        #converting html to string
        htmlinstring = htmlinbytes.decode(encoding='utf-8')
        return htmlinstring

    def findtitle(self, htmlstr):
        #regular expression to find recipe title
        title_re = re.compile(r'property="og:title" content=".*"></meta>')
        #finding recipe name
        title_m = title_re.search(htmlstr)
        #convoluted string extraction
        if title_m:
            x = title_m.span()[0]
            y = title_m.span()[1]
            x = x + len(self.title_beg_tag)
            y = y - len(self.title_end_tag)
            
            title_string = ""
        
            while x < y:
                title_string += htmlstr[x]
                x+=1
        
            return title_string  
        #else:
            #print("No title.")
            
    def getserv(self, htmlstr):        
        serv_re = re.compile(r'data-originalservings=".*" data')
        
        serv_m = serv_re.search(htmlstr)
        
        if serv_m:
            x = serv_m.span()[0]
            y = serv_m.span()[1]
            x = x + len(self.serv_beg_tag)
            y = y - len(self.serv_end_tag)
        
            serv_string = ""
            while x < y:
                serv_string += htmlstr[x]
                x+=1
            return serv_string
        #else:
            #print("No servings.")

    def gettime(self, htmlstr):
        time_re = re.compile(r'<span id="cookHoursSpan"><em>.*</em>.*</span>')
        time_m = time_re.search(htmlstr)
        
        str1 = '<span id="cookHoursSpan"><em>'
        str2 = '</em> hr</span>'
        
        if time_m:
            x = time_m.span()[0]
            y = time_m.span()[1]
            x = x + len(str1)
            y = y - len(str2)
        
            time_string = ""
        
            while x < y:
                time_string += htmlstr[x]
                x+=1
            return time_string
        else:
            return " "

    def gettimeunit(self, htmlstr):
        time_re = re.compile(r'<span id="cookHoursSpan"><em>.*</em>.*</span>')
        time_m = time_re.search(htmlstr)
        
        str1 = '<span id="cookHoursSpan"><em>1</em> '
        str2 = '</span>'
        
        if time_m:
            x = time_m.span()[0]
            y = time_m.span()[1]
            x = x + len(str1)
            y = y - len(str2)
        
            timeunit_string = ""
        
            while x < y:
                timeunit_string += htmlstr[x]
                x+=1
            
            return timeunit_string
        else:
            return " "
            
    def getingr(self, htmlstr):
        
        #some strings
        beg_amtstr = '<span id="lblIngAmount" class="ingredient-amount">'
        beg_namestr = '<span id="lblIngName" class="ingredient-name">'
        end_str = '</span>'
        
        #the regular expressions
        ingr_amt_re = re.compile(r'<span id="lblIngAmount" class="ingredient-amount">.*</span>')
        ingr_name_re = re.compile(r'<span id="lblIngName" class="ingredient-name">.*</span>')
        
        #finding matches
        #ingr_amt_m = ingr_amt_re.findall(htmlstr)
        #ingr_name_m = ingr_name_re.findall(htmlstr)
        
        #print (ingr_amt_m)
        #print (ingr_name_m)
        
        ingr_amt_iterator = ingr_amt_re.finditer(htmlstr)
        ingr_name_iterator = ingr_name_re.finditer(htmlstr)

        ingr_amt_list = []
        ingr_unit_list = []
        ingr_name_list = []
        
        for match in ingr_amt_iterator:
            ingr_amt_str = ""
            x = match.span()[0]
            y = match.span()[1]
            x = x + len(beg_amtstr)
            y = y - len(end_str)
            while x < y:
                ingr_amt_str += htmlstr[x]
                x+=1
                
            #splitting, formatting, gonna get hairy here
            quick_re_1 = re.compile(r'\d')
            quick_m_1 = quick_re_1.search(ingr_amt_str)
            quick_re_2 = re.compile(r'\d/\d')
            quick_m_2 = quick_re_2.search(ingr_amt_str)
            if quick_m_1:
                if quick_m_2:
                    lmnop = ""
                    l = quick_m_2.span()[0]
                    m = quick_m_2.span()[1]
                    while l < m:
                        lmnop += ingr_amt_str[l]
                        l+=1
                    ingr_amt_list.append(lmnop)
                else:
                    lmnop = ""
                    l = quick_m_1.span()[0]
                    m = quick_m_1.span()[1]
                    while l < m:
                        lmnop += ingr_amt_str[l]
                        l+=1
                    ingr_amt_list.append(lmnop)
            else:
                ingr_amt_list.append(" ")
                
                
            quick_re_3 = re.compile(r'[a-z]+')
            quick_m_3 = quick_re_3.search(ingr_amt_str)
            xyzzy = ""
            if quick_m_3:
                k = quick_m_3.span()[0]
                u = quick_m_3.span()[1]
                while k < u:
                    xyzzy += ingr_amt_str[k]
                    k+=1
                ingr_unit_list.append(xyzzy)
            else:
                ingr_unit_list.append(" ")
            
        for match in ingr_name_iterator:
            ingr_name_str = ""
            x = match.span()[0]
            y = match.span()[1]
            x = x + len(beg_namestr)
            y = y - len(end_str)
            while x < y:
                ingr_name_str += htmlstr[x]
                x+=1
            ingr_name_list.append(ingr_name_str)
            
        return ingr_amt_list, ingr_unit_list, ingr_name_list
        
    def getproc(self, htmlstr):
        beg_proc_str = '<li><span class="plaincharacterwrap break">'
        end_proc_str = '</span></li>'
        
        proc_str = ""
        
        proc_re = re.compile(r'<li><span class="plaincharacterwrap break">.*</span></li>')
        proc_iterator = proc_re.finditer(htmlstr)
        for match in proc_iterator:
            temp_str = ""
            x = match.span()[0]
            y = match.span()[1]
            x = x + len(beg_proc_str)
            y = y - len(end_proc_str)
            while x < y:
                temp_str += htmlstr[x]
                x+=1
            proc_str += (' ' + temp_str) + "\n\n"
        
        return proc_str
            
        
    def getrecipeparts(self, htmlstr):
        recipe = ["","",[0,""],[0,""],0,[],""]
        recipe[0] = self.findtitle(htmlstr)
        recipe[2][0] = self.gettime(htmlstr)
        recipe[2][1] = self.gettimeunit(htmlstr)
        recipe[4] = self.getserv(htmlstr)
        ingr_amt_list, ingr_unit_list, ingr_name_list = self.getingr(htmlstr)
        #print (ingr_amt_list)
        #print (ingr_unit_list)
        #print (ingr_name_list)
        x = 0
        while x < len(ingr_unit_list):
            recipe[5].append([ingr_name_list[x],ingr_amt_list[x],ingr_unit_list[x]])
            x+=1
        recipe[6] = self.getproc(htmlstr)
        
        return recipe
        #print(ingr_amt_list)
        #print(ingr_unit_list)
        #print(ingr_name_list)
        #print (recipe)
        
