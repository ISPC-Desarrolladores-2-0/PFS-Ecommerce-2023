import mysql.connector
from mysql.connector import Error
from connection import create_db_connection

class Category:  # Corrección de nombre de clase
    id_category = 0  # Corrección de nombre de atributo
    name = ""  # Corrección de nombre de atributo

    def __init__(self, id_category, name):  # Corrección de nombre de parámetros
        self.id_category = id_category
        self.name = name

    def get_id_category(self):
        return self.id_category

    def set_id_category(self, id_category):
        self.id_category = id_category

    def get_name(self):  # Corrección de nombre de método
        return self.name

    def set_name(self, name):  # Corrección de nombre de método
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

