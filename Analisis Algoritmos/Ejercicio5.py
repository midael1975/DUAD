def generate_list_trios(list_a, list_b, list_c):
	result_list = []
	for element_a in list_a:
		for element_b in list_b:
			for element_c in list_c:
				result_list.append(f'{element_a} {element_b} {element_c}')

	return result_list
# Code Analysis:
# The function uses three nested loops to generate combinations of elements from three input lists.
# If list_a has m elements, list_b has n elements, and list_c has p elements, the outer loop runs m times,
# the middle loop runs n times for each iteration of the outer loop, and the inner loop runs p times for each
# iteration of the middle loop.
# Therefore, the total number of iterations is m * n * p.
# The time complexity of this function is O(m * n * p), where m, n, and p are the lengths of the input lists.
# In the worst case, when all combinations are generated, the function will have to iterate through all possible
# combinations,
# resulting in O(m * n * p) time complexity.
# If the lists are of equal length, say n, then the time complexity can be expressed as O(n^3).