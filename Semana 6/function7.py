def prime_numbers(number_list):
    prime_numbers_list = []
    for number in number_list:
        is_prime = True
        if number <= 1:
            is_prime = False
        else:
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break
        if is_prime:
            prime_numbers_list.append(number)
    return prime_numbers_list

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 29]
print(prime_numbers(number_list))

