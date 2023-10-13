import re
from datetime import datetime


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
    telefono = ""

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
        self.telefono = ""

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
    
    def get_telefono(self, telefono):
        return self.telefono
    
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
    
    def set_telefono(self, telefono):
        self.telefono = telefono
        
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
    
    def validar_numero_tarjeta(self, numero_tarjeta):
        while not numero_tarjeta.isdigit() or len(numero_tarjeta) != 16:
            numero_tarjeta = input("➤El número de tarjeta no es válido. Ingrese nuevamente: ")
        return numero_tarjeta
    
    
    def validar_nombre_titular(self, nombre_titular):
        while len(nombre_titular.split()) != 2:
            nombre_titular = input("➤El nombre del titular debe tener nombre y apellido. Ingrese nuevamente: ")
        return nombre_titular
    
    @staticmethod
    def validar_vencimiento(vencimiento):
        while True:
            if not re.match(r"^[0-9/]+$", vencimiento):
                vencimiento = input("➤El formato del vencimiento no es válido. Por favor, ingrese solo 2 números para el mes, seguido de '/', y luego 2 números para el año: ")
            elif not re.match(r"^(0[1-9]|1[0-2])\/\d{2}$", vencimiento):
                vencimiento = input("➤El formato de vencimiento no es válido. Ingrese nuevamente (MM/AA): ")
            else:
                mes, anio = vencimiento.split('/')

                if not (mes.isdigit() and anio.isdigit()):
                    vencimiento = input("➤El formato de vencimiento no es válido. Ingrese nuevamente (MM/AA): ")
                    continue

                mes, anio = int(mes), int(anio)

                if not (1 <= mes <= 12 and 0 <= anio <= 99):
                    vencimiento = input("➤El formato de vencimiento no es válido. Ingrese nuevamente (MM/AA): ")
                    continue

                fecha_actual = datetime.now()
                fecha_comparar = datetime(fecha_actual.year % 100, fecha_actual.month, 1)

                if fecha_comparar > datetime(anio, mes, 1):
                    vencimiento = input("➤La fecha ingresada está vencida. Ingrese nuevamente (MM/AA): ")
                    continue               
            return vencimiento       
                
    def validar_codigo_verificacion(self, codigo_verificacion):
        while not codigo_verificacion.isdigit() or len(codigo_verificacion) != 3:
            codigo_verificacion = input("➤El código de verificación no es válido. Ingrese nuevamente: ")
        return codigo_verificacion


def mostrar_menu():
    while True:
        print("\nMétodos de Pago:\n")
        print("1. Efectivo")
        print("2. Transferencia")
        print("3. Tarjeta de Débito")
        print("4. Tarjeta de Crédito")
        opcion = input("Elija una opción ingresando el N°: ")

        if opcion in ["1", "2", "3", "4"]:
            return int(opcion)
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


def solicitar_cuotas():
    while True:
        print("\nOpciones de cuotas:")
        print("1 cuota (5% de recargo)")
        print("3 cuotas (15% de recargo)")
        print("6 cuotas (30% de recargo)")
        opcion_cuotas = input("➤Elija una opción ingresando el N° de cuotas: ")

        if opcion_cuotas in ["1", "3", "6"]:
            return int(opcion_cuotas)
        else:
            print("El número de cuotas no es válido. Por favor, seleccione una opción válida.")


def solicitar_datos_tarjeta():
    while True:
        print("\nOpciones de tarjetas:")
        print("1. VISA")
        print("2. Mastercard")
        print("3. Naranja")
        opcion_tarjeta = input("➤Elija una opción ingresando el N°: ")

        if opcion_tarjeta in ["1", "2", "3"]:
            tarjeta_elegida = None
            if opcion_tarjeta == "1":
                tarjeta_elegida = "VISA"
            elif opcion_tarjeta == "2":
                tarjeta_elegida = "Mastercard"
            elif opcion_tarjeta == "3":
                tarjeta_elegida = "Naranja"

            numero_tarjeta = input("➤Ingrese el número de la tarjeta: ")
            nombre_titular = input("➤Ingrese el nombre del titular de la tarjeta: ")
            vencimiento = input("➤Ingrese el vencimiento de la tarjeta (MM/AA): ")
            codigo_verificacion = input("➤Ingrese el código de verificación: ")
            return numero_tarjeta, nombre_titular, vencimiento, codigo_verificacion, tarjeta_elegida
        else:
            print("Opción de tarjeta inválida. Por favor, seleccione una opción válida.")

def validar_localidad_cba(localidad):
    return localidad.lower() in ['cordoba capital', 'córdoba capital']

def pago_en_efectivo(localidad):    
    if validar_localidad_cba(localidad):
        print("\n\tOpciones para pago en efectivo:")
        print("1. Retirar en el local")
        print("2. Abonar al recibir en domicilio")
        opcion_efectivo = input("➤Elija una opción ingresando el N°: ")

        if opcion_efectivo == "1":
            print("\n◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈")
            print("Le pedimos que se acerque al local en los próximos 5 días habiles. Caso contrario se procederá a contarlo")  # Precio ficticio
            print("◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈\n")
        elif opcion_efectivo == "2":
            print("\n◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈")
            print("En las proximas 24hs habiles se realizará la entrega de su pedido al domicilio que indicó sin costo adicional.")  # Precio ficticio
            print("◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈\n")
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
    else:
        print("La localidad ingresada no admite la opción de pago en efectivo.")

def transfer_pay():
    print("\n◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈")
    print("Por favor realiza el envío de la transferencia al alias: planet.superheroes \nBanco de Córdoba\nUna vez completado envianos el comprobante por mail a: pagos@planetsuper.com.ar")       
    print("◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈\n")
 
def procesar_factura():
    factura = Facturacion()
    
    print("\n\tFACTURACIÓN DE PEDIDOS\n")
    print("Por favor complete los siguientes datos de su pedido")
    factura.nombre = input("Ingrese su nombre: ")
    factura.apellido = input("Ingrese su apellido: ")
    factura.dni = input("Ingrese su DNI: ")
    factura.direccion = input("Ingrese su dirección: ")
    factura.numero_calle = input("Ingrese el número de su calle: ")
    factura.localidad = input("Ingrese su localidad: ")
    factura.telefono = input("Ingrese su número de teléfono: ")
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == 1:
            factura.metodo_pago = "Efectivo"
            pago_en_efectivo(factura.localidad)        
        elif opcion == 2:
            factura.metodo_pago = "Transferencia"
            transfer_pay()
        elif opcion == 3:
            factura.metodo_pago = "Tarjeta de Débito"    
        elif opcion == 4:
            factura.metodo_pago = "Tarjeta de Crédito"        
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

        precio_producto = 9800.00  # Precio ficticio, tendria que ser el que se consulta a la BDD

        try:
            precio_total = factura.calcular_precio_total(precio_producto)
            print(f"El precio total de su pedido es: {precio_total}.")

            if factura.metodo_pago == "Tarjeta de Crédito":
                print("Tenga en cuenta que el pago con tarjeta de crédito aplica recargos.")
                cuotas = solicitar_cuotas()
                factura.cuotas = cuotas
                precio_con_cuotas = factura.calcular_precio_total(precio_total)
                print(f"El precio con cuotas es: {precio_con_cuotas}")

                confirmacion = input("➤¿Desea continuar con el pago? (s/n): ")
           
                if confirmacion.lower() == "s":
                    numero_tarjeta, nombre_titular, vencimiento, codigo_verificacion, tarjeta_elegida = solicitar_datos_tarjeta()
                    numero_tarjeta = factura.validar_numero_tarjeta(numero_tarjeta)
                    nombre_titular = factura.validar_nombre_titular(nombre_titular)
                    vencimiento = factura.validar_vencimiento(vencimiento)
                    codigo_verificacion = factura.validar_codigo_verificacion(codigo_verificacion)
                    tarjeta_elegida = tarjeta_elegida

                    print("Datos de tarjeta validados.")
                    confirmacion = input("¿Desea continuar con el pago? (s/n): ")
                    print("Compra completada exitosamente. Pronto nos pondremos en contacto contigo.")
                else:
                    print("Compra cancelada.")
            else:            
                print("\nSi tienes alguna duda o consulta por favor tontactanos")
        
        except ValueError as e:
            print(e)
        continuar = input("¿Desea procesar otra factura? (s/n): ")
        if continuar.lower() != "s":
            break

if __name__ == "__main__":
    procesar_factura()





