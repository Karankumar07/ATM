class Withdraw:
    def __init__(self, account):
        self.account = account

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount."
        if amount > self.account.balance:
            return "Insufficient funds."
        self.account.balance -= amount
        self.account.transaction_history.add_transaction(f"Withdrawn ${amount}")
        return f"Withdrew ${amount}"