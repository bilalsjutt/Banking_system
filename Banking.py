import random

class Bank:
    def __init__(self):
        self.accounts = {}
        self.transactions = {}

    def create_account(self, account_holder, initial_balance):
        account_number = self.generate_account_number()
        account = BankAccount(account_number, account_holder, initial_balance)
        self.accounts[account_number] = account
        self.transactions[account_number] = []
        return account  # Return the created account

    def generate_account_number(self):
        return "".join(random.choice("0123456789") for _ in range(8))

    def get_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account
        else:
            print("Account not found!")
            return None

    def perform_transaction(self, account_number, transaction_type, amount):
        account = self.accounts.get(account_number)
        if not account:
            return "Account not found"
        if transaction_type == "deposit":
            account.deposit(amount)
        elif transaction_type == "withdraw":
            account.withdraw(amount)
        else:
            return "Invalid transaction type"
        self.transactions[account_number].append((transaction_type, amount))
        return "Transaction Successful"

    def get_transaction_history(self, account_number):  # Corrected method name
        return self.transactions.get(account_number, [])

class BankAccount:  # Corrected class name
    def __init__(self, account_number, account_holder, initial_balance):  # Corrected parameter name
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print(f"Withdrawal amount must be between 0 and {self.balance}")

    def get_balance(self):
        return self.balance

def main():
    bank = Bank()

    while True:
        print("\nPython Banking System")
        print("1. Create Account")
        print("2. Perform Transaction")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_holder = input("Enter your name: ")
            initial_balance = float(input("Enter initial balance: "))
            account = bank.create_account(account_holder, initial_balance)
            print(f"Account created successfully. Account Number: {account.account_number}")

        elif choice == "2":
            account_number = input("Enter account number: ")
            transaction_type = input("Enter transaction type (deposit/withdraw): ").lower()
            amount = float(input("Enter transaction amount: "))
            result = bank.perform_transaction(account_number, transaction_type, amount)
            print(result)

        elif choice == "3":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                print(f"Account Balance: ${account.get_balance()}")
            else:
                print("Account not found.")

        elif choice == "4":
            account_number = input("Enter account number: ")
            transactions = bank.get_transaction_history(account_number)  # Corrected method name
            if transactions is not None:
                print("Transaction History:")
                for trans_type, amount in transactions:
                    print(f"{trans_type.capitalize()}: ${amount}")
            else:
                print("Account not found or no transaction history.")

        elif choice == "5":
            print("Exiting the Python Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()