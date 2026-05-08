import json
import os
from logic import Transaction

# Default file name for our database
DATA_FILE = "finance_data.json"

def save_data(manager, filename=DATA_FILE):
    """
    Saves the data from FinanceManager into a JSON file.
    """
    # We create a base dictionary to hold our structured data
    data = {
        "categories": [],
        "transactions": []
    }

    # Step A: Convert Category objects to simple strings
    for cat in manager.categories:
        data["categories"].append(cat.name)
    data["categories"] = [cat.name for cat in manager.categories]

    # Step B: Convert Transaction objects to simple dictionaries
    for tx in manager.transactions:
        transaction_dict = {
            "title": tx.title,
            "amount": tx.amount,
            "category": tx.category,
            "transaction_type": tx.transaction_type,
            "date": tx.date
        }
        data["transactions"].append(transaction_dict)

    # Step C: Write the dictionary to a JSON file
    # 'w' means write mode. It will overwrite the file if it exists.
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
        
    return True

def load_data(manager, filename=DATA_FILE):
    """
    Loads data from a JSON file into the FinanceManager.
    """
    # Step A: Check if the file exists before trying to read it
    if not os.path.exists(filename):
        return False # No data to load

    # Step B: Open and read the JSON file
    # 'r' means read mode.
    with open(filename, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            # If the file is empty or corrupted, we stop the loading process
            return False 

    # Step C: Restore the categories
    manager.categories = [] # Clear any existing data first
    for cat_name in data.get("categories", []):
        manager.add_category(cat_name)

    # Step D: Restore the transactions
    manager.transactions = [] # Clear any existing data first
    for tx_data in data.get("transactions", []):
        
        # We create a new Transaction object with the saved basic data
        new_tx = Transaction(
            title=tx_data["title"],
            amount=tx_data["amount"],
            category=tx_data["category"],
            transaction_type=tx_data["transaction_type"]
        )
        
        # We override the default date with the saved date from the file
        if "date" in tx_data:
            new_tx.date = tx_data["date"]
            
        # Add the restored transaction to the manager's list
        manager.transactions.append(new_tx)

    return True # Data loaded successfully