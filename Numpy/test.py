mat1=[]
mat2=[]
mat=[]
r1=int(input('Enter the number of rows of matrix 1: '))
r2=int(input('Enter the number of rows of matrix 2: '))
for i in range(0,r1):
    b=list(map(int,input(f'Enter the elements of row{i+1} of matrix 1: ').split()))
    mat1.append(b)
for j in range(0,r2):
    c=list(map(int,input(f'Enter the elements of row{j+1} of matrix 2: ').split()))
    mat2.append(c)
c1=len(mat1[0])
c2=len(mat2[0])
if (c1!=r2):
    print('Matrix multiplication not possible')
else:
    mat=[[0 for _ in range(c2)] for _ in range(r1)]
    for i in range(0,r1):
        for j in range(0,c2):
            for k in range(0,c1):
                mat[i][j]+=mat1[i][k]*mat2[k][j]
    print('The resultant matrix is: ')
    for i in mat:
        print(i)
