
#Use test case:
#http://allrecipes.com/Recipe/Easy-Fruit-Cobbler/
#http://allrecipes.com/Recipe/Sugar-Cookie-Icing/
#Any others, just follow that format.


#importing regular expression thing
import re
#importing url thing
import urllib.request

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
            proc_str += (' ' + temp_str)
        
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
        
fetch = urlFetch()
fetch.main("http://allrecipes.com/Recipe/Slow-Cooker-Stuffing-2/Detail.aspx?soid=recs_recipe_seed")