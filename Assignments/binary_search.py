def binary_search(l,left,right,x):
    mid=(left+right)//2
    if x<l[left] or x>l[right]:
        return -1
    elif left>right:
        return -1
    else:
        if l[mid]==x:
            return mid
        elif l[mid]<x:
            return binary_search(l,mid+1,right,x)
        elif l[mid]>x:
            return binary_search(l,left,mid-1,x)
a = []
a = list(map(int, input("Enter the data: ").split()))
a.sort()
n=len(a)
y=int(input('Enter the data to search: '))
m=binary_search(a,0,n-1,y)
print(f'The sorted list: {a}')
if m==-1:
    print('The element is not in list')
else:
    print(f'The element is in position: {m+1}')