from TransactionHistory import TransactionHistory
class Account:
    def __init__(self, name, account_no, pin, balance=0):
        self.name = name
        self.account_no = account_no
        self.pin = pin
        self.balance = balance
        self.transaction_history = TransactionHistory()

    def authenticate(self, name, account_no, pin):
        return name == self.name and self.account_no and pin == self.pin