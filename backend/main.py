from connection import create_db_connection, close_db_connection
from products import *
from users import User, create_user, read_all_users, update_user, delete_user, manage_users, read_user_by_id
from categories import *
from orders import *
from facturacion import *

def menu_principal():
    menu = True
    while menu == True:
        print("\n•·.·•·.·•·.·•·.·• Menú Principal •·.·•·.·•·.·•·.·•\n")
        print("1. Gestionar Productos")
        print("2. Gestionar Usuarios")
        print("3. Gestionar Ordenes")
        print("4. Gestionar Facturas")
        print("5. Gestionar Categorias")
        print("6. Salir")
        opcion = input("\n⮞ Ingrese una opción: ")

        if opcion == "1":
            connection = create_db_connection()
            if connection:
                manage_products(connection)
                close_db_connection(connection)
            else:
                print("No se pudo establecer una conexión a la base de datos de productos.")
        
        elif opcion == "2":
            connection = create_db_connection()
            if connection:
                manage_users(connection)
                close_db_connection(connection)
            else:
                print("No se pudo establecer una conexión a la base de datos de usuarios.")
        
        elif opcion == "3":
            connection = create_db_connection()
            if connection:
                manage_orders(connection)
                close_db_connection(connection)
            else:
                print("No se pudo establecer una conexión a la base de datos de órdenes.")

        
        elif opcion == "4":    
                process_billing()
            
        elif opcion == "5":
            print("Sección de Categorías... en construcción")            
            
        
        elif opcion == "6":
            print("Ha salido del programa. ¡Hasta luego!")
            menu = False
        
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    menu_principal()
