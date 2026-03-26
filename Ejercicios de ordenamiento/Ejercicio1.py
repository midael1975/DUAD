def bubble_sort(list):
    for j in range(0, len(list) - 1):
        for i in  range(0, len(list) -1):
            current_value = list[i]
            next_value = list[i + 1]
            if current_value > next_value:
                list[i], list[i + 1] = next_value, current_value
    return list

# Example
if __name__ == "__main__":
    list = [64, 34, 25, 12, 22, 11, 90]
    print("Original Array:", list)
    sorted_list = bubble_sort(list)
    print("Sorted Array:", sorted_list)