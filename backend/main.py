from connection import create_db_connection, close_db_connection
from products import Product, create_product, read_all_products, update_product, delete_product, manage_products, read_product_by_id

if __name__ == "__main__":
    connection = create_db_connection()
    
    if connection:
        manage_products(connection)
        close_db_connection(connection)
    else:
        print("No se pudo establecer una conexión a la base de datos.")