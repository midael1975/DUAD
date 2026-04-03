def print_numbers_times_2(numbers_list):
	for number in numbers_list:
		print(number * 2)
# Code Analysis:
# The function iterates through each element in the input list, If the list has 5 elements, the loop makes 5 turns.
# If the list has n elements, the loop makes n turns.
# performing a constant time operation(multiplying by 2 and printing) for each element.
# Both are constant operations. It doesn't matter if the number is "2" or "1000",
# the computer takes practically the same amount of time to process it. This is represented as O(1).
# n (turns) X O(1) (constant operation) = O(n)
# The time complexity of this function is O(n), where n is the number of elements in the input list.
