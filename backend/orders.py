import mysql.connector
from mysql.connector import Error

class Order:
    def __init__(self, id_order, id_user, state, orderDate, payment_method, shipping_method, payment_status, total_amount):
        self.id_order = id_order
        self.id_user = id_user
        self.state = state
        self.orderDate = orderDate
        self.payment_method = payment_method
        self.shipping_method = shipping_method
        self.payment_status = payment_status
        self.total_amount = total_amount
        
    # Getter para id_order
    def get_id_order(self):
        return self.id_order

    # Setter para id_order
    def set_id_order(self, id_order):
        self.id_order = id_order

    # Getter para id_user
    def get_id_user(self):
        return self.id_user

    # Setter para id_user
    def set_id_user(self, id_user):
        self.id_user = id_user

    # Getter para state
    def get_state(self):
        return self.state

    # Setter para state
    def set_state(self, state):
        self.state = state

    # Getter para orderDate
    def get_orderDate(self):
        return self.orderDate

    # Setter para orderDate
    def set_orderDate(self, orderDate):
        self.orderDate = orderDate

    # Getter para payment_method
    def get_payment_method(self):
        return self.payment_method

    # Setter para payment_method
    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    # Getter para shipping_method
    def get_shipping_method(self):
        return self.shipping_method

    # Setter para shipping_method
    def set_shipping_method(self, shipping_method):
        self.shipping_method = shipping_method

    # Getter para payment_status
    def get_payment_status(self):
        return self.payment_status

    # Setter para payment_status
    def set_payment_status(self, payment_status):
        self.payment_status = payment_status

    # Getter para total_amount
    def get_total_amount(self):
        return self.total_amount

    # Setter para total_amount
    def set_total_amount(self, total_amount):
        self.total_amount = total_amount


def create_order(connection, id_user, state, orderDate, payment_method, shipping_method, payment_status, total_amount):
    try:
        cursor = connection.cursor()
        query = """
            INSERT INTO orders
            (id_user, state, orderDate, payment_method, shipping_method, payment_status, total_amount)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (id_user, state, orderDate, payment_method, shipping_method, payment_status, total_amount)
        cursor.execute(query, values)
        connection.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error al crear un pedido: {e}")
        return None

def read_all_orders(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM orders"
        cursor.execute(query)
        orders = []

        for row in cursor.fetchall():
            orders.append(row)

        return orders
    except Error as e:
        print(f"Error al leer pedidos: {e}")
        
def update_order(connection, id_order, id_user, state, orderDate, payment_method, shipping_method, payment_status, total_amount):
    try:
        cursor = connection.cursor()
        query = """
            UPDATE orders
            SET id_user = %s, state = %s, orderDate = %s, payment_method = %s,
                shipping_method = %s, payment_status = %s, total_amount = %s
            WHERE id_order = %s
        """
        values = (id_user, state, orderDate, payment_method, shipping_method, payment_status, total_amount, id_order)
        cursor.execute(query, values)
        connection.commit()
    except Error as e:
        print(f"Error al actualizar el pedido: {e}")


def delete_order(connection, id_order):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM orders WHERE id_order = %s"
        cursor.execute(query, (id_order,))
        connection.commit()
    except Error as e:
        print(f"Error al eliminar el pedido: {e}")

def print_order(order):
    print("\nDetalles del pedido:")
    print(f"ID: {order[0]}")
    print(f"ID de usuario: {order[1]}")
    print(f"Estado: {order[2]}")
    print(f"Fecha del pedido: {order[3]}")
    print(f"Método de pago: {order[4]}")
    print(f"Método de envío: {order[5]}")
    print(f"Estado del pago: {order[6]}")
    print(f"Total: {order[7]}")

def read_order_by_id(connection, id_order):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM orders WHERE id_order = %s"
        cursor.execute(query, (id_order,))
        row = cursor.fetchone()

        if row:
            return row  # Devuelve los datos del pedido como una tupla
        else:
            print("Pedido no encontrado")
            return None
    except Error as e:
        print(f"Error al leer pedido por ID: {e}")
        return None

def manage_orders(connection):
    while True:
        print("\nMenú de Gestión de Pedidos:")
        print("1. Crear pedido")
        print("2. Leer pedidos")
        print("3. Actualizar pedido")
        print("4. Eliminar pedido")
        print("5. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            id_user = int(input("ID de usuario: "))
            state = input("Estado del pedido: ")
            orderDate = input("Fecha del pedido: ")
            payment_method = input("Método de pago: ")
            shipping_method = input("Método de envío: ")
            payment_status = input("Estado del pago: ")
            total_amount = float(input("Total: "))

            order_id = create_order(connection, id_user, state, orderDate, payment_method, shipping_method, payment_status, total_amount)
            if order_id:
                print(f"Pedido creado con ID: {order_id}")

        elif choice == "2":
            orders = read_all_orders(connection)
            if orders:
                print("\nListado de pedidos:")
                for order in orders:
                    print_order(order)

        elif choice == "3":
            order_id = int(input("ID del pedido a actualizar: "))
            order_to_update = read_order_by_id(connection, order_id)
            if order_to_update:
                print(f"Pedido a actualizar:")
                print_order(order_to_update)
                new_state = input("Nuevo estado (dejar en blanco para mantener el mismo): ")
                new_orderDate = input("Nueva fecha del pedido (dejar en blanco para mantener la misma): ")
                new_payment_method = input("Nuevo método de pago (dejar en blanco para mantener el mismo): ")
                new_shipping_method = input("Nuevo método de envío (dejar en blanco para mantener el mismo): ")
                new_payment_status = input("Nuevo estado del pago (dejar en blanco para mantener el mismo): ")
                new_total_amount = float(input("Nuevo total (0 para mantener el mismo): "))

                # Crear una nueva tupla con los valores actualizados
                updated_order = (
                    order_to_update[0],  # id_order
                    order_to_update[1],  # id_user
                    new_state if new_state else order_to_update[2],  # state
                    new_orderDate if new_orderDate else order_to_update[3],  # orderDate
                    new_payment_method if new_payment_method else order_to_update[4],  # payment_method
                    new_shipping_method if new_shipping_method else order_to_update[5],  # shipping_method
                    new_payment_status if new_payment_status else order_to_update[6],  # payment_status
                    new_total_amount if new_total_amount > 0 else order_to_update[7]  # total_amount
                )

                update_order(connection, *updated_order)
                print("Pedido actualizado")

        elif choice == "4":
            order_id = int(input("ID del pedido a eliminar: "))
            delete_order(connection, order_id)
            print("Pedido eliminado")

        elif choice == "5":
            break