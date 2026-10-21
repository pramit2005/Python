import bs4
exampleFile=open('HTML/example.html')
exampleSoup=bs4.BeautifulSoup(exampleFile,features='html.parser')
elems=exampleSoup.select('#author')

pElems=exampleSoup.select('p')
print(len(pElems))
for i in range(len(pElems)):
    print(pElems[i].getText())
