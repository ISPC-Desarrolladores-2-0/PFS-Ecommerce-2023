"""
class Facturacion: 
    id_facturacion = 0
    id_cliente = 0
    nombre=""
    apellido=""
    dni=""
    direccion=""
    numero_calle=""
    localidad=""
    metodo_pago=""

    def __init__(self, id_facturacion, id_cliente, nombre, apellido, dni, direccion, numero_calle, localidad, metodo_pago):
        self.id_facturacion = id_facturacion
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.numero_calle = numero_calle
        self.localidad = localidad
        self.metodo_pago = metodo_pago

    def get_name(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_dni(self):
        return self.dni
    
    def get_direccion(self):
        return self.direccion
    
    def get_numero_calle(self):
        return self.numero_calle
    
    def get_localidad(self):
        return self.localidad
    
    def get_metodo_pago(self):
        return self.metodo_pago
    
    def get_id_facturacion(self):
        return self.id_facturacion
    
    def get_id_cliente(self):
        return self.id_cliente
    
    def set_name(self, nombre):
        self.nombre = nombre
    
    def set_apellido(self, apellido):
        self.apellido = apellido
    
    def set_dni(self, dni):
        self.dni = dni
    
    def set_direccion(self, direccion):
        self.direccion = direccion
    
    def set_numero_calle(self, numero_calle):
        self.numero_calle = numero_calle
    
    def set_localidad(self, localidad):
        self.localidad = localidad
    
    def set_metodo_pago(self, metodo_pago):
        self.metodo_pago = metodo_pago
    
    def set_id_facturacion(self, id_facturacion):
        self.id_facturacion = id_facturacion
    
    def set_id_cliente(self, id_cliente):
        self.id_cliente = id_cliente
        
    def calcular_precio_total(self, precio_producto, cuotas=1):
        if self.metodo_pago == "Efectivo" or self.metodo_pago == "Transferencia":
            return precio_producto
        elif self.metodo_pago == "Tarjeta de Crédito":
            if cuotas == 1:
                return precio_producto * 1.10
            elif cuotas == 3:
                return precio_producto * 1.20
            elif cuotas == 6:
                return precio_producto * 1.30
            else:
                raise ValueError("El número de cuotas no es válido")
        else:
            raise ValueError("Método de pago no válido")

def mostrar_menu():
    print("Métodos de Pago:")
    print("1. Efectivo o Transferencia")
    print("2. Tarjeta de Crédito (1 cuota)")
    print("3. Tarjeta de Crédito (3 cuotas)")
    print("4. Tarjeta de Crédito (6 cuotas)")
    opcion = int(input("Elija una opción (1-4): "))
    return opcion

def main():
    factura = Facturacion(id_facturacion, id_cliente, nombre, apellido, dni, direccion, numero_calle, localidad, metodo_pago)
    precio_producto = float(input("Ingrese el precio del producto: "))

    opcion = mostrar_menu()

    if opcion == 1:
        precio_total = factura.calcular_precio_total(precio_producto)
    elif opcion in [2, 3, 4]:
        cuotas = opcion  # La opción 2 corresponde a 1 cuota, la 3 a 3 cuotas y la 4 a 6 cuotas.
        precio_total = factura.calcular_precio_total(precio_producto, cuotas)
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

    print(f"El precio total es: {precio_total}")

if __name__ == "__main__":
    main()    
"""


class Facturacion: 
    id_facturacion = 0
    id_cliente = 0
    nombre = ""
    apellido = ""
    dni = ""
    direccion = ""
    numero_calle = ""
    localidad = ""
    metodo_pago = ""
    cuotas = 1

    def __init__(self):
        self.id_facturacion = 0
        self.id_cliente = 0
        self.nombre = ""
        self.apellido = ""
        self.dni = ""
        self.direccion = ""
        self.numero_calle = ""
        self.localidad = ""
        self.metodo_pago = ""
        self.cuotas = 1

    def get_name(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_dni(self):
        return self.dni
    
    def get_direccion(self):
        return self.direccion
    
    def get_numero_calle(self):
        return self.numero_calle
    
    def get_localidad(self):
        return self.localidad
    
    def get_metodo_pago(self):
        return self.metodo_pago
    
    def get_id_facturacion(self):
        return self.id_facturacion
    
    def get_id_cliente(self):
        return self.id_cliente
    
    def set_name(self, nombre):
        self.nombre = nombre
    
    def set_apellido(self, apellido):
        self.apellido = apellido
    
    def set_dni(self, dni):
        self.dni = dni
    
    def set_direccion(self, direccion):
        self.direccion = direccion
    
    def set_numero_calle(self, numero_calle):
        self.numero_calle = numero_calle
    
    def set_localidad(self, localidad):
        self.localidad = localidad
    
    def set_metodo_pago(self, metodo_pago):
        self.metodo_pago = metodo_pago
    
    def set_id_facturacion(self, id_facturacion):
        self.id_facturacion = id_facturacion
    
    def set_id_cliente(self, id_cliente):
        self.id_cliente = id_cliente
        
    def calcular_precio_total(self, precio_producto):
        if self.metodo_pago == "Efectivo" or self.metodo_pago == "Transferencia":
            return round(precio_producto, 2)
        elif self.metodo_pago == "Tarjeta de Débito":
            return round(precio_producto, 2)
        elif self.metodo_pago == "Tarjeta de Crédito":
            if self.cuotas == 1:
                return round(precio_producto * 1.05, 2)
            elif self.cuotas == 3:
                return round(precio_producto * 1.15, 2)
            elif self.cuotas == 6:
                return round(precio_producto * 1.30, 2)
            else:
                raise ValueError("El número de cuotas no es válido")
        else:
            raise ValueError("Método de pago no válido")

def mostrar_menu():    
    print("\nMétodos de Pago:\n")
    print("1. Efectivo")
    print("2. Transferencia")
    print("3. Tarjeta de Débito")
    print("4. Tarjeta de Crédito") 
    opcion = int(input("Elija una opción ingresando el N°: "))
    return opcion

def solicitar_cuotas():
    print("\nOpciones de cuotas:")
    print("1 cuota (5% de recargo)")
    print("3 cuotas (15% de recargo)")
    print("6 cuotas (30% de recargo)")
    opcion_cuotas = int(input("Elija una opción ingresando el N° de cuotas: "))

    if opcion_cuotas in [1, 3, 6]:
        return opcion_cuotas
    else:
        raise ValueError("El número de cuotas no es válido.")

def solicitar_datos_tarjeta():
    print("\nOpciones de tarjetas:")
    print("1. VISA")
    print("2. Mastercard")
    print("3. Naranja")
    opcion_tarjeta = int(input("Elija una opción ingresando el N°: "))

    if opcion_tarjeta in [1, 2, 3]:
        numero_tarjeta = input("Ingrese el número de la tarjeta: ")
        nombre_titular = input("Ingrese el nombre del titular de la tarjeta: ")
        vencimiento = input("Ingrese el vencimiento de la tarjeta (MM/AA): ")
        codigo_verificacion = input("Ingrese el código de verificación: ")

        return numero_tarjeta, nombre_titular, vencimiento, codigo_verificacion
    else:
        raise ValueError("Opción de tarjeta inválida. Cancelando compra.")

def procesar_factura():
    factura = Facturacion()

    # Solicitar al usuario que ingrese la información necesaria
    print("FACTURACIÓN DE PEDIDOS\n")
    print("Por favor complete los siguientes datos de su pedido")
    factura.nombre = input("Ingrese su nombre: ")
    factura.apellido = input("Ingrese su apellido: ")
    factura.dni = input("Ingrese su DNI: ")
    factura.direccion = input("Ingrese su dirección: ")
    factura.numero_calle = input("Ingrese el número de su calle: ")
    factura.localidad = input("Ingrese su localidad: ")

    opcion = mostrar_menu()

    if opcion == 1:
        factura.metodo_pago = "Efectivo"
    elif opcion == 2:
        factura.metodo_pago = "Transferencia"
    elif opcion == 3:
        factura.metodo_pago = "Tarjeta de Débito"    
    elif opcion == 4:
        factura.metodo_pago = "Tarjeta de Crédito"
        #factura.cuotas = opcion - 2   La opción 3 corresponde a 3 cuotas y la 4 a 6 cuotas.
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

    precio_producto = 9800.00  # Precio ficticio, tendria que ser el que se consulta a la BDD

    try:
        precio_total = factura.calcular_precio_total(precio_producto)
        print(f"El precio total de su pedido es: {precio_total}. Tenga en cuenta que el pago con tarjeta de crédito aplica recargos.")

        if factura.metodo_pago == "Tarjeta de Crédito":
            cuotas = solicitar_cuotas()
            factura.cuotas = cuotas
            precio_con_cuotas = factura.calcular_precio_total(precio_total)
            print(f"El precio con cuotas es: {precio_con_cuotas}")

            confirmacion = input("¿Desea continuar con el pago? (s/n): ")

            if confirmacion.lower() == "s":
                numero_tarjeta, nombre_titular, vencimiento, codigo_verificacion = solicitar_datos_tarjeta()

                # Faltan las validaciones para los datos de la tarjeta (número, vencimiento, CVV)
                

                print("Datos de tarjeta validados.")
                confirmacion = input("¿Desea continuar con el pago? (s/n): ")
                print("Compra completada exitosamente. Pronto nos pondremos en contacto contigo.")
            else:
                print("Compra cancelada.")
        else:            
            print("Compra completada exitosamente. Pronto nos pondremos en contacto contigo.")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    procesar_factura()