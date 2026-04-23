import re
number=re.compile(r"\d+(?:[.]\d+)?")
a=input('Enter the text:')
x=number.findall(a)
print(x)