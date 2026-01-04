
class  BankAccount: 
    def __init__ (self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance+amount
        print( f"{self.owner} deposited ${amount}. New balance: ${self.balance}")


my_account= BankAccount("Alice", 100)
my_account.deposit(50) 