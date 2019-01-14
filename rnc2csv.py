#скрипт делает табличку csv из сохранённой html-страницы выдачи НКРЯ
#не забыть в html поменять кодировку на utf
#столбцы в таблице: источник текста, искомое слово, пример

import re
def openfile ():
    f = open ('C:\\Users\\Настя\\Desktop\\2.html', 'r', encoding = 'utf-8')
    txt = f.read()
    f.close
    return txt
def search (txt):
    txt2 = ''
    regexp1 = '\<li\>(.+?)\<\/li\>' 
    res = re.findall (regexp1, txt)
    if res:
        for line in res:
            regexp2 = '\<span class="b-wrd-expl g-em".*?\>(.*?)\<\/span\>'
            res2 = re.findall (regexp2, line)
            if res2:
                for match in res2:
                    match = re.sub(r'(\<(/?[^>]+)>)', '', match)
                    #print (match)
                    regexp3 = '\<span class="doc"\>(.*?)\<\/span\>'
                    res3 = re.search (regexp3, line)
                    if res3:
                        source = res3.group(1)
                        source = re.sub(r'(\<(/?[^>]+)>)', '', source)
                        #print (source)
                    line = re.sub(r'\<span class="doc"\>.*?\<\/span\>', '', line)
                    line = re.sub(r'(\<(/?[^>]+)>)', '', line)
                    line = re.sub(r'\[.*?\]', '', line)
                    line = re.sub(r'      &#8592;…&#8594;', '', line)
                    #print (line)
            txt2 = txt2 + source + '\t' + match + '\t' + line + '\n'
        
    return txt2
def savefile (txt2):
    f = open ('C:\\Users\\Настя\\Desktop\\rnc.csv', 'w', encoding = 'utf-8')
    f.write (txt2)
    f.close
def main ():
    f1 = openfile ()
    f2 = search (f1)
    f3 = savefile (f2)

if __name__ == '__main__':
    main ()
