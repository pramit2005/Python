a=input('Enter the string 1: ')
b=input('Enter the string 2: ')
str1=[]
str2=[]
for i in a:
    str1.append(i)
for j in b:
    str2.append(j)
if set(str1)==set(str2):
    print('The strings are anagram')
else:
    print('The strings are not anagram')