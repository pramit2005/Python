#Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical
try:
    a=input('Enter a number: ')
    b=input('Enter another number: ')
    if a.isdigit() and b.isdigit():
        a=int(a)
        b=int(b)
    c=a-b
except TypeError:
    print('Inputs are not numerical')
else:
    print('Inputs are numerical')
