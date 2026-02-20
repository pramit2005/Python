#Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer
try:
    a=input('Enter a valid integer: ')
    b=int(a)
except ValueError:
    print('The input is not a valid integer')
else:
    print('The input is a valid integer')