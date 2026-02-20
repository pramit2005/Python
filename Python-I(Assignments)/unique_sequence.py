a=list(input('Enter the words(comma separated): ').split(','))
b=[]
for i in a:
    if i not in b:
        b.append(i)
b.sort()
print(','.join(b))
