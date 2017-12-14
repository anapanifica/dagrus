import re
def function1 ():
    f = open ('C:\\Users\\Настя\\Desktop\\ubeqi_03.TextGrid', 'r', encoding = 'utf-8')
    string = f.read()
    string = string.split ('\n')
    f.close ()
##    for word in string:
##        print (word)
    return string
def function2(string):
    text = ''
    for line in string:
        if 'text = ' in line:
            #print (line)
            regexp = 'text = "(.+?)"'
            res = re.search (regexp, line)
            if res:
                lex = res.group(1)
                lex = lex.capitalize()
                if ((lex.endswith('?') == False) and (lex.endswith('!') == False) and
                    (lex.endswith('...') == False)):
                    lex = lex + '.'
                #lex = re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), lex, 1)
                #lex = str(lex)
                #regex = re.compile("[A-Za-z]") # find a alpha
                #s = regex.search(lex).group() # find the first alpha
                #lex = lex.replace(s, s.upper(), 1) # replace only 1 instance
                #lex = re.sub(r'(\d\w)', lambda w: w.group()[0].upper(), lex)

                line = re.sub(res.group(1), lex, line)
        #print (line)

        text = text + line + '\n'
    text = text.replace ('??', '?')
    text = text.replace ('[[нрзб].[нрзб].[нрзб].[нрзб].]', '[нрзб]')
    print (text)
    f = open ('C:\\Users\\Настя\\Desktop\\ubeqi_03_capitalized.TextGrid', 'w', encoding = 'utf-8')
    f.write (text)
def main ():
    f1 = function1 ()
    f2 = function2 (f1)
if __name__ == '__main__':
    main ()
