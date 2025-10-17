a=list(map(int,input('Enter the elements: ').split()))
b=[]
for i in a:
    if a.count(i)>1 and i not in b:
        b.append(i)
print('The duplicate elements are: ',b)