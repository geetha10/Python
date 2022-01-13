from bank_account import BankAccount

class User:
    def __init__(self,name,email,balance:float):
        self.user_name= name
        self.email=email
        self.account=[BankAccount(balance,2.5)]

    def make_deposit(self,amount):
        selected_account=int(input(f"""User has {len(self.account)} accounts: 
        Specify the account to which you want to deposit the amount"""))
        self.account[selected_account-1].balance += amount
        print(f"{amount}$ is deposited to your account. Your Current balance is {self.account[selected_account-1].balance}")
        return self

    def make_withdrawal(self,amount):
        selected_account=int(input(f"""User has {len(self.account)} accounts: 
        Specify the account to which you want to withdraw the amount"""))
        self.account[selected_account-1].balance -= amount
        print(f"{amount}$ is withdrawn from your account. Your Current balance is {self.account[selected_account-1].balance}")
        return self

    def display_user_balance(self):
        print(f"{self.user_name} has {len(self.account)} accounts")
        [print(f"Account {i+1} has {self.account[i].balance}") for i in range(len(self.account))]
        return self

    def transfer_money(self, amount, user):
        print(f"{user.user_name} has a balance of {user.account.balance}")
        selected_account=int(input(f"""User has {len(self.account)} accounts: 
        Specify the account from which you want to transfer the amount"""))
        transfer_to_account=int(input(f"""User has {len(user.account)} accounts: 
        Specify the account to which you want to transfer the amount"""))
        self.account[selected_account-1].balance -= amount
        user.account[transfer_to_account-1].balance += amount
        print(f"{self.user_name} has transferred {amount}$ to {user.user_name}")
        print(f"{user.user_name} has a balance of {user.account.balance}")
        return self

    def open_bank_account(self,amount):
        self.account.append(BankAccount(amount,2.5))

user1 = User('Geetha','hrzd@gmail.com',100000)

user2 = User('Pranav','dfvjdfk@gmail.com',100000)


# additional excercise for practice
while(True):
    perform_transaction = input("Enter yes if you want to perform one more transactio else enter no:\n1. Yes \n2: No")
    if(perform_transaction in ["yes","Yes","Y",'y']):
        print("""You can perform following operations \n 
        1. Check Account Balance \n 
        2. Deposit Amount to account \n 
        3. Withdraw cash \n 
        4. Transfer Money to another account \n 
        5. Open another bank account""")
        user_choice=int(input('Enter your choice'))
        if(user_choice == 1):
            user1.display_user_balance()
        if (user_choice == 2):
            amount_to_deposit = float(input("Enter the amount:"))   
            user1.make_deposit(amount_to_deposit)
        if (user_choice == 3):
            amount_to_withdraw = float(input("Enter the amount:"))   
            user1.make_withdrawal(amount_to_withdraw)
        if (user_choice == 4):
            amount_to_transfer = float(input("Enter the amount:"))  
            user1.transfer_money(amount_to_transfer,user2)
        if (user_choice == 5):
            user1.open_bank_account(2000)
    else:
        print("Thanks for Visiting bank, Have a good day")
        break



# print('You can perform following operations \n '
# +'1. Check Account Balance \n'
# +' 2. Deposit Amount to account \n'
# +' 3. Withdraw cash \n'
# +' 4. Transfer Money to another account')

