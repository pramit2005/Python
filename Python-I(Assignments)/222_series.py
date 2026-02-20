import dis
a=int(input('Enter the number of terms: '))
def term_cal(n):
    term=0
    for i in range(0,n):
        term=(term*10)+2
    return term
dis.dis(term_cal)
sum=0
for i in range(1,a+1):
    term=term_cal(i)
    sum=sum+term
print(f'The sum of the series is:{sum}')
