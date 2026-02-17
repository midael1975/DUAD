class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive.")
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        except ValueError as e:
            print(e)

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if amount > self.balance:
                raise ValueError("Insufficient funds.")
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        except ValueError as e:
            print(e)

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, min_balance):
        super().__init__(account_number, account_holder, balance)
        self.min_balance = min_balance
    
    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")

            if self.balance - amount < self.min_balance:
                raise ValueError("Withdrawal denied: minimum balance would be exceeded.")

            # If validation passes, call the parent method
            super().withdraw(amount)

        except ValueError as e:
            print(e)

# Example usage
account = BankAccount("123456789", "Wilker Pacheco", 1000)
account.deposit(500)
account.withdraw(200)

savings = SavingsAccount("987654321", "Wilker", 2000, 500)

print(f"Account holder: {savings.account_holder}")
print(f"Account number: {savings.account_number}")
print(f"Current balance: {savings.get_balance()}")

savings.withdraw(1700)  # NOT allowed
savings.withdraw(1200)  # Allowed


# class BankAccount:
#     def __init__(self, account_number, account_holder, initial_balance=0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = initial_balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited: {amount}. New balance: {self.balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#                 print(f"Withdrew: {amount}. New balance: {self.balance}")
#             else:
#                 print("Insufficient funds.")
#         else:
#             print("Withdrawal amount must be positive.")

#     def get_balance(self):
#         return self.balance


# class SavingsAccount(BankAccount):
#     def __init__(self, account_number, account_holder, balance, min_balance):
#         super().__init__(account_number, account_holder, balance)
#         self.min_balance = min_balance
    
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Withdrawal amount must be positive.")
#             return
        
#         if self.balance - amount < self.min_balance:
#             print("Withdrawal denied: minimum balance would be exceeded.")
#             return
        
#         # Si pasa la validación, usa el método original
#         super().withdraw(amount)


# # Example usage
# account = BankAccount("123456789", "John Doe", 1000)
# account.deposit(500)
# account.withdraw(200)

# savings = SavingsAccount("987654321", "Jane Doe", 2000, 500)

# print(f"Account holder: {savings.account_holder}")
# print(f"Account number: {savings.account_number}")
# print(f"Current balance: {savings.get_balance()}")

# savings.withdraw(1700)  # NO permitido
# savings.withdraw(1200)  # Sí permitido