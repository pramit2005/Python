import bs4
soup=bs4.BeautifulSoup(open('HTML/example.html'),features='html.parser')
spanElem=soup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))

