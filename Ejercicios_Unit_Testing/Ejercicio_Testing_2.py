import unittest

# Import all functions from your main file
from functions import (
    add,
    is_even,
    max_of_three,
    reverse_string,
    count_vowels,
    factorial,
    is_palindrome,
    average
)

# ------------------------------
# Exercise 3 — add(a, b)
# ------------------------------
class TestExercise3(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 7), 12)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-3, -8), -11)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-4, 10), 6)


# ------------------------------
# Exercise 4 — is_even(n)
# ------------------------------
class TestExercise4(unittest.TestCase):

    def test_even_number(self):
        self.assertTrue(is_even(8))

    def test_odd_number(self):
        self.assertFalse(is_even(7))

    def test_zero_is_even(self):
        self.assertTrue(is_even(0))


# ------------------------------
# Exercise 5 — max_of_three(a, b, c)
# ------------------------------
class TestExercise5(unittest.TestCase):

    def test_max_at_start(self):
        self.assertEqual(max_of_three(9, 3, 1), 9)

    def test_max_in_middle(self):
        self.assertEqual(max_of_three(2, 10, 5), 10)

    def test_max_at_end(self):
        self.assertEqual(max_of_three(4, 7, 20), 20)


# ------------------------------
# Exercise 6 — reverse_string(text)
# ------------------------------
class TestExercise6(unittest.TestCase):

    def test_simple_word(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_word_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")


# ------------------------------
# Exercise 7 — count_vowels(text)
# ------------------------------
class TestExercise7(unittest.TestCase):

    def test_only_vowels(self):
        self.assertEqual(count_vowels("aeiou"), 5)

    def test_mixed_text(self):
        self.assertEqual(count_vowels("Hello World"), 3)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("rhythm"), 0)


# ------------------------------
# Exercise 8 — factorial(n)
# ------------------------------
class TestExercise8(unittest.TestCase):

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_small(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_larger(self):
        self.assertEqual(factorial(7), 5040)


# ------------------------------
# Exercise 9 — is_palindrome(text)
# ------------------------------
class TestExercise9(unittest.TestCase):

    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("ana"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("anita lava la tina"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("python"))


# ------------------------------
# Exercise 10 — average(numbers)
# ------------------------------
class TestExercise10(unittest.TestCase):

    def test_average_integers(self):
        self.assertEqual(average([1, 2, 3]), 2)

    def test_average_decimals(self):
        self.assertAlmostEqual(average([1.5, 2.5, 3.5]), 2.5)

    def test_average_single_value(self):
        self.assertEqual(average([10]), 10)


# ------------------------------
# Run all tests
# ------------------------------
if __name__ == "__main__":
    unittest.main()
