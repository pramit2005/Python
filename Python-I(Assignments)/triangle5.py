r=int(input('Enter the number of rows: '))
for i in range(1,r+1):
    for k in range(1,r-i+1):
       print(' ',end=' ')
    odd=2*i-1
    for j in range(i,odd+1):
        print(j,end=' ')
    for x in range(odd-1,i-1,-1):
        print(x,end=' ')
    print()