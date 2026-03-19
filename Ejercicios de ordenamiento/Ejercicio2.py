def bubble_sort(list):
    for j in range(0, len(list) - 1):
        # We move from right to left
        for i in range(len(list) - 1, 0, -1):
            current_value = list[i]
            prev_value = list[i - 1]

            # If the current value is smaller, we push it to the left
            if current_value < prev_value:
                list[i], list[i - 1] = prev_value, current_value

    return list


# Example
if __name__ == "__main__":
    list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Original Array:", list)
    sorted_list = bubble_sort(list)
    print("Sorted Array:", sorted_list)