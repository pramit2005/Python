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
def linear_search(l,x):
    n=len(l)
    for i in range(n):
        if l[i]==x:
            return i
    return -1