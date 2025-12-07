name_lastname = input("Ingrese su nombre y apellido: ")
print(name_lastname)
age = int(input("Ingrese su edad: "))
print(age)


if 0<=age<4:
    print("Eres un bebe")
elif 4<=age<12:
    print("Eres un niño")
elif 12<=age<14:
    print("Eres un preadolescente")
elif 14<=age<18:
    print("Eres un adolescente")
elif 18<=age<31:
    print("Eres un joven adulto")
elif 31<=age<51:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")

