import json
import random

class Account:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = str(random.randint(10000, 99999))
        while account_number in self.accounts:
            account_number = str(random.randint(10000, 99999))

        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        print(f"Account created successfully. Account Number: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print("\nAccount Details:")
            print(f"Account Number: {account.account_number}")
            print(f"Name: {account.name}")
            print(f"Balance: {account.balance}\n")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def save_to_file(self):
        with open("accounts.json", "w") as file:
            json.dump({acc: vars(self.accounts[acc]) for acc in self.accounts}, file, indent=4)

    def load_from_file(self):
        try:
            with open("accounts.json", "r") as file:
                data = json.load(file)
                self.accounts = {acc: Account(**data[acc]) for acc in data}
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {}

def main():
    bank = Bank()

    while True:
        print("\nBank System")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            bank.create_account(name, initial_deposit)

        elif choice == "2":
            acc_num = input("Enter your account number: ")
            bank.view_account(acc_num)

        elif choice == "3":
            acc_num = input("Enter your account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(acc_num, amount)

        elif choice == "4":
            acc_num = input("Enter your account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(acc_num, amount)

        elif choice == "5":
            print("Exiting... Thank you for using the bank system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
