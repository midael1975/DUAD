"""
Collection of basic Python functions.
Each function is simple, clear, and designed to be easily testable.
"""

# ---------------------------------------------------------
# Exercise 3 — Add two numbers
# ---------------------------------------------------------
def add(a, b):
    """Return the sum of two numbers."""
    return a + b


# ---------------------------------------------------------
# Exercise 4 — Check if a number is even
# ---------------------------------------------------------
def is_even(n):
    """Return True if the number is even, otherwise False."""
    return n % 2 == 0


# ---------------------------------------------------------
# Exercise 5 — Return the largest of three numbers
# ---------------------------------------------------------
def max_of_three(a, b, c):
    """Return the largest of three numbers."""
    return max(a, b, c)


# ---------------------------------------------------------
# Exercise 6 — Reverse a string
# ---------------------------------------------------------
def reverse_string(text):
    """Return the reversed version of the string."""
    return text[::-1]


# ---------------------------------------------------------
# Exercise 7 — Count vowels in a string
# ---------------------------------------------------------
def count_vowels(text):
    """Return the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for c in text if c in vowels)


# ---------------------------------------------------------
# Exercise 8 — Calculate factorial
# ---------------------------------------------------------
def factorial(n):
    """
    Calculate the factorial of a non‑negative integer.
    0! = 1
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# ---------------------------------------------------------
# Exercise 9 — Check if a string is a palindrome
# ---------------------------------------------------------
def is_palindrome(text):
    """
    Return True if the text is a palindrome.
    Spaces and uppercase letters are ignored.
    """
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


# ---------------------------------------------------------
# Exercise 10 — Calculate the average of a list
# ---------------------------------------------------------
def average(numbers):
    """Return the average of a list of numbers."""
    if len(numbers) == 0:
        raise ValueError("The list cannot be empty.")
    return sum(numbers) / len(numbers)
