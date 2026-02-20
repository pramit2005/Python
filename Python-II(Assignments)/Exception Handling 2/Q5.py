#Develop a program that attempts to open and read a file specified by the user. The program should handle exceptions such
# as files not found and permission issues gracefully.
try:
    a=input('Enter the name of the file: ')
    file=open(a,'r')
    print(file.read())
except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('User does not have the necessary permission to access the file')