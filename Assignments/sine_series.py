x=int(input('Enter the angle of sine: '))
a=int(input('Enter the number of terms: '))
sin=0
def fact(n):
    f=1
    if n==0 or n==1:
        return 1
    for i in range(1,n+1):
        f=f*i
    return f
for j in range(1,a*2,2):
    term=((x**j)/fact(j))*((-1)**(j//2))
    sin=sin+term
print(f'The sum of {a} terms of sine series is:{sin}')
