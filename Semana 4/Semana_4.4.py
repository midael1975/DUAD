num_1 = int(input("Ingrese el primer numero: "))
print(num_1)
num_2 = int(input("Ingrese el segundo numero: "))
print(num_2)
num_3 = int(input("Ingrese el tercer numero: "))
print(num_3)
mens = "El numero mayor es: "


if num_1 > num_2 and num_1 > num_3:
    print("{mens}", num_1)
elif num_2 > num_1 and num_2 > num_3:
    print("{mens}", num_2)
else:
    print("El numero mayor es: ", num_3)