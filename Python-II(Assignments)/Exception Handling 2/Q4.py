#Write a program to simulate a login system using a predefined set of usernames and passwords. The program should handle incorrect usernames and passwords
#using appropriate exception handling techniques. [ Wrong username → KeyError,Wrong password → custom exception ]
class IncorrectPasswordError(Exception):
    pass
dict={'user1':'user1@1234','user2':'user2@4321'}
x=input('Enter the username: ')
y=input('Enter the password: ')
try:
    if dict[x]==y:
        print(f'Welcome {x}')
    else:
        raise IncorrectPasswordError
except KeyError:
    print('Incorrect Username')
except IncorrectPasswordError:
    print('Incorrect Password')