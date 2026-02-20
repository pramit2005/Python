
x=int(input('Enter the angle of cosine: '))
m=int(input('Enter the number of terms of the series: '))
cos=0
def fact(n):
    f=1
    if n==0 or n==1:
        return 1
    for i in range(1,n+1):
        f=f*i
    return f
for j in range(0,m*2,2):
    term=(x**j/fact(j))*((-1)**(j//2))
    cos=cos+term
print(f'The sum of {m} terms are : {cos}')
