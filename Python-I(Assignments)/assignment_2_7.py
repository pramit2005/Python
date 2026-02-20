salary=int(input('Enter your salary: '))
yoe=int(input('Enter your YOE: '))
if yoe>=5:
    print(f'Congratulations,You will get bonus salary \n The bonus is {salary/20} \n Net salary will be: {salary+salary/20}')
else:
    print('Sorry,you will not bonus salary because of lack of experience')