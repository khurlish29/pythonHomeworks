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
            print(f"Deposited {amount} to {self.account_number}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.account_number}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount.")

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
        print(f"Account created successfully! Account Number: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}\nName: {account.name}\nBalance: {account.balance}")
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
        with open("accounts.txt", "w") as file:
            json.dump({acc: vars(self.accounts[acc]) for acc in self.accounts}, file)

    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as file:
                data = json.load(file)
                self.accounts = {acc: Account(**data[acc]) for acc in data}
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {}
