#Develop a program to accept marks of 5 subjects from a student and calculate the average.
#The program should handle invalid inputs such as non-numeric values,marks outside the valid range (0–100), and missing inputs using exception
#handling. [ Marks > 100 or < 0 → custom error, Wrong input type → ValueError, Missing subject → IndexError]
class InvalidMarksError(Exception):
    pass
try:
    a=list(map(int, input('Enter the marks of 5 subjects: ').split()))
    if len(a)<5:
        raise IndexError
    for i in a:
        if i>100 or i<0:
            raise InvalidMarksError()
except ValueError:
    print('Please enter a valid marks type')
except IndexError:
    print('One or more subject marks are missing')
except InvalidMarksError:
    print("Marks can't exceed 100 or be lower than 0")
else:
    avg=sum(a)/5
    print('The average is:',avg)
