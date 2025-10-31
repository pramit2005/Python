a=input('Enter the string 1: ')
b=input('Enter the string 2: ')
c=[]
if len(a)==len(b):
    for i in a:
        if i not in b:
            c.append(i)
    if len(c)>1:
        print('The strings are not nearly equal')
    else:
        print('The strings are nearly equal')
else:
    print('The strings are not nearly equal')