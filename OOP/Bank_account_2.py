class Bank:
    def __init__(self,name,age,amount):
        self.name=name
        self.age=age
        self.__balance=amount   #Used Encapsulation
    def check_balance(self):
        return self.__balance
    def withdraw(self,amount):
        if amount>self.__balance:
            print('Withdrawal not possible')
        else:
            self.__balance=self.__balance-amount
    def deposit(self,amount):
        self.__balance=self.__balance+amount
a1=Bank('Pramit',20,1000)
a1.deposit(1000)
a1.withdraw(1)
print(a1.check_balance())