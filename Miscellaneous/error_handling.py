a,b=map(int,input('Enter the numbers: ').split())
print(f'\n Addition: {a+b}\n Subtraction: {a-b}\n Multiplication: {a*b}')
try:
    print(f' Division: {a/b}')
except ZeroDivisionError:
    print(' Cannot divide by zero!')

