a=input('Enter the email: ')
index1=a.index('@')
index2=a.index('.')
print(f' User name: {a[0:index1]}\n Company name: {a[index1+1:index2]} ')

