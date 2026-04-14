def new_std(l):
    a=input('Enter the name:')
    b=int(input('Enter the age:'))
    c=list(map(int,input('Enter the marks:').split()))
    l.append([a,b,c])
def result(r):
    total=sum(r)
    p=total/len(r)
    print(f'The total marks obtained is:{total} & the obtained percentage is:{p:.2f}')