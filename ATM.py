from Account import Account
from TransactionHistory import TransactionHistory
from Withdraw import Withdraw
from Deposit import Deposit
from Transfer import Transfer
from Quit import Quit
class ATM:
    def __init__(self):
        self.accounts = {}
        self.current_account = None

    def create_account(self, name, account_no, pin):
        if account_no in self.accounts:
            return "Account No already exists. Please choose a different one."
        account = Account(name, account_no, pin)
        self.accounts[account_no] = account
        return "Account created successfully."

    def login(self, name, account_no, pin):
        if account_no in self.accounts:
            account = self.accounts[account_no]
            if account.authenticate(name, account_no, pin):
                self.current_account = account
                return "Login successful."
        return "Invalid name or Account No or PIN. Please try again."

    def logout(self):
        self.current_account = None

    def display_menu(self):
        print("\nATM Menu:")
        print("1. Display Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Quit")

    def run(self):
        while True:
            if not self.current_account:
                print("\nWelcome to the ATM!")
                name = input("Enter  your Name: ")
                account_no = input("Enter account No: ")
                pin = input("Enter PIN: ")
                login_result = self.login(name, account_no, pin)
                print(login_result)
                if login_result != "Login successful.":
                    continue

            self.display_menu()
            choice = input("Enter your choice (1/2/3/4/5/6): ")

            if choice == "1":
                print(f"Balance: ${self.current_account.balance}")
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: $"))
                withdrawal_handler = Withdraw(self.current_account)
                withdrawal_result = withdrawal_handler.withdraw(amount)
                print(withdrawal_result)
            elif choice == "3":
                amount = float(input("Enter deposit amount: $"))
                deposit_handler = Deposit(self.current_account)
                deposit_result = deposit_handler.deposit(amount)
                print(deposit_result)
            elif choice == "4":
                recipient_name = input("Enter recipient's name: ")
                recipient_id = input("Enter recipient's account No: ")
                amount = float(input("Enter transfer amount: $"))
                if recipient_id in self.accounts:
                    recipient = self.accounts[recipient_id]
                    transfer_handler = Transfer(self.current_account, recipient)
                    transfer_result = transfer_handler.transfer(amount)
                    print(transfer_result)
                else:
                    print("Recipient not found.")
            elif choice == "5":
                self.current_account.transaction_history.display_history()
            elif choice == "6":
                quit_handler = Quit(self)
                quit_handler.quit()
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    atm = ATM()
    while True:
        print("\nATM Main Menu:")
        print("1. Create Account")
        print("2. Login")
        print("3. Quit")
        main_choice = input("Enter your choice (1/2/3): ")

        if main_choice == "1":
            name = input("Enter your name: ")
            account_no = input("Enter a new Account No: ")
            pin = input("Enter a new PIN: ")
            create_result = atm.create_account(name,account_no, pin)
            print(create_result)
        elif main_choice == "2":
            atm.run()
        elif main_choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")