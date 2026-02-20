#Design a Python program to simulate a simple bank account system. The program should allow a user to deposit and withdraw money.
#Ensure that the system handles invalid inputs and prevents withdrawal of an amount greater than the available balance using appropriate exception handling.
class InsufficientBalanceError(Exception):
    pass
class Bank:
    def __init__(self,name,age,amount):
        self.name=name
        self.age=age
        self.__balance=amount   #Used Encapsulation
    def check_balance(self):
        return self.__balance
    def withdraw(self,amount):
        if amount<0:
            raise ValueError
        if amount>self.__balance:
            raise InsufficientBalanceError
        else:
            self.__balance=self.__balance-amount
    def deposit(self,amount):
        if amount<0:
            raise ValueError
        self.__balance=self.__balance+amount
a=Bank('Pramit',20,1000)
try:
    a.deposit(1)
    a.withdraw(9999)
except ValueError:
    print('Enter a positive amount')
except InsufficientBalanceError:
    print('Withdrawal not possible')

