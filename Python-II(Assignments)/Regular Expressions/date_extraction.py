import re
pattern=r"\b\d{2}/\d{2}/\d{4}\b"
a=input('Enter the paragraph:')
x=re.findall(pattern,a)
print(x)