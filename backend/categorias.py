import mysql.connector
from mysql.connector import Error
from connection import create_db_connection
from products import list_of_products  # Import the list_all_products function from products.py

def list_products_by_category(connection, category_id):
    try:
        if category_id is None:
            return list_of_products(connection)  # Use list_all_products to retrieve all products

        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT p.id_products, p.name, p.price
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

def categories_main():  # Cambiado el nombre de la función a categories_main
    connection = create_db_connection()
    
    if not connection:
        exit()

    while True:
        print("\nMenú:")
        print("1. Listar todos los productos")
        print("2. Listar productos de Marvel")
        print("3. Listar productos de DC")
        print("4. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            products = list_products_by_category(connection, category_id=None)
            if products:
                print("\nListado de todos los productos:")
                for product in products:
                    print(f"ID: {product['id_products']}, Nombre: {product['name']}, Precio: {product['price']}")

        elif choice == "2":
            # Listar productos de Marvel
            marvel_category_id = 1  # Supongamos que Marvel tiene un ID de categoría 1
            marvel_products = list_products_by_category(connection, marvel_category_id)

            if marvel_products:
                print("\nListado de productos de Marvel:")
                for product in marvel_products:
                    print(f"ID: {product['id_products']}, Nombre: {product['name']}, Precio: {product['price']}")
            else:
                print("No hay productos de Marvel disponibles.")

        elif choice == "3":
            # Listar productos de DC
            dc_category_id = 2  # Supongamos que DC tiene un ID de categoría 2
            dc_products = list_products_by_category(connection, dc_category_id)

            if dc_products:
                print("\nListado de productos de DC:")
                for product in dc_products:
                    print(f"ID: {product['id_products']}, Nombre: {product['name']}, Precio: {product['price']}")
            else:
                print("No hay productos de DC disponibles.")

        elif choice == "4":
            connection.close()
            break

if __name__ == "__main__":
    categories_main()
