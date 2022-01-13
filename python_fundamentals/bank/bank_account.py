class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, balance:float=2500, int_rate:float=1.5): 
        self.interest_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self 

    def display_account_info(self):
        print(f"Balance is: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance>0:
            interest = self.balance*self.interest_rate
            self.balance += interest
            return self
        else:
            print("Your account has negative balance. Cannot yeild interest")

    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) <0:
            return False
        else:
            return True

account1=BankAccount(25000,3.5)
account2=BankAccount(35000,5.5)

account1.deposit(1000).deposit(5000).deposit(300).withdraw(2000).withdraw(300).withdraw(700).withdraw(1000).yield_interest().display_account_info()
