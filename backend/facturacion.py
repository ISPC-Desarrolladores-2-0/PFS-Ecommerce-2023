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
    payment_method = ""
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
        self.payment_method = ""
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
    
    def get_payment_method(self):
        return self.payment_method
    
    def get_id_facturacion(self):
        return self.id_facturacion
    
    def get_id_cliente(self):
        return self.id_cliente
    
    def get_telefono(self):
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
    
    def set_payment_method(self, payment_method):
        self.payment_method = payment_method
    
    def set_id_facturacion(self, id_facturacion):
        self.id_facturacion = id_facturacion
    
    def set_id_cliente(self, id_cliente):
        self.id_cliente = id_cliente
    
    def set_telefono(self, telefono):
        self.telefono = telefono
        
    def calculate_total_price(self, product_price):
        if self.payment_method == "Efectivo" or self.payment_method == "Transferencia":
            return round(product_price, 2)
        elif self.payment_method == "Tarjeta de Débito":
            return round(product_price, 2)
        elif self.payment_method == "Tarjeta de Crédito":
            if self.cuotas == 1:
                return round(product_price * 1.05, 2)
            elif self.cuotas == 3:
                return round(product_price * 1.15, 2)
            elif self.cuotas == 6:
                return round(product_price * 1.30, 2)
            else:
                raise ValueError("El número de cuotas no es válido")
        else:
            raise ValueError("Método de pago no válido")
    
    def validate_credit_card_number(self, numero_tarjeta):
        while not numero_tarjeta.isdigit() or len(numero_tarjeta) != 16:
            numero_tarjeta = input("➤El número de tarjeta no es válido. Ingrese nuevamente: ")
        return numero_tarjeta
    
    
    def validate_cardholder_name(self, nombre_titular):
        while len(nombre_titular.split()) != 2:
            nombre_titular = input("➤El nombre del titular debe tener nombre y apellido. Ingrese nuevamente: ")
        return nombre_titular
    
    @staticmethod
    def validate_expiration(expiration):
        while True:
            if not re.match(r"^[0-9/]+$", expiration):
                expiration = input("➤El formato del vencimiento no es válido. Por favor, ingrese solo 2 números para el mes, seguido de '/', y luego 2 números para el año: ")
            elif not re.match(r"^(0[1-9]|1[0-2])\/\d{2}$", expiration):
                expiration = input("➤El formato de vencimiento no es válido. Ingrese nuevamente (MM/AA): ")
            else:
                mes, anio = expiration.split('/')

                if not (mes.isdigit() and anio.isdigit()):
                    expiration = input("➤El formato de vencimiento no es válido. Ingrese nuevamente (MM/AA): ")
                    continue

                mes, anio = int(mes), int(anio)

                if not (1 <= mes <= 12 and 0 <= anio <= 99):
                    expiration = input("➤El formato de vencimiento no es válido. Ingrese nuevamente (MM/AA): ")
                    continue

                actual_date = datetime.now()
                compare_date = datetime(actual_date.year % 100, actual_date.month, 1)

                if compare_date> datetime(anio, mes, 1):
                    expiration = input("➤La fecha ingresada está vencida. Ingrese nuevamente (MM/AA): ")
                    continue               
            return expiration       
                
    def validate_verification_code(self, verification_code):
        while not verification_code.isdigit() or len(verification_code) != 3:
            verification_code = input("➤El código de verificación no es válido. Ingrese nuevamente: ")
        return verification_code


def display_menu():
    while True:
        print("\nMétodos de Pago:\n")
        print("1. Efectivo")
        print("2. Transferencia")
        print("3. Tarjeta de Débito")
        print("4. Tarjeta de Crédito")
        option = input("Elija una opción ingresando el N°: ")

        if option in ["1", "2", "3", "4"]:
            return int(option)
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


def request_credit_card_installments():
    while True:
        print("\nOpciones de cuotas:")
        print("1 cuota (5% de recargo)")
        print("3 cuotas (15% de recargo)")
        print("6 cuotas (30% de recargo)")
        option_installments = input("➤Elija una opción ingresando el N° de cuotas: ")

        if option_installments in ["1", "3", "6"]:
            return int(option_installments)
        else:
            print("El número de cuotas no es válido. Por favor, seleccione una opción válida.")


def request_card_information():
    while True:
        print("\nOpciones de tarjetas:")
        print("1. VISA")
        print("2. Mastercard")
        print("3. Naranja")
        option_card = input("➤Elija una opción ingresando el N°: ")

        if option_card in ["1", "2", "3"]:
            card_select = None
            if option_card == "1":
                card_select = "VISA"
            elif option_card == "2":
                card_select = "Mastercard"
            elif option_card == "3":
                card_select = "Naranja"

            numero_tarjeta = input("➤Ingrese el número de la tarjeta: ")
            nombre_titular = input("➤Ingrese el nombre del titular de la tarjeta: ")
            expiration = input("➤Ingrese el vencimiento de la tarjeta (MM/AA): ")
            verification_code = input("➤Ingrese el código de verificación: ")
            return numero_tarjeta, nombre_titular, expiration, verification_code, card_select
        else:
            print("Opción de tarjeta inválida. Por favor, seleccione una opción válida.")

def validate_locality_cba(localidad):
    return localidad.lower() in ['cordoba capital', 'córdoba capital']

def cash_payment(localidad):    
    if validate_locality_cba(localidad):
        print("\n\Opciones para pago en efectivo:")
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
 
def process_billing():
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
        option = display_menu()
        
        if option == 1:
            factura.payment_method = "Efectivo"
            cash_payment(factura.localidad)        
        elif option == 2:
            factura.payment_method = "Transferencia"
            transfer_pay()
        elif option == 3:
            factura.payment_method = "Tarjeta de Débito"    
        elif option == 4:
            factura.payment_method = "Tarjeta de Crédito"        
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

        product_price = 9800.00  # Precio ficticio, tendria que ser el que se consulta a la BDD

        try:
            total_price = factura.calculate_total_price(product_price)
            print(f"El precio total de su pedido es: {total_price}.")

            if factura.payment_method == "Tarjeta de Crédito":
                print("Tenga en cuenta que el pago con tarjeta de crédito aplica recargos.")
                cuotas = request_credit_card_installments()
                factura.cuotas = cuotas
                precio_con_cuotas = factura.calculate_total_price(total_price)
                print(f"El precio con cuotas es: {precio_con_cuotas}")

                confirmacion = input("➤¿Desea continuar con el pago? (s/n): ")
           
                if confirmacion.lower() == "s":
                    numero_tarjeta, nombre_titular, expiration, verification_code, card_select = request_card_information()
                    numero_tarjeta = factura.validate_credit_card_number(numero_tarjeta)
                    nombre_titular = factura.validate_cardholder_name(nombre_titular)
                    expiration = factura.validate_expiration(expiration)
                    verification_code = factura.validate_verification_code(verification_code)
                    card_select = card_select

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
    process_billing()