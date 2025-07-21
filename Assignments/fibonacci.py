def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
m=int(input('Enter the range: '))
for i in range(m):
    print( fib(i) ,end=' ')


