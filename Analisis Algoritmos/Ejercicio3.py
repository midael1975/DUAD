def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:
		for element_b in list_b:
			if element_a == element_b:
				return True

	return False

# Code Analysis:
# The function uses two nested loops to compare each element of list_a with each element of list_b.
# If list_a has m elements and list_b has n elements, the outer loop runs m times and for each iteration of the outer
# loop, the inner loop runs n times.
# Therefore, the total number of comparisons made is m * n.
# The time complexity of this function is O(m * n), where m and n are the lengths of the input lists.
# In the worst case, when there are no common elements between the two lists, the function will have to compare 
# every element of list_a with every element of list_b, resulting in O(m * n) time complexity.
# If the lists are of equal length, say n, then the time complexity can be expressed as O(n^2).
