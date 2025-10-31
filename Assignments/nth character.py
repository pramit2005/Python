a=list(input('Enter the string: '))
ind=int(input('Enter the position of the character to remove: '))
del a[ind-1]
print(''.join(a))
