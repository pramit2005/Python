def combination(n,r):
    import math
    return (math.factorial(n)//(math.factorial(n-r)*math.factorial(r)))
def pascal():
    m=int(input('Enter the number of rows: '))
    for i in range(0,m):
        for k in range(0,m-i+1):
            print(' ',end='')
        for j in range(0,i+1):
            print(combination(i,j),end=' ')
        print()
pascal()
