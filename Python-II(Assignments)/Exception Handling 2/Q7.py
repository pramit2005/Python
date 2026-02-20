class AgeNegativeError(Exception):
    pass
try:
    a=int(input('Enter the age: '))
    if a<0:
        raise AgeNegativeError
except ValueError:
    print('Enter a valid input')
except AgeNegativeError:
    print('Age cannot be negative')
else:
    if 18 <= a <= 50:
        print('You are eligible for driving licence')
    else:
        print('You are not eligible for driving licence')
