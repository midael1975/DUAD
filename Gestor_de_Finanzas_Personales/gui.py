import FreeSimpleGUI as sg
from logic import FinanceManager
from persistence import save_data, load_data

def create_main_window():
    """
    Builds the main window layout.
    """
    headings = ["Date", "Title", "Amount", "Category", "Type"]
    
    layout = [
        [sg.Text("Personal Finance Manager", font=("Helvetica", 16, "bold"), justification="center", expand_x=True)],
        [sg.Table(values=[], headings=headings, max_col_width=25,
                  auto_size_columns=True, display_row_numbers=False,
                  justification='center', num_rows=10, key='-TABLE-',
                  row_height=30, expand_x=True)],
        [sg.Button("Add Category"), sg.Button("Add Income"), sg.Button("Add Expense"), sg.Button("Exit")]
    ]

    # finalize=True is required so we can update the table immediately after creating the window
    return sg.Window("Finance Manager", layout, size=(600, 400), finalize=True)

def open_category_window():
    """
    Creates and handles the secondary window to add a new category.
    """
    layout = [
        [sg.Text("Category Name:"), sg.InputText(key="-CAT_NAME-")],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]
    return sg.Window("New Category", layout, modal=True)

def open_transaction_window(transaction_type, category_names):
    """
    Creates and handles the secondary window for both Incomes and Expenses.
    """
    layout = [
        [sg.Text("Title:"), sg.InputText(key="-TITLE-")],
        [sg.Text("Amount:"), sg.InputText(key="-AMOUNT-")],
        [sg.Text("Category:"), sg.Combo(category_names, key="-CATEGORY-", readonly=True, size=(20, 1))],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]
    return sg.Window(f"Add {transaction_type}", layout, modal=True)

def refresh_table(window, manager):
    """
    Extracts transactions from the manager and updates the GUI table.
    """
    table_data = []
    for tx in manager.transactions:
        # We format each row as a list to match the table headings
        row = [tx.date, tx.title, f"${tx.amount:.2f}", str(tx.category), tx.transaction_type]
        table_data.append(row)
    
    # Update the table element with the new data
    window['-TABLE-'].update(values=table_data)

def run_app():
    """
    Main application logic and event loop.
    """
    # 1. Initialize the Brain and Memory
    manager = FinanceManager()
    load_data(manager) # Load existing data if any

    # 2. Create Main Window
    window = create_main_window()
    refresh_table(window, manager) # Show loaded data immediately

    # 3. Main Event Loop
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            break
            
        elif event == "Add Category":
            cat_window = open_category_window()
            cat_event, cat_values = cat_window.read()
            
            if cat_event == "Save":
                new_name = cat_values["-CAT_NAME-"]
                if manager.add_category(new_name):
                    save_data(manager) # Save automatically
                    sg.popup(f"Category '{new_name}' added successfully!")
                else:
                    sg.popup_error("Category name cannot be empty.")
                    
            cat_window.close()
            
        elif event in ["Add Income", "Add Expense"]:
            # Check mandatory rubric validation: Must have categories first
            if not manager.categories:
                sg.popup_error("Error: You must add at least one category first.")
                continue

            # Get the type of transaction based on the button pressed
            tx_type = "Income" if event == "Add Income" else "Expense"
            
            # Get a list of category names (strings) for the dropdown menu
            category_names = [cat.name for cat in manager.categories]
            
            tx_window = open_transaction_window(tx_type, category_names)
            tx_event, tx_values = tx_window.read()
            
            if tx_event == "Save":
                title = tx_values["-TITLE-"]
                amount_str = tx_values["-AMOUNT-"]
                selected_cat = tx_values["-CATEGORY-"]
                
                # Basic validation
                if not title or not amount_str or not selected_cat:
                    sg.popup_error("Please fill all fields.")
                else:
                    try:
                        # Try to convert amount to a float and add the transaction
                        # For expenses, we could multiply by -1, but let's keep it simple for now
                        amount = float(amount_str) 
                        if tx_type == "Expense" and amount > 0:
                            amount = -amount # Ensure expenses are negative in logic
                            
                        manager.add_transaction(title, amount, selected_cat, tx_type)
                        save_data(manager) # Save automatically
                        refresh_table(window, manager) # Update the view
                        
                    except ValueError:
                        sg.popup_error("Amount must be a valid number.")
                        
            tx_window.close()

    window.close()

if __name__ == "__main__":
    run_app()