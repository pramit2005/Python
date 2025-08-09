import math
def isLeapyear(a):
    if ((a % 4 == 0) and (a % 100 != 0))or(a % 400 == 0):
        return True
    else:
        return False
month,year=map(int,input('Enter the month & year in integers: ').split())
m={1:['January',31],2:['February',28],3:['March',31],4:['April',30],5:['May',31],6:['June',30],
   7:['July',31],8:['August',31],9:['September',30],10:['October',31],11:['November',30],12:['December',31]}
if month==2 and isLeapyear(year):

    print(f'{m[month][0]} {year} has {m[month][1]+1}days ')
else:

    print(f'{m[month][0]} {year} has {m[month][1]}days ')


