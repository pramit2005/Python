st=input("Enter the string: ")
w=st.split()
min=9999
max=-1
for i in w:
    if len(i)>max:
        max_word=i
        max=len(i)
    if len(i)<min:
        min_word=i
        min=len(i)
print(f'The largest word is: {max_word} \n The length of the largest word: {max} '
      f'\n The smallest word is: {min_word} \n The length of the smallest word: {min}')


