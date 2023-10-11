import mysql.connector
from mysql.connector import Error
from connection import create_db_connection, close_db_connection
from tabulate import tabulate

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

    # Getters and setters for Order class
    def get_id_order(self):
        return self.id_order

    def set_id_order(self, id_order):
        self.id_order = id_order

    def get_id_user(self):
        return self.id_user

    def set_id_user(self, id_user):
        self.id_user = id_user

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def get_orderDate(self):
        return self.orderDate

    def set_orderDate(self, orderDate):
        self.orderDate = orderDate

    def get_payment_method(self):
        return self.payment_method

    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    def get_shipping_method(self):
        return self.shipping_method

    def set_shipping_method(self, shipping_method):
        self.shipping_method = shipping_method

    def get_payment_status(self):
        return self.payment_status

    def set_payment_status(self, payment_status):
        self.payment_status = payment_status

    def get_total_amount(self):
        return self.total_amount

    def set_total_amount(self, total_amount):
        self.total_amount = total_amount
        
        
def list_available_products(connection):
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id_products, name, price, stock FROM products WHERE stock > 0")
        products = cursor.fetchall()
        cursor.close()

        if not products:
            print("No hay productos disponibles.")
        else:
            table = []
            for product in products:
                table.append([
                    product['id_products'],
                    product['name'],
                    f"${product['price']:.2f}",  # Agregar "$" al precio
                    product['stock']
                ])

            headers = ["ID", "Nombre", "Precio", "Stock"]
            print(tabulate(table, headers, tablefmt="fancy_grid"))
    except Error as e:
        print(f"Error al listar los productos: {e}")



def create_order(connection, id_user, state, orderDate, payment_method, shipping_method, payment_status, product_items):
    try:
        cursor = connection.cursor()
        cursor.execute("START TRANSACTION")

        total_amount = 0  # Inicializa el total_amount

        # Crear el pedido
        query_create_order = """
            INSERT INTO orders (id_user, state, orderDate, payment_method, shipping_method, payment_status, total_amount)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query_create_order, (id_user, state, orderDate, payment_method, shipping_method, payment_status, total_amount))
        order_id = cursor.lastrowid

        # Agregar los productos al pedido con verificaciones
        query_create_order_items = """
            INSERT INTO order_items (id_order, id_products, quantity)
            VALUES (%s, %s, %s)
        """
        for product in product_items:
            # Verificar si el producto existe y si hay suficiente stock
            cursor.execute("SELECT id_products, stock, price FROM products WHERE id_products = %s", (product['id'],))
            product_info = cursor.fetchone()

            if not product_info:
                cursor.execute("ROLLBACK")
                print(f"El producto con ID {product['id']} no existe. Introduce un ID de producto válido.")
                return None  # Terminar la creación del pedido

            if product['quantity'] <= 0 or product['quantity'] > product_info[1]:  # Usar índices numéricos
                cursor.execute("ROLLBACK")
                print(f"La cantidad del producto con ID {product['id']} no es válida o excede el stock disponible. Introduce una cantidad válida.")
                return None  # Terminar la creación del pedido

            # Actualizar el total_amount con el costo total del producto
            total_amount += product_info[2] * product['quantity']

            cursor.execute(query_create_order_items, (order_id, product['id'], product['quantity']))

            # Actualizar el stock de los productos
            query_update_stock = """
                UPDATE products
                SET stock = stock - %s
                WHERE id_products = %s
            """
            cursor.execute(query_update_stock, (product['quantity'], product['id']))

        # Actualizar el total_amount en la base de datos
        query_update_total_amount = "UPDATE orders SET total_amount = %s WHERE id_order = %s"
        cursor.execute(query_update_total_amount, (total_amount, order_id))

        cursor.execute("COMMIT")
        return order_id
    except Error as e:
        cursor.execute("ROLLBACK")
        print(f"Error al crear el pedido: {e}")
        return None


# Función para leer los detalles de un pedido
def read_order_with_details(connection, order_id):
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT orders.id_order, orders.id_user, orders.state, orders.orderDate, 
            orders.payment_method, orders.shipping_method, orders.payment_status, 
            orders.total_amount
            FROM orders
            WHERE id_order = %s
        """
        cursor.execute(query, (order_id,))
        order = cursor.fetchone()
        if not order:
            return None

        order['products'] = get_products_for_order(connection, order_id)
        return order
    except Error as e:
        print(f"Error al obtener los detalles del pedido: {e}")
        return None

# Función para obtener productos asociados a un pedido
def get_products_for_order(connection, order_id):
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT products.id_products, products.name, order_items.quantity, products.price
            FROM order_items
            LEFT JOIN products ON order_items.id_products = products.id_products
            WHERE order_items.id_order = %s
        """
        cursor.execute(query, (order_id,))
        products = cursor.fetchall()
        return products
    except Error as e:
        print(f"Error al obtener los productos para el pedido: {e}")

# Función para actualizar un pedido
def update_order(connection, order_id, new_state, new_orderDate, new_payment_method, new_shipping_method, new_payment_status):
    try:
        cursor = connection.cursor()
        cursor.execute("START TRANSACTION")

        query_update_order = """
            UPDATE orders
            SET state = %s, orderDate = %s, payment_method = %s, shipping_method = %s, payment_status = %s
            WHERE id_order = %s
        """
        cursor.execute(query_update_order, (new_state, new_orderDate, new_payment_method, new_shipping_method, new_payment_status, order_id))

        cursor.execute("COMMIT")
        return True
    except Error as e:
        cursor.execute("ROLLBACK")
        print(f"Error al actualizar el pedido: {e}")
        return False
    
    
def delete_order(connection, order_id):
    try:
        cursor = connection.cursor()
        cursor.execute("START TRANSACTION")

        # Eliminar los registros relacionados en order_items
        query_delete_order_items = "DELETE FROM order_items WHERE id_order = %s"
        cursor.execute(query_delete_order_items, (order_id,))

        # Eliminar el pedido
        query_delete_order = "DELETE FROM orders WHERE id_order = %s"
        cursor.execute(query_delete_order, (order_id,))

        cursor.execute("COMMIT")
        return True
    except Error as e:
        cursor.execute("ROLLBACK")
        print(f"Error al eliminar el pedido: {e}")
        return False


# Función para listar todos los pedidos con los nombres de los productos uno debajo del otro
def list_all_orders(connection):
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
    SELECT orders.id_order, orders.id_user, orders.state, orders.orderDate, 
    orders.payment_method, orders.shipping_method, orders.payment_status, 
    orders.total_amount
    FROM orders
"""

        cursor.execute(query)
        orders = cursor.fetchall()

        if not orders:
            print("No hay pedidos disponibles.")
        else:
            for order in orders:
                order_id = order['id_order']

                cursor.execute("SELECT products.name FROM order_items LEFT JOIN products ON order_items.id_products = products.id_products WHERE order_items.id_order = %s", (order_id,))
                product_info = cursor.fetchall()
                
                print("\nDetalles del pedido:")
                details = {
                    "ID del Pedido": order['id_order'],
                    "ID del Usuario": order['id_user'],
                    "Estado": order['state'],
                    "Fecha": order['orderDate'],
                    "Método de Pago": order['payment_method'],
                    "Método de Envío": order['shipping_method'],
                    "Estado del Pago": order['payment_status'],
                    "Monto Total": "${:.2f}".format(order['total_amount'])  # Agregamos el símbolo "$"
                }
                
                if product_info:
                    details["Nombres de los Productos"] = "\n".join([product['name'] for product in product_info])
                else:
                    details["Nombres de los Productos"] = "No hay productos en este pedido."
                
                headers = details.keys()
                table = [list(details.values())]
                print(tabulate(table, headers, tablefmt="fancy_grid"))
    except Error as e:
        print(f"Error al listar los pedidos: {e}")



# Función para imprimir los detalles de un pedido
def print_order_with_details(order):
    if not order:
        print("Pedido no encontrado.")
        return

    print("\nDetalles del pedido:")
    print(f"ID del Pedido: {order['id_order']}")
    print(f"ID del Usuario: {order['id_user']}")
    print(f"Estado: {order['state']}")
    print(f"Fecha: {order['orderDate']}")
    print(f"Método de Pago: {order['payment_method']}")
    print(f"Método de Envío: {order['shipping_method']}")
    print(f"Estado del Pago: {order['payment_status']}")
    print(f"Monto Total: ${order['total_amount']:.2f}")  # Agregamos el símbolo "$"

if __name__ == "__main__":
    try:
        connection = create_db_connection()
        cursor = connection.cursor()  # Define cursor aquí

        with connection:
            while True:
                print("\nMenú de pedidos:")
                print("1. Listar productos disponibles")
                print("2. Crear un pedido")
                print("3. Leer detalles de un pedido")
                print("4. Actualizar un pedido")
                print("5. Eliminar un pedido")
                print("6. Listar todos los pedidos")
                print("7. Salir")
                choice = input("Elige una opción: ")

                if choice == "1":
                    list_available_products(connection)
                elif choice == "2":
                    id_user = int(input("ID de usuario: "))
                    state = input("Estado: ")
                    orderDate = input("Fecha del pedido (YYYY-MM-DD): ")
                    payment_method = input("Método de pago: ")
                    shipping_method = input("Método de envío: ")
                    payment_status = input("Estado del pago: ")

                    product_items = []  # Lista para almacenar los productos y cantidades

                    while True:
                        list_available_products(connection)  # Listar productos disponibles
                        product_id = input("ID del producto (0 para terminar): ")

                        if product_id == "0":
                            break  # Si el usuario ingresa "0", salimos del bucle
                        try:
                            product_id = int(product_id)
                            # Verificar si el producto existe
                            cursor.execute("SELECT id_products, stock FROM products WHERE id_products = %s", (product_id,))
                            product_info = cursor.fetchone()

                            if product_info:
                                quantity = int(input("Cantidad: "))
                                if quantity > 0 and quantity <= product_info[1]:
                                    product_items.append({'id': product_info[0], 'quantity': quantity})
                                else:
                                    print("La cantidad del producto no es válida o excede el stock disponible.")
                            else:
                                print(f"El producto con ID {product_id} no existe.")
                        except ValueError:
                            print("ID del producto no válido. Debe ser un número entero.")
                            continue

                    order_id = create_order(connection, id_user, state, orderDate, payment_method, shipping_method, payment_status, product_items)
                    if order_id:
                        print(f"Pedido creado con ID: {order_id}")
                elif choice == "3":
                    order_id = int(input("ID del pedido: "))
                    order = read_order_with_details(connection, order_id)
                    print_order_with_details(order)
                elif choice == "4":
                    order_id = int(input("ID del pedido a actualizar: "))
                    new_state = input("Nuevo estado: ")
                    new_orderDate = input("Nueva fecha del pedido (YYYY-MM-DD): ")
                    new_payment_method = input("Nuevo método de pago: ")
                    new_shipping_method = input("Nuevo método de envío: ")
                    new_payment_status = input("Nuevo estado del pago: ")
                    if update_order(connection, order_id, new_state, new_orderDate, new_payment_method, new_shipping_method, new_payment_status):
                        print("Pedido actualizado con éxito.")
                    else:
                        print("Error al actualizar el pedido.")
                elif choice == "5":
                    order_id = int(input("ID del pedido a eliminar: "))
                    if delete_order(connection, order_id):
                        print("Pedido eliminado con éxito.")
                    else:
                        print("Error al eliminar el pedido.")
                elif choice == "6":
                    list_all_orders(connection)
                elif choice == "7":
                    print("Saliendo del programa.")
                    break
                else:
                    print("Opción no válida. Introduce un número del 1 al 7.")
    except Error as e:
        print(f"Error en la base de datos: {e}")
    finally:
        close_db_connection(connection)
