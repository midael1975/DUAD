numbers_list = [53, 60, 32, 62, 400, 10]

def  change_list(numbers_list):
    for index, number in enumerate(numbers_list):
        if number > 100:
            numbers_list[index] = number -10
            return numbers_list

print(change_list(numbers_list))