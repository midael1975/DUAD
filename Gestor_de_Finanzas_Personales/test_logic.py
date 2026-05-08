import unittest
from logic import Category, Transaction, FinanceManager

class TestFinanceManager(unittest.TestCase):

    def setUp(self):
        # This function runs BEFORE each test.
        # It provides a clean, empty "FinanceManager" for each test.
        self.manager = FinanceManager()

    # Test 1: Verify that a valid category can be added
    def test_add_valid_category(self):
        result = self.manager.add_category("Food")
        self.assertTrue(result)
        self.assertEqual(len(self.manager.categories), 1)
        self.assertEqual(self.manager.categories[0].name, "Food")

    # Test 2: Verify that empty categories or categories with only spaces are NOT added
    def test_add_empty_category(self):
        result = self.manager.add_category("   ")
        self.assertFalse(result)
        self.assertEqual(len(self.manager.categories), 0)

    # Test 3: Verify that the text representation (str) of Category works
    def test_category_str(self):
        cat = Category("Transport")
        self.assertEqual(str(cat), "Transport")

    # Test 4: Verify that a transaction is added if categories are available
    def test_add_transaction_success(self):
        self.manager.add_category("Salary")
        result = self.manager.add_transaction("April Salary", 1500, "Salary", "Income")
        self.assertTrue(result)
        self.assertEqual(len(self.manager.transactions), 1)
        self.assertEqual(self.manager.transactions[0].title, "April Salary")

    # Test 5: Verify that it raises an ERROR if trying to add a transaction without categories
    def test_add_transaction_no_categories(self):
        # with self.assertRaises verifies that the error occurs correctly
        with self.assertRaises(ValueError):
            self.manager.add_transaction("Groceries", 50, "Food", "Expense")

    # Test 6: Verify that the amount is always saved as a decimal (float)
    def test_transaction_amount_is_float(self):
        self.manager.add_category("Entertainment")
        # We pass the number as a string (str) to see if the class converts it to float
        self.manager.add_transaction("Movies", "25.50", "Entertainment", "Expense")
        self.assertIsInstance(self.manager.transactions[0].amount, float)
        self.assertEqual(self.manager.transactions[0].amount, 25.50)

    # Test 7: Verify the text representation (str) of Transaction
    def test_transaction_str_format(self):
        self.manager.add_category("Food")
        self.manager.add_transaction("Pizza", 15, "Food", "Expense")
        transaction = self.manager.transactions[0]
        tx_string = str(transaction)

        # We verify that the text contains the key data
        self.assertIn("Pizza", tx_string)
        self.assertIn("$15.0", tx_string)
        self.assertIn("Expense", tx_string)

    # Test 8: Verify that the system handles multiple entries correctly
    def test_multiple_entries(self):
        self.manager.add_category("Food")
        self.manager.add_category("Utilities")
        self.manager.add_transaction("Burger", 10, "Food", "Expense")
        self.manager.add_transaction("Internet", 60, "Utilities", "Expense")

        self.assertEqual(len(self.manager.categories), 2)
        self.assertEqual(len(self.manager.transactions), 2)

if __name__ == '__main__':
    unittest.main()