import unittest


# Functions to test
def add(a, b):
    """Add two numbers."""
    return a + b


def average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def celsius_to_fahrenheit(celsius):
    """Convert degrees Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


# Test class
class TestNumericOperations(unittest.TestCase):
    """Test suite for numeric operations."""
    
    # ===== Tests for the add function =====
    def test_add_positive_numbers(self):
        """Test add with positive numbers."""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(10, 20), 30)
        self.assertEqual(add(1, 1), 2)
    
    def test_add_negative_numbers(self):
        """Test add with negative numbers."""
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-10, -20), -30)
        self.assertEqual(add(-1, -1), -2)
    
    def test_add_with_zeros(self):
        """Test add with zeros."""
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, -3), -3)
    
    # ===== Tests for the average function =====
    def test_average_positive_numbers(self):
        """Test average with positive numbers."""
        self.assertEqual(average([2, 4, 6]), 4)
        self.assertEqual(average([10, 20, 30]), 20)
        self.assertEqual(average([5]), 5)
    
    def test_average_negative_numbers(self):
        """Test average with negative numbers."""
        self.assertEqual(average([-2, -4, -6]), -4)
        self.assertEqual(average([-10, -20, -30]), -20)
        self.assertEqual(average([-5]), -5)
    
    def test_average_with_zeros(self):
        """Test average with zeros."""
        self.assertEqual(average([0, 0, 0]), 0)
        self.assertEqual(average([0, 5, 10]), 5)
        self.assertEqual(average([]), 0)
    
    # ===== Tests for the celsius_to_fahrenheit function =====
    def test_celsius_to_fahrenheit_positive_numbers(self):
        """Test Celsius to Fahrenheit conversion with positive numbers."""
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6)
    
    def test_celsius_to_fahrenheit_negative_numbers(self):
        """Test Celsius to Fahrenheit conversion with negative numbers."""
        self.assertEqual(celsius_to_fahrenheit(-40), -40)
        self.assertEqual(celsius_to_fahrenheit(-10), 14)
        self.assertAlmostEqual(celsius_to_fahrenheit(-20), -4)
    
    def test_celsius_to_fahrenheit_with_zeros(self):
        """Test Celsius to Fahrenheit conversion with zero."""


if __name__ == '__main__':
    unittest.main()
