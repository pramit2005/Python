#Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero
a=int(input('Enter the Dividend: '))
b=int(input('Enter the Divisor: '))
try:
    c=a/b
except ZeroDivisionError:
    print('Division by zero not possible')
else:
    print('The result is:',c)