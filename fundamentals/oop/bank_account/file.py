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

# Create two bank accounts
savings = BankAccount(.05, 500)
checking = BankAccount(.02, 2000)

# Perform operations on the savings account and checking account
savings.deposit(50).deposit(30).deposit(100).withdraw(700).yield_interest().display_account_info()
checking.deposit(600).deposit(100).deposit(50).withdraw(300).yield_interest().display_account_info()

# Print information for all accounts
BankAccount.print_all_accounts()