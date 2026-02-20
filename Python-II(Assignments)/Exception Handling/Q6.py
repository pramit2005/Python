#Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
try:
    a=[1,2]
    print(a[-3])
except IndexError:
    print('Invalid Index')

