import unittest
def divide(number1, number2):
    """Divide two numbers."""
    if number2 == 0:
        raise ValueError("Cannot divide by zero.")
    return number1 / number2

class TestDivide(unittest.TestCase):
    def test_divide_normal(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)
    
    def test_divide_string(self):
        with self.assertRaises(TypeError):
            divide("10", 2)


if __name__ == '__main__':
    unittest.main()