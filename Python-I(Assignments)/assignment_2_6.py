class_held=int(input('Enter the classes held: '))
class_att=int(input('Enter the no of classes attended: '))
if ((class_att/class_held)*100)>=75:
    print('You are allowed to sit for university exam')
else:
    print('Ypu are not allowed to sit for university exam')
