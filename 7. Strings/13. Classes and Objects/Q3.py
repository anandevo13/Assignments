"""
Q. Defina a class Account with static variable rate_of_interest, instance variables balance and account 
number. Make functions to set values in instance object of account, show balance, show rate of interest, 
withdraw and deposit.
"""

class account:
    def __init__(self):
        self.account = float(input("Enter the account number: "))
        self.money = float(input("Enter the amount deposited: "))
        self.roi = float(input("Enter the roi: "))
        
    def deposit(self):
        self.amount = float(input("Enter the amount deposited: "))
        self.amount += self.money
        print("\n Amount deposited: ",self.amount)
        
    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.amount >= amount:
            self.amount -= amount
            print("\n Net available balance= ", self.amount)
        else:
            print("Insufficient balance")
            
    def display(self):
        print("\n Net Available balance= ", self.amount*self.roi)        
            
            
s = account()
s.deposit()
s.withdraw()
s.display()            
            
                
            