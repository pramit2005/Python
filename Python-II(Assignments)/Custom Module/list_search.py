import search
l=list(map(int,input('Enter the data:').split()))
l.sort()
x=int(input('Enter the element to search:'))
y=search.binary_search(l,0,len(l)-1,x)
if y==-1:
    print('Element not found')
else:
    print(f'Element found at position {y+1}')
