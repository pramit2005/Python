a=input("Enter the line/paragraph: ")
b=a.split()
for i in range(len(b)):
    if b[i].lower()=='a' or b[i].lower()=='an':
        b[i]='the'
print(' '.join(b))
