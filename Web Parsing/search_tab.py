#opens several google search results
import bs4,requests,webbrowser,sys
print('Googling...')
res=requests.get('https://google.com/search?q=',params={'q':sys.argv[1:]},)
try:
    res.raise_for_status()
except Exception as exc:
    print('A problem occured: '+ exc)

soup=bs4.BeautifulSoup(res.text,features="html.parser")
linkElems=soup.select('a')
print('length: ',len(linkElems))
numOpen=min(5,len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://google.com' + linkElems[i].get('href'))
