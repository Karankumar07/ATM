class Deposit:
    def __init__(self, account):
        self.account = account

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount."
        self.account.balance += amount
        self.account.transaction_history.add_transaction(f"Deposited ${amount}")
        return f"Deposited ${amount}"