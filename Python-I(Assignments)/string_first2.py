a=input('Enter the string: ')
b=[]
if len(a)<=2:
    print(b)
else:
    b.append(a[0])
    b.append(a[1])
    b.append(a[-2])
    b.append(a[-1])
    print(''.join(b))