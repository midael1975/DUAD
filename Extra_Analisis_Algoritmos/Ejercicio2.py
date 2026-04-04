def linear_search(my_list, target):
    for item in my_list:
        if item == target:
            return True
    return False
# Example usage
my_list = [1, 2, 3, 4, 5]
target = 3
resultado = linear_search(my_list, target)
print(f"The target {target} is in the list: {resultado}")

# Code Analysis:
# The function linear_search takes a list and a target value as input and performs a linear search
# to determine if the target is present in the list.
# In the worst case, the function will iterate through all elements of the list,
# making it have a time complexity of O(n), where n is the number of elements in the list.
# The space complexity of this function is O(1) because it uses a constant amount of space to store
# the loop variable and the return value, regardless of the input size.

def binary_search(my_list, target):
    left, right = 0, len(my_list) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
# Example usage
my_list = [1, 2, 3, 4, 5]
target = 3
resultado = binary_search(my_list, target)
print(f"The target {target} is in the list: {resultado}")

# Code Analysis:
# The function binary_search takes a sorted list and a target value as input and performs a binary search
# to determine if the target is present in the list.
# In the worst case, the function will iterate through half of the elements of the list,
# making it have a time complexity of O(log n), where n is the number of elements in the list.
# The space complexity of this function is O(1) because it uses a constant amount of space to store
# the loop variables and the return value, regardless of the input size.

# Questions:
# What is the complexity of each algorithm?
# Under what conditions is it appropriate to use each one?
# What happens if the list is not sorted?
# Answer:
# The linear search algorithm has a time complexity of O(n) and is appropriate to use when the list is unsorted
# or when the list is small. It is a simple and straightforward algorithm that does not require any additional data
# structures or sorting.
# The binary search algorithm has a time complexity of O(log n) and is appropriate to use when the list is sorted.
# It is more efficient than linear search for large sorted lists, as it reduces the number of comparisons needed
# to find the target value.
# If the list is not sorted, the binary search algorithm will not work correctly,
# as it relies on the order of the elements to determine which half of the list to search next.
# In such cases, it may return incorrect results or fail to find the target value even if it is present in the list.
# Therefore, it is crucial to ensure that the list is sorted before using binary search.

