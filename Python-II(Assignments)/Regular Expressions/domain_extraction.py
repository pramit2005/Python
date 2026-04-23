import re
x=[]
pattern=r"(?:https?://)?(?:www[.])?([^/]+)"
a=input('Enter the URLs:').split()
for i in a:
    b=re.match(pattern,i)
    if b:
        x.append(b.group(1) or b.group(2))
print(x)