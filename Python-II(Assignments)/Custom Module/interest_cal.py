import interest
a=int(input("Enter the principle amount:"))
b=float(input('Enter the rate of interest:'))
c=int(input('Enter the time period:'))
print(f'The simple interest is:{interest.si(a,b,c)}\nThe compound interest is:{interest.cpi(a,b,c)}')