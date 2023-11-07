class BankAccount:
    # Class variable to keep track of all bank accounts created
    accounts = []

    def __init__(self, int_rate, balance):
        # Initializing a Bank_Account
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)  # Add the account to the list of all accounts

    def deposit(self, amount):
        # Deposit money into the account
        self.balance += amount
        return self

    def withdraw(self, amount):
        # Method to withdraw money from the account
        if (self.balance - amount) >= 0:
            self.balance -= amount  # Decrease the account balance by the withdrawal amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5  # Charge a $5 fee for insufficient funds
        return self

    def display_account_info(self):
        # Method to display the account's current balance
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        # Method to calculate and add interest to the account balance
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)  # Calculate and add interest
        return self

    @classmethod
    def print_all_accounts(aac):
        # Class method to print information for all created accounts
        for account in aac.accounts:
            account.display_account_info()

#--------------------------------User_bank_account assignment ----------------------------------------

class User:
    # Initialize a User object with a name and two bank accounts (checking and savings).
    def __init__(self, name):
        self.name = name
        self.account = {
            "checking": BankAccount(0.02, 1300),
            "savings": BankAccount(0.05, 2500)
        }

    # Method to display the user's account balances.
    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

    # Method to transfer money from the user's account to another user's account.
    def transfer_money(self, amount, user):
        self.account['checking'].withdraw(amount)
        user.account['checking'].deposit(amount)
        
        # Display updated account balances for both users.
        self.display_user_balance()
        user.display_user_balance()
        return self

# Create a User object named 'Abdelkader'.
Abdelkader = User("Abdelkader")

# Deposit $100 into Abdelkader's checking account.
Abdelkader.account['checking'].deposit(100)

# Display the updated account balances for Abdelkader.
Abdelkader.display_user_balance()