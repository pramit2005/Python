def jump_search(l,j,x):
    n=len(l)
    key=j-1
    pos=-1
    for i in range(0,n,j):
        key=min(i+j-1,n-1)
        if l[key] >= x:
            for k in range(i, key + 1):
                if l[k] == x:
                    pos = k
                    break
            break
    if pos==-1:
        print('The element is not in list')
    else:
        print(f'The element is in position: {pos+1}')
a=list(map(int,input("Enter the data: ").split()))
a.sort()
jump=int(input('Enter the jump: '))
y=int(input("Enter the data tob search: "))
jump_search(a,jump,y)