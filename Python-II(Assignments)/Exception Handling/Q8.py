#Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
try:
    a=float(input('Enter a number: '))
    b=float(input('Enter another number: '))
    c=a/b
except ArithmeticError:
    print('Arithmetic operation is not possible')
else:
    print('Result:',c)