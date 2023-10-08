import mysql.connector
from mysql.connector import Error
from connection import create_db_connection

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
        self.product_details = []

    def get_id_order(self):
        return self.id_order

    def get_id_user(self):
        return self.id_user

    def get_state(self):
        return self.state

    def get_order_date(self):
        return self.orderDate

    def get_payment_method(self):
        return self.payment_method

    def get_shipping_method(self):
        return self.shipping_method

    def get_payment_status(self):
        return self.payment_status

    def get_total_amount(self):
        return self.total_amount

    def set_id_order(self, id_order):
        self.id_order = id_order

    def set_id_user(self, id_user):
        self.id_user = id_user

    def set_state(self, state):
        self.state = state

    def set_order_date(self, orderDate):
        self.orderDate = orderDate

    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    def set_shipping_method(self, shipping_method):
        self.shipping_method = shipping_method

    def set_payment_status(self, payment_status):
        self.payment_status = payment_status

    def set_total_amount(self, total_amount):
        self.total_amount = total_amount


def list_products(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT id_products, name, price, stock FROM products"
        cursor.execute(query)
        products = []
        for row in cursor.fetchall():
            product = {
                'id_products': row[0],
                'name': row[1],
                'price': row[2],
                'stock': row[3]
            }
            products.append(product)
        return products
    except Error as e:
        print(f"Error al listar productos: {e}")
        return None

def list_orders(connection):
    try:
        cursor = connection.cursor()
        query = """
            SELECT o.id_order, o.id_user, o.state, o.orderDate, o.payment_method, o.shipping_method, o.payment_status, o.total_amount,
                   oi.id_products, p.name AS product_name, oi.quantity, p.price
            FROM orders o
            INNER JOIN order_items oi ON o.id_order = oi.id_order
            INNER JOIN products p ON oi.id_products = p.id_products
        """
        cursor.execute(query)

        orders = []

        current_order_id = None
        current_order = None

        for row in cursor.fetchall():
            (
                order_id, id_user, state, order_date, payment_method, shipping_method, payment_status, total_amount,
                product_id, product_name, quantity, product_price
            ) = row

            if current_order_id is None or order_id != current_order_id:
                if current_order is not None:
                    orders.append(current_order)
                current_order = Order(
                    order_id, id_user, state, order_date, payment_method, shipping_method, payment_status, total_amount
                )
                current_order.product_details = []
                current_order_id = order_id

            current_order.product_details.append(
                {
                    'product_id': product_id,
                    'product_name': product_name,
                    'quantity': quantity,
                    'product_price': product_price
                }
            )

        if current_order is not None:
            orders.append(current_order)

        return orders
    except Error as e:
        print(f"Error al listar pedidos: {e}")
        return None

def create_order(connection, id_user, state, orderDate, payment_method, shipping_method, payment_status):
    try:
        cursor = connection.cursor()
        query = """
            INSERT INTO orders
            (id_user, state, orderDate, payment_method, shipping_method, payment_status, total_amount)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute("SELECT id_products, name, price, stock FROM products")
        products = cursor.fetchall()

        if not products:
            print("No hay productos disponibles.")
            return None

        print("Lista de Productos:")
        selected_products = []

        for product in products:
            print(f"{product[0]}. {product[1]} - Precio: ${product[2]} - Stock: {product[3]}")
            selected_products.append({'id_products': product[0], 'name': product[1], 'quantity': 0, 'stock': product[3]})

        product_ids = []
        quantities = []

        while True:
            product_id = input("Ingrese el ID del producto que desea agregar (0 para finalizar): ")
            if product_id == "0":
                break
            try:
                product_id = int(product_id)
                product = next((p for p in selected_products if p['id_products'] == product_id), None)
                if product:
                    quantity = int(input(f"Ingrese la cantidad de {product['name']} que desea agregar: "))
                    if 0 < quantity <= product['stock']:
                        product_ids.append(product_id)
                        quantities.append(quantity)
                        product['quantity'] += quantity
                    else:
                        print(f"No hay suficiente stock para {product['name']}. Stock disponible: {product['stock']}")
                else:
                    print(f"No se encontró ningún producto con el ID {product_id}")
            except ValueError:
                print("Ingrese un ID de producto válido.")

        total_amount = calculate_total_amount(connection, product_ids, quantities)

        if total_amount is None:
            print("No se pudo calcular el total del pedido.")
            return None

        values = (id_user, state, orderDate, payment_method, shipping_method, payment_status, total_amount)
        cursor.execute(query, values)
        connection.commit()
        order_id = cursor.lastrowid

        associate_products_with_order(connection, order_id, product_ids, quantities)

        return order_id, selected_products
    except Error as e:
        print(f"Error al crear un pedido: {e}")
        return None

def update_product_stock(connection, product_ids, quantities):
    try:
        cursor = connection.cursor()
        for product_id, quantity in zip(product_ids, quantities):
            query = "UPDATE products SET stock = stock - %s WHERE id_products = %s"
            cursor.execute(query, (quantity, product_id))
        connection.commit()
    except Error as e:
        print(f"Error al actualizar el stock de productos: {e}")

def calculate_total_amount(connection, product_ids, quantities):
    try:
        cursor = connection.cursor()
        total_amount = 0
        for product_id, quantity in zip(product_ids, quantities):
            query = "SELECT price FROM products WHERE id_products = %s"
            cursor.execute(query, (product_id,))
            price = cursor.fetchone()
            if price is not None:
                total_amount += price[0] * quantity
            else:
                return None
        return total_amount
    except Error as e:
        print(f"Error al calcular el total del pedido: {e}")
        return None

def associate_products_with_order(connection, order_id, product_ids, quantities):
    try:
        cursor = connection.cursor()
        for product_id, quantity in zip(product_ids, quantities):
            query = "INSERT INTO order_items (id_order, id_products, quantity) VALUES (%s, %s, %s)"
            cursor.execute(query, (order_id, product_id, quantity))
        connection.commit()
    except Error as e:
        print(f"Error al asociar productos con el pedido: {e}")

def display_order(order):
    print(f"ID de Pedido: {order.id_order}")
    print(f"ID de Usuario: {order.id_user}")
    print(f"Estado: {order.state}")
    print(f"Fecha de Pedido: {order.orderDate}")
    print(f"Método de Pago: {order.payment_method}")
    print(f"Método de Envío: {order.shipping_method}")
    print(f"Estado de Pago: {order.payment_status}")
    print(f"Total Amount: {order.total_amount:.2f}")
    print("Productos en el pedido:")
    for product_detail in order.product_details:
        print(f"Nombre: {product_detail['product_name']}, Cantidad: {product_detail['quantity']}")

def get_order_by_id(connection, order_id):
    try:
        cursor = connection.cursor()
        query = """
            SELECT o.id_order, o.id_user, o.state, o.orderDate, o.payment_method, o.shipping_method, o.payment_status, o.total_amount,
                   oi.id_products, p.name AS product_name, oi.quantity, p.price
            FROM orders o
            INNER JOIN order_items oi ON o.id_order = oi.id_order
            INNER JOIN products p ON oi.id_products = p.id_products
            WHERE o.id_order = %s
        """
        cursor.execute(query, (order_id,))
        rows = cursor.fetchall()

        if not rows:
            print(f"No se encontró ningún pedido con el ID {order_id}")
            return None

        (
            order_id, id_user, state, order_date, payment_method, shipping_method, payment_status, total_amount,
            product_id, product_name, quantity, product_price
        ) = rows[0]

        order = Order(order_id, id_user, state, order_date, payment_method, shipping_method, payment_status, total_amount)
        order.product_details.append(
            {
                'product_id': product_id,
                'product_name': product_name,
                'quantity': quantity,
                'product_price': product_price
            }
        )

        return order
    except Error as e:
        print(f"Error al obtener un pedido por ID: {e}")
        return None

def update_order(connection, order):
    try:
        cursor = connection.cursor()
        query = """
            UPDATE orders
            SET id_user = %s, state = %s, orderDate = %s, payment_method = %s, shipping_method = %s, payment_status = %s, total_amount = %s
            WHERE id_order = %s
        """
        values = (
            order.id_user, order.state, order.orderDate, order.payment_method,
            order.shipping_method, order.payment_status, order.total_amount, order.id_order
        )
        cursor.execute(query, values)
        connection.commit()

        # Eliminar productos asociados al pedido
        cursor.execute("DELETE FROM order_items WHERE id_order = %s", (order.id_order,))
        connection.commit()

        # Asociar productos actualizados al pedido
        for product_detail in order.product_details:
            cursor.execute(
                "INSERT INTO order_items (id_order, id_products, quantity) VALUES (%s, %s, %s)",
                (order.id_order, product_detail['product_id'], product_detail['quantity'])
            )
            connection.commit()

        print(f"Pedido con ID {order.id_order} actualizado exitosamente.")
    except Error as e:
        print(f"Error al actualizar un pedido: {e}")

def delete_order(connection, order_id):
    try:
        cursor = connection.cursor()
        # Obtener los productos asociados al pedido
        cursor.execute("SELECT id_products, quantity FROM order_items WHERE id_order = %s", (order_id,))
        product_quantities = cursor.fetchall()

        # Actualizar el stock de productos
        for product_quantity in product_quantities:
            product_id, quantity = product_quantity
            cursor.execute("UPDATE products SET stock = stock + %s WHERE id_products = %s", (quantity, product_id))
            connection.commit()

        # Eliminar el pedido y sus productos asociados
        cursor.execute("DELETE FROM orders WHERE id_order = %s", (order_id,))
        connection.commit()
        print(f"Pedido con ID {order_id} eliminado exitosamente.")
    except Error as e:
        print(f"Error al eliminar un pedido: {e}")

if __name__ == "__main__":
    try:
        conn = create_db_connection()
        if conn.is_connected():
            print("Conexión a la base de datos exitosa")

            while True:
                print("\nMenú de Gestión de Pedidos:")
                print("1. Crear Pedido")
                print("2. Listar Pedidos")
                print("3. Actualizar Pedido")
                print("4. Eliminar Pedido")
                print("5. Salir")
                option = input("Selecciona una opción: ")

                if option == "1":
                    id_user = input("ID de Usuario: ")
                    state = input("Estado: ")
                    orderDate = input("Fecha de Pedido (YYYY-MM-DD): ")
                    payment_method = input("Método de Pago: ")
                    shipping_method = input("Método de Envío: ")
                    payment_status = input("Estado de Pago: ")
                    order_id, selected_products = create_order(
                        conn, id_user, state, orderDate, payment_method, shipping_method, payment_status
                    )
                    if order_id is not None:
                        print(f"Pedido creado con ID: {order_id}")
                        print("Productos en el pedido:")
                        for product in selected_products:
                            print(f"{product['name']} - Cantidad: {product['quantity']}")

                elif option == "2":
                    orders = list_orders(conn)
                    if orders:
                        print("Listado de Pedidos:")
                        for order in orders:
                            display_order(order)

                elif option == "3":
                    order_id = input("ID del pedido que desea actualizar: ")
                    order = get_order_by_id(conn, order_id)
                    if order is not None:
                        print("Detalles del Pedido:")
                        display_order(order)
                        id_user = input("ID de Usuario: ")
                        state = input("Estado: ")
                        orderDate = input("Fecha de Pedido (YYYY-MM-DD): ")
                        payment_method = input("Método de Pago: ")
                        shipping_method = input("Método de Envío: ")
                        payment_status = input("Estado de Pago: ")
                        order.id_user = id_user
                        order.state = state
                        order.orderDate = orderDate
                        order.payment_method = payment_method
                        order.shipping_method = shipping_method
                        order.payment_status = payment_status
                        update_order(conn, order)

                elif option == "4":
                    order_id = input("ID del pedido que desea eliminar: ")
                    delete_order(conn, order_id)

                elif option == "5":
                    break

    except Error as e:
        print(f"Error en la base de datos: {e}")
    finally:
        if conn.is_connected():
            conn.close()
            print("Conexión a la base de datos cerrada")