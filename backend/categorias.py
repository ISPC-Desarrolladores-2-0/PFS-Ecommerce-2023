import mysql.connector
from mysql.connector import Error
from connection import create_db_connection

class Categoria:
    id_categoria = 0
    nombre_categoria = ""

    def __init__(self, id_categoria, nombre_categoria):
        self.id_categoria = id_categoria
        self.nombre_categoria = nombre_categoria

    def get_id_categoria(self):
        return self.id_categoria

    def set_id_categoria(self, id_categoria):
        self.id_categoria = id_categoria

    def get_nombre_categoria(self):
        return self.nombre_categoria

    def set_nombre_categoria(self, nombre_categoria):
        self.nombre_categoria = nombre_categoria

def list_products_by_category(connection, category_id):
    try:
        cursor = connection.cursor(dictionary=True)
        if category_id is None:
            query = """
                SELECT id_products, name, price, stock
                FROM products
                ORDER BY name ASC
            """
            cursor.execute(query)
        else:
            query = """
                SELECT p.id_products, p.name, p.price, p.stock
                FROM products AS p
                JOIN categories AS c ON p.id_categories = c.id_categories
                WHERE c.id_categories = %s
                ORDER BY p.name ASC
            """
            cursor.execute(query, (category_id,))
            
        products = cursor.fetchall()
        cursor.close()
        return products
    except Error as e:
        print(f"Error al obtener la lista de productos por categoría: {e}")
        return []


def categories_main(connection):
    selected_products = []  # Lista para almacenar los productos seleccionados

    while True:
        print("\nMenú:")
        print("1. Listar todos los productos")
        print("2. Listar productos de Marvel")
        print("3. Listar productos de DC")
        print("4. Finalizar selección")
        print("5. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            products = list_products_by_category(connection, category_id=None)
            if products:
                print("\nListado de todos los productos:")
                for product in products:
                    print(f"ID: {product['id_products']}, Nombre: {product['name']}, Precio: {product['price']}")
        
        elif choice == "2":
            marvel_category_id = 1
            marvel_products = list_products_by_category(connection, marvel_category_id)

            if marvel_products:
                print("\nListado de productos de Marvel:")
                for product in marvel_products:
                    print(f"ID: {product['id_products']}, Nombre: {product['name']}, Precio: {product['price']}")

        elif choice == "3":
            dc_category_id = 2
            dc_products = list_products_by_category(connection, dc_category_id)

            if dc_products:
                print("\nListado de productos de DC:")
                for product in dc_products:
                    print(f"ID: {product['id_products']}, Nombre: {product['name']}, Precio: {product['price']}")

        elif choice == "4":
            return selected_products  # Devuelve la lista de productos seleccionados

        elif choice == "5":
            return None  # Si elige salir, devuelve None

        # Opción adicional para seleccionar productos
        elif choice.isdigit() and int(choice) <= len(products):
            product_to_select = products[int(choice) - 1]
            selected_products.append((product_to_select['id_products'], product_to_select['name']))
            print(f"Producto '{product_to_select['name']}' seleccionado.")
