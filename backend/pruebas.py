


def solicitar_datos_tarjeta():
    while True:
        print("\nOpciones de tarjetas:")
        print("1. VISA")
        print("2. Mastercard")
        print("3. Naranja")
        opcion_tarjeta = input("Elija una opción ingresando el N°: ")

        if opcion_tarjeta in ["1", "2", "3"]:
            tarjeta_elegida = None
            if opcion_tarjeta == "1":
                tarjeta_elegida = "VISA"
            elif opcion_tarjeta == "2":
                tarjeta_elegida = "Mastercard"
            elif opcion_tarjeta == "3":
                tarjeta_elegida = "Naranja"

            numero_tarjeta = input("Ingrese el número de la tarjeta: ")
            nombre_titular = input("Ingrese el nombre del titular de la tarjeta: ")
            vencimiento = input("Ingrese el vencimiento de la tarjeta (MM/AA): ")
            codigo_verificacion = input("Ingrese el código de verificación: ")

            # Validaciones
            numero_tarjeta = validar_numero_tarjeta(numero_tarjeta)
            nombre_titular = validar_nombre_titular(nombre_titular)
            vencimiento = validar_vencimiento(vencimiento)
            codigo_verificacion = validar_codigo_verificacion(codigo_verificacion)

            return numero_tarjeta, nombre_titular, vencimiento, codigo_verificacion, tarjeta_elegida
        else:
            print("Opción de tarjeta inválida. Por favor, seleccione una opción válida.")