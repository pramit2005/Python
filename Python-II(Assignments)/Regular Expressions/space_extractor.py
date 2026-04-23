import re
a=input('Enter the text:')
x=re.sub(r" ",'-',a)
print(x)