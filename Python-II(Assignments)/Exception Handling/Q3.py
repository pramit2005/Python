#Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    file=open('../Exception Handling 2/a.txt', 'r')
except FileNotFoundError:
    print('File does not exists')
else:
    print('File exists')
