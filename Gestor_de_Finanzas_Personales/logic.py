from datetime import datetime

class Category:
    def __init__(self, name):
        self.name = name
        # self.color = None

    def __str__(self):
        return self.name

class Transaction:
    def __init__(self, title, amount, category, transaction_type):
        self.title = title
        self.amount = float(amount)
        self.category = category
        self.transaction_type = transaction_type
        self.date = datetime.now().strftime("%d/%m/%Y")

    def __str__(self):
        return f"{self.date} | {self.title} | ${self.amount} | {self.transaction_type}"

class FinanceManager:
    def __init__(self):
        self.categories = []
        self.transactions = []

    def add_category(self, category_name):
        if category_name.strip():
            new_category = Category(category_name)
            self.categories.append(new_category)
            return True
        return False

    def add_transaction(self, title, amount, category, transaction_type):
        if not self.categories:
            raise ValueError("Cannot add a transaction without available categories.")

        new_transaction = Transaction(title, amount, category, transaction_type)
        self.transactions.append(new_transaction)
        return True