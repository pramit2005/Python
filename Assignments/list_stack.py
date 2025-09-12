a=[]
while True:
    print(' 1.Push\n 2.Pop\n 3.Display\n 4.Exit')
    x = int(input('Enter a option: '))
    if x==1:
        b=int(input('Enter the data: '))
        a.append(b)
    elif x==2:
        a.pop()
    elif x==3:
        print(a)
    elif x==4:
        exit()
    else:
        print('Invalid option')
