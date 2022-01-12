class User:
    def __init__(self,name,balance:int):
        self.user_name= name
        self.account_balance= int(balance)

    def make_deposit(self,amount):
        self.account_balance += amount
        print(f"{amount}$ is deposited to your account. Your Current balance is {self.account_balance}")

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        print(f"{amount}$ is withdrawn from your account. Your Current balance is {self.account_balance}")

    def display_user_balance(self):
        print(f"{self.user_name} has a balance of {self.account_balance}")

    def transfer_money(self, amount, user):
        print(f"{user.user_name} has a balance of {user.account_balance}")
        self.account_balance -= amount
        user.account_balance += amount
        print(f"{self.user_name} has transferred {amount}$ to {user.user_name}")
        print(f"{user.user_name} has a balance of {user.account_balance}")


user1 = User('Geetha',100000)
user2 = User('Pranav',100000)
print('You can perform following operations \n 1. Check Accounr Balance \n 2. Deposit Amount to account \n 3. Withdraw cash \n 4. Transfer Money to another account')
user_choice=int(input('Enter your choice'))
if(user_choice == 1):
    user1.display_user_balance()
if (user_choice == 2):
    amount_to_deposit = int(input("Enter the amount:"))   
    user1.make_deposit(amount_to_deposit)
if (user_choice == 3):
    amount_to_withdraw = int(input("Enter the amount:"))   
    user1.make_withdrawal(amount_to_withdraw)
if (user_choice == 4):
    amount_to_transfer = int(input("Enter the amount:"))  
    user1.transfer_money(amount_to_transfer,user2)


