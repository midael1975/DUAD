def ask_number():

    while True:
        try:
            return int(input("Ingresa el nuevo número: "))
        except ValueError:
            print("Entrada inválida. Debes ingresar un número válido.")
            continue

def ask_operation():

    while True:
        try:
            mathematic_operation = input('Cual operacion deseas realizar (+,-,*,/): ')
            if mathematic_operation in ['+', '-', '*', '/']:
                return mathematic_operation
        except ValueError as e:
            print(f'Operacion Matematica Invalida. Debes ingresar +, -, *, /: {e}')
            #mathematic_operation = input('Cual operacion deseas realizar (+,-,*,/): ')

def plus(number1, number_new):
    return number1 + number_new

def minus(number1, number_new):
    return number1 - number_new

def multiply(number1, number_new):
    return number1 * number_new

def divide(number1, number_new):
    if number_new == 0:
        print('No se puede dividir por cero')
        return number1
    return number1 / number_new

def do_operation(number1, mathematic_operation, number_new):

        try:
            if mathematic_operation == '+':
               return plus(number1, number_new)
            elif mathematic_operation == '-':
                return minus(number1, number_new)
            elif mathematic_operation == '*':
                return multiply(number1, number_new)
            elif mathematic_operation == '/':
                return divide(number1, number_new)

        except Exception as e:
            print(f'Ocurrió un error inesperado: {e}')
            return number1

        #try:
            #number_new = int(input('Ingresa el segundo número:'))
        #except ValueError:
            #print(f'Numero Invalido: {number_new} Intenta de nuevo')
            #continue
def calculator_function():

    number1 = 0
    print(f'La calculadora inicia en: {number1}')

    while True:
        number_new = ask_number()
        mathematic_operation = ask_operation()
        number1 = do_operation(number1, mathematic_operation, number_new)
        print(f'El resultado es: {number1}')

calculator_function()

