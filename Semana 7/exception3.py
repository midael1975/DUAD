def ask_number():
    """Solicita un número entero al usuario con validación."""
    while True:
        try:
            return int(input("Ingresa un número: "))
        except ValueError:
            print("Entrada inválida. Debes ingresar un número válido.")

def plus(result, number):
    return result + number

def minus(result, number):
    return result - number

def multiply(result, number):
    return result * number

def divide(result, number):
    if number == 0:
        print('No se puede dividir por cero')
        return result
    return result / number

def ask_operation():
    """Solicita una operación matemática válida (+, -, *, /)."""
    while True:
        operation = input("¿Qué operación deseas realizar? (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            return operation
        print("Operación inválida. Debes ingresar +, -, *, /.")

def do_operation(result, operation, number):
    """Realiza la operación matemática indicada y devuelve el nuevo resultado."""
    try:
        if operation == '+':
            return plus(result, number)
        elif operation == '-':
            return minus(result, number)
        elif operation == '*':
            return multiply(result, number)
        elif operation == '/':
            return divide(result, number)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return result

def calculator_function():
    """Función principal que coordina la calculadora, siempre empezando en 0."""
    result = 0  # siempre inicia en cero
    print(f"La calculadora inicia en: {result}")

    while True:
        operation = ask_operation()
        number = ask_number()
        result = do_operation(result, operation, number)
        print(f"El resultado es: {result}")

# Ejecutar la calculadora
calculator_function()