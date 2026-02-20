class Calculator:
    @staticmethod
    def add(a,b):
        print(f'The sum is:{a+b}')
    @staticmethod
    def sub(a,b):
        print(f'The subtraction is:{a-b}')
    @staticmethod
    def mul(a,b):
        print(f'The multiplication is:{a*b}')
    @staticmethod
    def div(a,b):
        try:
            print(f'The division is:{a/b}')
        except ZeroDivisionError:
            print('Division by zero is not possible')
c,d=map(int,input('Enter two numbers: ').split())
Calculator.add(c,d)
Calculator.sub(c,d)
Calculator.mul(c,d)
Calculator.div(c,d)