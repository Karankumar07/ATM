class Transfer:
    def __init__(self, source_account, recipient_account):
        self.source_account = source_account
        self.recipient_account = recipient_account

    def transfer(self, amount):
        if amount <= 0:
            return "Invalid transfer amount."
        if amount > self.source_account.balance:
            return "Insufficient funds."
        self.source_account.balance -= amount
        self.recipient_account.balance += amount
        self.source_account.transaction_history.add_transaction(f"Transferred ${amount} to {self.recipient_account.account_no}")
        self.recipient_account.transaction_history.add_transaction(f"Received ${amount} from {self.source_account.account_no}")
        return f"Transferred ${amount} to {self.recipient_account.account_no}"