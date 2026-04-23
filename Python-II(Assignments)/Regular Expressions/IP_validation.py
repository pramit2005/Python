import re
pattern=r"\b(?:25[0-5]|2[0-4]\d|1\d\d|[0-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[0-9]?\d)){3}\b"
a=input('Enter the text:')
x=re.findall(pattern,a)
print(x)