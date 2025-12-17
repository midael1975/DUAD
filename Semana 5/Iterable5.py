numbers = []

# ask the user for 10 numbers
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numbers.append(num)

# Show all entered numbers
print("Números ingresados:", numbers)

# Show the highest number
print("El número más alto es:", max(numbers))

