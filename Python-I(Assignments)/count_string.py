a=list(input('Enter the string: '))
b={}
for i in a:
    b[i]=b.setdefault(i,0)+1
print(b)



