def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)):
		print(list_to_print[index])
# Code Analysis:
# The function calculates the length of the input list and then uses a loop to print elements.
# The loop runs for a number of iterations equal to the smaller of the list length and 10.
# If the list has 10 or fewer elements, the loop will run for each element in the list,
# resulting in O(n) time complexity, where n is the number of elements in the list.
# If the list has more than 10 elements, the loop will run for a fixed number of iterations (10),
# resulting in O(1) time complexity.
# Therefore, the overall time complexity of this function is O(min(n, 10)),
# which simplifies to O(n) for lists of 10 or fewer elements and O(1) for lists of more than 10 elements.
# In Big O, if the time does not depend on the size of the input, it is always O(1).