def solicitar_numero(mensaje):
    """Solicita un número entero al usuario con validación."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada inválida. Debes ingresar un número válido.")

def solicitar_operacion():
    """Solicita una operación matemática válida (+, -, *, /)."""
    while True:
        operacion = input("¿Qué operación deseas realizar? (+, -, *, /): ")
        if operacion in ['+', '-', '*', '/']:
            return operacion
        print("Operación inválida. Debes ingresar +, -, *, /.")

def realizar_operacion(resultado, operacion, nuevo_numero):
    """Realiza la operación matemática indicada."""
    try:
        if operacion == '+':
            return resultado + nuevo_numero
        elif operacion == '-':
            return resultado - nuevo_numero
        elif operacion == '*':
            return resultado * nuevo_numero
        elif operacion == '/':
            if nuevo_numero == 0:
                print("No se puede dividir por cero.")
                return resultado
            return resultado / nuevo_numero
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return resultado

def calculator_function():
    """Función principal que coordina la calculadora."""
    resultado = solicitar_numero("Ingresa el primer número: ")

    while True:
        operacion = solicitar_operacion()
        nuevo_numero = solicitar_numero("Ingresa el siguiente número: ")
        resultado = realizar_operacion(resultado, operacion, nuevo_numero)
        print(f"El resultado es: {resultado}")

# Ejecutar la calculadora
calculator_function()



