class Bank:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance= self.balance + amount
    def withdraw(self,amount):
        if amount>self.balance:
            print('Not enough money to withdraw')
        else:
           self.balance=self.balance-amount
           print(f'You withdrawn {amount} & remaining is {self.balance}')
    def balance_check(self):
        print(f"The balance in {self.name}'s account is: {self.balance}")
b1=Bank('Pramit')
b1.deposit(1000)
b1.deposit(2000)
b1.balance_check()



