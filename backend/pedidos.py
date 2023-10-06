
import mysql.connector
from datetime import datetime

class OrderManager:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    

    def crear_pedido(self, id_user, state, orderDate, payment_method, shipping_method, payment_status, total_amount):
        try:
            orderDate = datetime.strptime(orderDate, "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            print("Formato de fecha incorrecto. Utiliza el formato dd/mm/yyyy.")
            return
        if not self.verificar_usuario_existente(id_user):
            print("Error: El usuario con ID", id_user, "no existe en la base de datos.")
            return

        query = "INSERT INTO orders (id_user, state, orderDate, payment_method, shipping_method, payment_status, total_amount) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (id_user, state, orderDate, payment_method, shipping_method, payment_status, total_amount)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Pedido creado con éxito!")

        

    def obtener_pedido_por_id(self, id_pedido):
        query = "SELECT * FROM orders WHERE id_order = %s"
        self.cursor.execute(query, (id_pedido,))
        pedido = self.cursor.fetchone()
        if pedido:
            print("Información del pedido:")
            print("ID:", pedido[0])
            print("ID de Usuario:", pedido[1])
            print("Estado:", pedido[2])
            print("=====================")
        else:
            print("Pedido no encontrado.")
    

        


    
   



    def actualizar_pedido(self, id_pedido, new_state, new_orderDate):
        query = "UPDATE orders SET state = %s, orderDate = %s WHERE id_order = %s"
        values = (new_state, new_orderDate, id_pedido)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Pedido actualizado con éxito!")




    def eliminar_pedido(self, id_pedido):
        query = "DELETE FROM orders WHERE id_order = %s"
        self.cursor.execute(query, (id_pedido,))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            print("Pedido eliminado con éxito!")
        else:
            print("Error: Pedido no encontrado o ya ha sido eliminado.")

    

def mostrar_menu():
    print("MENU PEDIDOS")
    print("====================")
    print("SELECCIONE OPCION")
    print("Menú de Operaciones:")
    print("1. Crear un nuevo pedido")
    print("2. Obtener información de un pedido por ID")
    print("3. Actualizar un pedido")
    print("4. Eliminar un pedido por ID")
    
    print("5. Salir")

if __name__ == "__main__":
    host = 'localhost'
    user = 'root'
    password = 'hernan'
    database = 'planetSuperheroesDB'
    
    order_manager = OrderManager(host, user, password, database)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_user = input("ID de Usuario: ")
            state = input("Estado: ")
            orderDate = input("Fecha de Pedido: ")
            payment_method = input("Método de Pago: ")
            shipping_method = input("Método de Envío: ")
            payment_status = input("Estado de Pago: ")
            total_amount = input("Monto Total: ")
            order_manager.crear_pedido(id_user, state, orderDate, payment_method, shipping_method, payment_status, total_amount)
           
        elif opcion == '2':
            id_pedido = input("Ingrese el ID del pedido: ")
            order_manager.obtener_pedido_por_id(id_pedido)

        elif opcion == '3':
            id_pedido = input("Ingrese el ID del pedido a actualizar: ")
            new_state = input("Nuevo estado: ")
            new_orderDate = input("Nueva fecha de pedido: ")
            order_manager.actualizar_pedido(id_pedido, new_state, new_orderDate)

        elif opcion == '4':
            id_pedido = input("Ingrese el ID del pedido a eliminar: ")
            order_manager.eliminar_pedido(id_pedido)

      
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

