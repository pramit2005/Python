import re
pattern=r"\B[#]\w+[^\s]"
a=input('Enter the paragraph:')
x=re.findall(pattern,a)
print(x)