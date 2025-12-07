import random


num_secr = random.randint(1,10)
print("Adivina el numero secreto")

while True:
    num_user = int(input("Ingrese un numero: "))
    print(num_user)

    if num_user == num_secr:
        print("Felicidades, adivinaste el numero secreto")
        break
    else:
        print("Lo siento, no adivinaste el numero secreto, intenta de nuevo")




   

