mat1=[]
r1=int(input('\n Enter the number of rows of matrix 1: '))
for i in range(r1):
    a=list(map(int,input(f'Enter the elements of row {i+1}: ').split()))
    mat1.append(a)
mat2=[]
r2=int(input('\n Enter the number of rows of matrix 2: '))
for j in range(r2):
    b=list(map(int,input(f'Enter the elements of row {j+1}: ').split()))
    mat2.append(b)
if len(mat1[0])!=len(mat2):
    print('Matrix multiplication not possible')
else:
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j]+=mat1[i][k]*mat2[k][j]
    print('The resultant matrix is : ')
    for i in result:
        print(i)
