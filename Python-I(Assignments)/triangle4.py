r=int(input('Enter the number of rows: '))
for i in range(1,r+1):
    for k in range(1,r-i+1):
       print(' ',end=' ')
    for j in range(1,2*i):
             print('*',end=' ')
    print()