import math
a,b,c=map(int,input('Enter the co-efficients: ').split())
d=b**2-4*a*c
if d>0:
    print('The roots are real')
    root1=(-b+math.sqrt(d))/2*a
    root2 = (-b-math.sqrt(d))/2*a
    print(f'The roots are {root1} & {root2}')
elif d==0:
    print('The roots are real & equal')
    root1 = (-b + math.sqrt(d)) / 2 * a
    root2 = (-b - math.sqrt(d)) / 2 * a
    print(f'The roots are {root1} & {root2}')
else:
    d=d*-1
    print('The roots are imaginary')
    root1=complex(-b/2*a,math.sqrt(d)/2*a)
    root2= complex(-b/2*a,-math.sqrt(d) / 2 * a)
    print(f'The root1 is {root1} & real part is {root1.real} & the imaginary part is {root1.imag}')
    print(f'The root2 is {root2} & real part is {root2.real} & the imaginary part is {root2.imag}')
