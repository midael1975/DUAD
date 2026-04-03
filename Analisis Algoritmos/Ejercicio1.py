def bubble_sort(arr):
    n = len(arr)
    for i in range(n): #Outer loop
        for j in range(0, n-i-1): #Inner loop
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Code Analysis:
# The outer loop is executed n times where n represents the number of elements in the list, therefore,
# according to Big O this is O(n)
# The inner loop traverses the list, comparing the elements for each iteration of the outer loop.
# The number of comparisons in the inner loop decreases with each iteration.
# Analysis shows that the number of comparisons depends proportionally on n, so the inner loop's timescale is O(n).
# Therefore, since it's a nested loop, its timescale is O(n) x O(n) = O(n^2).

