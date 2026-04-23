import re
tag=re.compile(r"</?\w+>")
a=input('Enter the text:')
x=tag.findall(a)
print(x)