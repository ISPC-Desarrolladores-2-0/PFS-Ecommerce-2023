from connection import create_db_connection, close_db_connection
import mysql.connector
from mysql.connector import Error

class Category:
    def __init__(self, id_categories, name):
        self.id_categories = id_categories
        self.name = name

    def get_id_categories(self):
        return self.id_categories

    def set_id_categories(self, id_categories):
        self.id_categories = id_categories

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

def list_products_by_category(connection, category_id):
    try:
        cursor = connection.cursor(dictionary=True)
        if category_id is None:
            query = """
                SELECT id_products, name
                FROM products
            """
            cursor.execute(query)
        else:
            query = """
                SELECT p.id_products, p.name
                FROM products AS p
                JOIN categories AS c ON p.id_categories = c.id_categories
                WHERE c.id_categories = %s
            """
            cursor.execute(query, (category_id,))
            
        products = cursor.fetchall()
        cursor.close()
        return products
    except Error as e:
        print(f"Error al obtener la lista de productos por categoría: {e}")
        return []

def create_category(connection, name):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO categories (name) VALUES (%s)"
        cursor.execute(query, (name,))
        connection.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error al crear una categoría: {e}")
        return None

def read_all_categories(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM categories"
        cursor.execute(query)
        categories = []

        for row in cursor.fetchall():
            category = {
                'id': row[0],
                'name': row[1]
            }
            categories.append(category)

        return categories
    except Error as e:
        print(f"Error al leer categorías: {e}")

def update_category(connection, category_id, new_name):
    try:
        cursor = connection.cursor()
        query = "UPDATE categories SET name = %s WHERE id_categories = %s"
        cursor.execute(query, (new_name, category_id))
        connection.commit()
    except Error as e:
        print(f"Error al actualizar la categoría: {e}")

def delete_category(connection, category_id):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM categories WHERE id_categories = %s"
        cursor.execute(query, (category_id,))
        connection.commit()
    except Error as e:
        print(f"Error al eliminar la categoría: {e}")
def categories_main(connection):
    selected_products = []  # Lista para almacenar los productos seleccionados
    cursor = connection.cursor()
    while True:
        print("\nMenú:")
        print("1. Listar todos los productos")
        print("2. Listar productos de Marvel")
        print("3. Listar productos de DC")
        print("4. Crear una nueva categoría")
        print("5. Leer categorías")
        print("6. Actualizar categoría")
        print("7. Eliminar categoría")
        print("8. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            products = list_products_by_category(connection, category_id=None)
            if products:
                print("\nListado de todos los productos:")
                for product in products:
                    print(f"ID: {product['id_products']}, Nombre: {product['name']}")
        
        elif choice == "2":
            marvel_category_id = 1
            marvel_products = list_products_by_category(connection, marvel_category_id)

            if marvel_products:
                print("\nListado de productos de Marvel:")
                for product in marvel_products:
                    print(f"ID: {product['id_products']}, Nombre: {product['name']}")

        elif choice == "3":
            dc_category_id = 2
            dc_products = list_products_by_category(connection, dc_category_id)

            if dc_products:
                print("\nListado de productos de DC:")
                for product in dc_products:
                    print(f"ID: {product['id_products']}, Nombre: {product['name']}")


        elif choice == "4":
            name = input("Nombre de la nueva categoría: ")
            create_category(connection, name)
            print("Categoría creada")

        elif choice == "5":
            categories = read_all_categories(connection)
            if categories:
                print("\nListado de categorías:")
                for category in categories:
                    print(f"ID: {category['id']}, Nombre: {category['name']}")

        elif choice == "6":
            category_id = int(input("ID de la categoría a actualizar: "))
            new_name = input("Nuevo nombre: ")
            update_category(connection, category_id, new_name)
            print("Categoría actualizada")

        elif choice == "7":
            category_id = int(input("ID de la categoría a eliminar: "))
            delete_category(connection, category_id)
            print("Categoría eliminada")

        elif choice == "8":
            return None  # Si elige salir, devuelve None
        
        
if __name__ == "__main__":
    connection = create_db_connection()  # Crear la conexión a la base de datos

    if connection:
        categories_main(connection)  # Llamar a la función de gestión de pedidos con la conexión
        close_db_connection(connection)  # Cerrar la conexión a la base de datos cuando hayas terminado
    else:
        print("No se pudo establecer una conexión a la base de datos.")
