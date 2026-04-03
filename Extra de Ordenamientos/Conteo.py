def bubble_sort_steps(list):
    n= len(list)
    iterations = 0
    swaps = 0
    for j in range(0, n - 1):
        for i in range(0, n - 1):
            iterations = iterations + 1
            current_value = list[i]
            next_value = list[i + 1]
            if current_value > next_value:
                list[i], list[i + 1] = next_value, current_value
                swaps = swaps + 1
    return list, iterations, swaps


# Example
if __name__ == "__main__":
    example_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list, iterations, swaps = bubble_sort_steps(example_list)
    print(f"Sorted list: {sorted_list}")
    print(f"Iterations: {iterations}")
    print(f"Swaps: {swaps}")
