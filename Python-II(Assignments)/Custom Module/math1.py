def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    try:
        c=a/b
    except ZeroDivisionError:
        print('Division by zero is not possible')
        return None
    else:
        return c
