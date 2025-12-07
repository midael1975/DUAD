def calculadora_interactiva():
    actual = 0.0  # Número actual
    print("🧮 Calculadora iniciada. Número actual: 0.0")

    while True:
        print("\nMenú de operaciones:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Borrar resultado (reiniciar a 0)")
        print("0. Salir")

        opcion = input("Selecciona una opción (0-5): ")

        if opcion == '0':
            print("👋 Saliendo de la calculadora. ¡Hasta luego!")
            break

        if opcion not in {'1', '2', '3', '4', '5'}:
            print("❌ Opción inválida. Por favor selecciona del 0 al 5.")
            continue

        if opcion == '5':
            actual = 0.0
            print("🔄 Resultado borrado. Número actual reiniciado a 0.0")
            continue

        try:
            nuevo = float(input("Ingresa el nuevo número: "))
        except ValueError:
            print("❌ Entrada inválida. Debes ingresar un número válido.")
            continue

        try:
            if opcion == '1':
                actual += nuevo
            elif opcion == '2':
                actual -= nuevo
            elif opcion == '3':
                actual *= nuevo
            elif opcion == '4':
                if nuevo == 0:
                    print("❌ Error: No se puede dividir por cero.")
                    continue
                actual /= nuevo

            print(f"✅ Resultado actualizado: {actual}")

        except Exception as e:
            print(f"⚠️ Ocurrió un error inesperado: {e}")

# Ejecutar la calculadora
calculadora_interactiva()