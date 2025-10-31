a=input('Enter the string: ')
l=[]
u=[]
res=[]
for i in a:
    if i.islower():
        l.append(i)
    else:
        u.append(i)
res=l+u
print(''.join(res))

