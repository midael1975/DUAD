import random


num_secr = random.randint(1,10)
print("Adivina el numero secreto")
num_usua = int(input("Ingrese un numero: "))
print(num_usua)

if 1<=num_usua<=10 and num_usua==num_secr:
    print("Felicidades, adivinaste el numero secreto")
    break
else:
    print("Lo siento, no adivinaste el numero secreto, intenta de nuevo")
    num_usua = int(input("Ingrese un numero: "))
    print(num_usua)
    while num_usua!=num_secr and 1<=num_usua<=10:
        print("Lo siento, no adivinaste el numero secreto, intenta de nuevo")
        

