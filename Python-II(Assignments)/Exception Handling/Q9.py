#Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
try:
    a=[1,2,3]
    a.isdigit()
except AttributeError:
    print('This attribute is not available for list operations')


