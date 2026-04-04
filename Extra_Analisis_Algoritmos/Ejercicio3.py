def print_all_pairs(my_dict):
    for key1 in my_dict:
        for key2 in my_dict:
            print(f"{key1}-{key2}")

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 3}
print_all_pairs(my_dict)

# Code Analysis:
# The function print_all_pairs takes a dictionary as input and prints all possible pairs of keys in the dictionary.
# The outer loop iterates through each key in the dictionary, and for each key,
# the inner loop also iterates through each key in the dictionary, resulting in a total of n * n iterations,
# where n is the number of keys in the dictionary.
# Therefore, the time complexity of this function is O(n^2) because the number of operations grows quadratically
# with the number of keys in the dictionary.
# The space complexity of this function is O(1) because it uses a constant amount of space to store
# the loop variables and the print statement, regardless of the input size.

# Questions:
# What is the time complexity?
# How long does it take if there are 1 million keys?
# Answer:
# The time complexity is O(n^2), so with 1 million keys, it would take approximately 1 trillion operations.
# This is because the number of pairs would be 1 million * 1 million = 1 trillion.
