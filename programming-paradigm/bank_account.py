class BankAccount:
    def __init__(self,account_balance):
        self.account_balance = account_balance

    def deposit(self, amount):
        if float(amount) > 0:
            self.account_balance += amount
        else:
            return f"unable to deposit amount"

    def withdraw(self, amount):
        if 0 < self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${float(self.account_balance):.2f}")