
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

        