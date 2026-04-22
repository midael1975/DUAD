def manual_add(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result
# Example usage
n = 5
resultado = manual_add(n)
print(f"The sum of integers from 1 to {n} is: {resultado}")

# Code Analysis:
# The function manual_add takes an integer n as input and calculates the sum of integers from 1 to n
# using a for loop. The loop iterates n times, and in each iteration,
# it performs a constant time operation (adding the current integer to the result).
# Therefore, the time complexity of this function is O(n) because the number of operations grows linearly
# with the input size n.
# The space complexity of this function is O(1) because it uses a constant amount of space to store the result
# and the loop variable, regardless of the input size n.

def formula_add(n):
    return n * (n + 1) // 2
# Example usage
n = 5
resultado = formula_add(n)
print(f"The sum of integers from 1 to {n} is: {resultado}")

# Code Analysis:
# The function formula_add calculates the sum of integers from 1 to n using the formula n(n + 1) / 2.
# This formula allows us to compute the sum in constant time, O(1),
# because it performs a fixed number of operations regardless of the input size n.
# The space complexity of this function is also O(1) because it uses a constant amount of space to store the result
# and the input variable n, regardless of the input size.

# Questions:
# Which version would you use if number = 1,000,000,000? Why?
# Answer:I would use the formula_add version if the number is 1,000,000,000 because it has a time complexity of O(1),
# meaning it will compute the result in constant time regardless of the input size.
# In contrast, the manual_add version has a time complexity of O(n),
# which means it would require 1,000,000,000 iterations to compute the sum,
# making it inefficient and impractical for such a large input.
# The formula_add version is much more efficient and suitable for large values of n.
