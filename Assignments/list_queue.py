a=[]
while True:
    print(' 1.Enqueue\n 2.Dequeue\n 3.Display\n 4.Exit')
    x = int(input('Enter a option: '))
    if x==1:
        b=int(input('Enter the data: '))
        a.append(b)
    elif x==2:
        a.pop(0)
    elif x==3:
        print(a)
    elif x==4:
        exit()
    else:
        print('Invalid option')