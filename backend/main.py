from connection import create_db_connection, close_db_connection
from products import Product, create_product, read_all_products, update_product, delete_product, manage_products, read_product_by_id
from users import User, create_user, read_all_users, update_user, delete_user, manage_users, read_user_by_id


def menu_principal():
    menu = True
    while menu == True:
        print("\n•·.·•·.·•·.·•·.·• Menú Principal •·.·•·.·•·.·•·.·•\n")
        print("1. Gestionar Productos")
        print("2. Gestionar Usuarios")
        print("3. Inicio")
        print("4. Quienes Somos?")
        print("5. Contacto")
        print("6. Salir")
        opcion = input("\n⮞ Ingrese una opción: ")

        if opcion == "1":
            # Opción para gestionar productos
            connection = create_db_connection()
            if connection:
                manage_products(connection)
                close_db_connection(connection)
            else:
                print("No se pudo establecer una conexión a la base de datos de productos.")
        
        elif opcion == "2":
            # Opción para gestionar usuarios
            connection = create_db_connection()
            if connection:
                manage_users(connection)
                close_db_connection(connection)
            else:
                print("No se pudo establecer una conexión a la base de datos de usuarios.")
        
        elif opcion == "3":
            print("Sección de Inicio (en construcción)")
        
        elif opcion == "4":
            print("Sección de Quiénes Somos? (en construcción)")
        
        elif opcion == "5":
            print("Sección de Contacto (en construcción)")
        
        elif opcion == "6":
            print("Ha salido del programa. ¡Hasta luego!")
            menu = False
        
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    menu_principal()
