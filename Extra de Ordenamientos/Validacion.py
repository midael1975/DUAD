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

def validated_bubble_sort(arr):
    try:
        if not list(arr):
            raise ValueError("Input must be a non-empty list.")
        sum(arr)  # Check if all elements are numbers
        return bubble_sort(arr)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    except ValueError as ve:
        print(f"Value error: {ve}")
        return None
    except TypeError as te:
        print(f"Type error: The list contains non-numeric elements. {te}")
        return None


# Example
if __name__ == "__main__":
    example_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", example_list)
    sorted_list = validated_bubble_sort(example_list)
    print("Sorted list:", sorted_list)

    # Testing with invalid input
    invalid_list = [64, "34", 25, 12, 22, 11, 90]
    sorted_list = validated_bubble_sort(invalid_list)
    print("Sorted invalid list:", sorted_list)


    # Testing with empty list
    empty_list = []
    sorted_list = validated_bubble_sort(empty_list)
    print("Sorted empty list:", sorted_list)


