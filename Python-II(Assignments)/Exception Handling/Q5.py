#Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
try:
    file=open('../Exception Handling 2/a.txt', 'r')
    raise PermissionError
except PermissionError:
    print("Don't have the permission to open the file")

