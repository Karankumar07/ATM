class TransactionHistory:
    def __init__(self):
        self.history = []

    def add_transaction(self, transaction):
        self.history.append(transaction)

    def display_history(self):
        print("\nTransaction History:")
        for transaction in self.history:
            print(transaction)