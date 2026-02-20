a = input('Enter the string: ')
b = []
for i in a:
    if i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'o' or i.lower() == 'u' or i.lower() == 'i':
        b.append(i)
print(''.join(b))
