import re
spc=re.compile(r"[$@!%&*.~#<>':;^]")
a=input('Enter text:')
x=spc.sub('',a)
print(x)