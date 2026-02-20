import math
r=int(input('Enter the number of rows: '))
mid=math.ceil(r/2)
for i in range(1,mid+1):
    for j in range(1,i+1):
        print( j ,end=' ')
    print()
for k in range(mid,1,-1):
    for l in range(1,k):
        print( l ,end=' ')
    print()