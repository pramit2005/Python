a=input('Enter the string: ')
if len(a)<3:
    print('String is too small')
elif a[-1]=='g' and a[-2]=='n' and a[-3]=='i':
    b='ly'
    a=a+b
    print(a)
elif len(a)>=3 and a[-1]!='y' and a[-2]!='l':
    b='ing'
    a=a+b
    print(a)
else:
    print(a)