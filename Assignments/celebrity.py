mat=[]
n=int(input('Enter the number of guests in party: '))
cel=0
flag=0
for i in range(n):
    row=list(map(int,input(f"Enter the people known by guest {i}(space separated): ").split(' ')))
    mat.append(row)
    if sum(row)==1:
        for j in range(i):
            if row[j]==1:
                flag=1
        for k in range(i+1,n):
            if row[k]==1:
                flag=1
        if flag==0:
            cel=i
print(f'The celebrity is: {cel+1}th guest')




