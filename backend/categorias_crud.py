import mysql.connector
from mysql.connector import Error
from connection import create_db_connection

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

if __name__ == "__main__":
    connection = create_db_connection()
    
    if not connection:
        exit()

    while True:
        print("\nMenú de Categorías:")
        print("1. Crear una nueva categoría")
        print("2. Leer categorías")
        print("3. Actualizar categoría")
        print("4. Eliminar categoría")
        print("5. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            name = input("Nombre de la nueva categoría: ")
            create_category(connection, name)
            print("Categoría creada")

        elif choice == "2":
            categories = read_all_categories(connection)
            if categories:
                print("\nListado de categorías:")
                for category in categories:
                    print(f"ID: {category['id']}, Nombre: {category['name']}")

        elif choice == "3":
            category_id = int(input("ID de la categoría a actualizar: "))
            new_name = input("Nuevo nombre: ")
            update_category(connection, category_id, new_name)
            print("Categoría actualizada")

        elif choice == "4":
            category_id = int(input("ID de la categoría a eliminar: "))
            delete_category(connection, category_id)
            print("Categoría eliminada")

        elif choice == "5":
            break
