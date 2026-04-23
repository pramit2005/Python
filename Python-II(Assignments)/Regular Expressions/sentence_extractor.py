import re
pattern=r"([a-zA-Z0-9\s]+[^.?!])"
b=input('Enter the paragraph:')
x=re.findall(pattern,b)
print(x)
