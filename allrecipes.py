
#Use test case:
#http://allrecipes.com/Recipe/Easy-Fruit-Cobbler/
# to see it kind of work
#Use:
#http://allrecipes.com/Recipe/Sugar-Cookie-Icing/
# to see it not work


#importing regular expression thing
import re
#importing url thing
import urllib.request

#strings from allrecipes
title_beg_tag = 'property="og:title" content="'
title_end_tag = '"></meta>'
serv_beg_tag = 'data-originalservings="'
serv_end_tag = '" data'
ing_amnt_tag = '<span id="lblIngAmount" class="ingredient-amount">'
ing_name_tag = '<span id="lblIngName" class="ingredient-name">'
end_tag = '</span>'

def main():
    uchoice = input('Input URL:')
    #htmlstr = htmlinstring
    htmlstr = gethtml(uchoice)
    #title_string = findtitle(htmlstr)
    #print ('The recipe title is: ' + title_string + '\n')
    #writerecipe(title_string, htmlstr)
    getrecipeparts(htmlstr)
    
def gethtml(page_to_get):
    #getting the html (in byte form)
    response = urllib.request.urlopen(page_to_get)
    htmlinbytes = response.read()
    response.close()
    #converting html to string
    htmlinstring = htmlinbytes.decode(encoding='utf-8')
    return htmlinstring

def findtitle(htmlstr):
    #regular expression to find recipe title
    title_re = re.compile(r'property="og:title" content=".*"></meta>')
    #finding recipe name
    title_m = title_re.search(htmlstr)
    #convoluted string extraction
    x = title_m.span()[0]
    y = title_m.span()[1]
    x = x + len(title_beg_tag)
    y = y - len(title_end_tag)
    
    title_string = ""
    
    while x < y:
        title_string += htmlstr[x]
        x+=1
    
    return title_string  
    
def getserv(htmlstr):        
    serv_re = re.compile(r'data-originalservings=".*" data')
    
    serv_m = serv_re.search(htmlstr)
    
    x = serv_m.span()[0]
    y = serv_m.span()[1]
    x = x + len(serv_beg_tag)
    y = y - len(serv_end_tag)
    
    serv_string = ""
    while x < y:
        serv_string += htmlstr[x]
        x+=1
    return serv_string

def gettime(htmlstr):
    time_re = re.compile(r'<span id="cookHoursSpan"><em>.*</em>.*</span>')
    time_m = time_re.search(htmlstr)
    
    str1 = '<span id="cookHoursSpan"><em>'
    str2 = '</em> hr</span>'
    
    x = time_m.span()[0]
    y = time_m.span()[1]
    x = x + len(str1)
    y = y - len(str2)
    
    time_string = ""
    
    while x < y:
        time_string += htmlstr[x]
        x+=1
    return time_string

def gettimeunit(htmlstr):
    time_re = re.compile(r'<span id="cookHoursSpan"><em>.*</em>.*</span>')
    time_m = time_re.search(htmlstr)
    
    str1 = '<span id="cookHoursSpan"><em>1</em> '
    str2 = '</span>'
    
    x = time_m.span()[0]
    y = time_m.span()[1]
    x = x + len(str1)
    y = y - len(str2)
    
    timeunit_string = ""
    
    while x < y:
        timeunit_string += htmlstr[x]
        x+=1
        
    return timeunit_string
    
def getrecipeparts(htmlstr):
    recipe = []
    for i in range(5):
        recipe.append([])
    recipe[2].append([])
    recipe[2].append([])
    recipe[3].append([])
    recipe[3].append([])
    recipe[0] = findtitle(htmlstr)
    recipe[1] = getserv(htmlstr)
    recipe[2][0] = gettime(htmlstr)
    recipe[2][1] = gettimeunit(htmlstr)
    
    print (recipe[0])
    print (recipe[1])
    print (recipe[2][0])
    print (recipe[2][1])
    print (recipe[3][0])
    print (recipe[3][1])
    print (recipe)
main()