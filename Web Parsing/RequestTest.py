import requests
res=requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
try:
    res.raise_for_status()
except Exception as exc:
    print(f'A problem occurred: {exc}')
print(type(res))
print(len(res.text))
if res.status_code==requests.codes.ok:
    print(res.text[:250])
