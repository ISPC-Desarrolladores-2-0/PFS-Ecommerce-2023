import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

class categories:
    id_categories = 0
    name_categories = " "

    def __init__(self, id_categories, name_categories, add_comic_categories, eliminate_comic_categories):
        self.id_categories = id_categories
        self.name_categories = name_categories
        self.add_comic_categories = add_comic_categories
        self.eliminate_comic_categories = eliminate_comic_categories

    def get_id_categories(self):
        return self.id_categories
        
    def set_id_categories(self, id_categories):
        self.id_categories = id_categories

    def get_name_categories(self,):
        return self.name_categories
        
    def set_name_categories(self, name_categories):
        self.name_categories = name_categories

    def get_add_comic_categories(self):
        return self.add_comic_categories
        
    def set_add_comic_categories(self, add_comic_categories):
        self.add_comic_categories = add_comic_categories

    def get_eliminate_comic_categories(self):
        return self.eliminate_comic_categories
        
    def set_eliminate_comic_categories(self, eliminate_comic_categories):
        self.eliminate_comic_categories = eliminate_comic_categories
        
    def get_filter_list_categories(self):
        return self.filter_list_categories
        
    def set_filter_list_categories(self, filter_list_categories):
        self.filter_list_categoryies = filter_list_categories

#Coneccion a la base de datos
    
    # def create_db_connection():
    #     try:
    #         connection = mysql.connector.connect(
    #         host='localhost',
    #         user='root',
    #         password='',
    #         database='planetSuperheroesDB'
    #     )
    #         if connection.is_connected():
    #             print("Conexión a la base de datos exitosa")
    #         return connection
    #     except Error as e:
    #         print(f"Error durante la conexión a la base de datos: {e}")
    #     return None

    # def close_conexion(self):
    #     if self.conexion.is_connected():
    #         self.conexion.close()

#Filtro del producto por categoria

    def products_categories_filter(self, name_categories):
        try:
            cursor = self.conexion.cursor(dictionary=True)
            query = """
                        SELECT p.id_products, p.name, p.description, p.price, p.stock, p.image 
                        FROM products p
                        INNER JOIN categories c ON p.id_categories = c.id_categories
                        WHERE c.name_categories = %s
                        ORDER BY p.name
                    """
            cursor.execute(query, (name_categories))
            products = cursor.fetchall()
            cursor.close()
            return products
        except Error as err:
            print(f"Error al filtrar productos por categoría: {err}")
            return []

#Lista del producto por categoria

    def list_products_categories(self):
        try:
            cursor = self.conexion.cursor(dictionary=True)
            query = """
                        SELECT c.name_categories, p.id_products, p.name, p.description,p.price, p.stock, p.image
                        FROM categories c
                        LEFT JOIN products p ON c.id_categories = p.id_categories
                        ORDER BY c.name_categories, p.name
                    """
            cursor.execute(query)
            products = cursor.fetchall()
            cursor.close()
            return products
        except Error as err:
            print(f"Error al listar todos los productos por categoría: {err}")
            return []

#Creador de categoria

    def create_categories(self, name):
        try:
            cursor = self.conexion.cursor()
            query = "INSERT INTO categories (name) VALUES(%s)"
            cursor.execute(query, (name,))
            self.conexion.commit()
            cursor.close()
            return True
        except Error as err:
            print(f"Error al crear la categoría: {err}")
            return False

    def read_categories(self):
        try:
            cursor = self.conexion.cursor()
            query = "SELECT * FROM categories ORDER BY name"
            cursor.execute(query)
            categories = cursor.fetchall()
            cursor.close()
            return categories
        except mysql.connector.Error as err:
            print(f"Error al leer las categorías: {err}")
            return []

    def filter_products_by_categories(self, name_categories):
        try:
            cursor =self.conexion.cursor(dictionary=True)
            query = """
                        SELECT p.id_products, p.name, p.price, p.description 
                        FROM products p
                        INNER JOIN categories c ON p.id_categories = c.id_categories
                        WHERE c.name = %s
                        ORDER BY p.name
                    """
            cursor.execute (query, (name_categories,))
            products = cursor.fetchall()
            cursor.close()
            return products
        except mysql.connector.Error as err:
            print(f"Error al filtrar productos por categoria:{err}")
        return []

    def list_products_by_category(self):
        try:
            cursor = self.conexion.cursor(dictionary=True)
            query = """
                        SELECT c.name AS categories, p.name, p.price, p.description
                        FROM products p
                        INNER JOIN categories c ON p.id_categories = c.id_categories
                        ORDER BY c.name, p.name
                    """
            cursor.execute(query)
            products = cursor.fetchall()
            cursor.close()
            return products
        except mysql.connector.Error as err:
            print(f"Error al listar todos los productos por categoría: {err}")
        return []
    
    def prog_categories():
        host='localhost',
        user='root',
        password='',
        database='planetSuperheroesDB'
    
        categories = categories(host, user, password, database)

        while True:
            print("\n Menú de Categorías:")
            print("1. Filtrar Productos por Categoría (Marvel)")
            print("2. Filtrar Productos por Categoría (DC)")
            print("3. Listar todos los Productos por Categoría")
            print("0. Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                products_marvel = categories.filter_products_by_categories("Marvel")
            
            elif products_marvel:
                print(tabulate(products_marvel, headers="keys", tablefmt="fancy_grid"))
            else:
                print("No se encontraron productos en la categoría Marvel.")
            
            if opcion == "2":
                products_dc = categories.filter_products_by_categories("DC")
            
            elif products_dc:
                print(tabulate(products_dc, headers="keys", tablefmt="fancy_grid"))
            else:
                print("No se encontraron productos en la categoría DC.")

            if opcion == "3":
                all_products = categories.list_products_by_category()
            
            elif all_products:
                print(tabulate(all_products, headers="keys", tablefmt="fancy_grid"))
            else:
                print("No se encontraron productos en ninguna categoría.")
            
            if opcion == "0":
                categories.cerrar_conexion()
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    if __name__ == "__main__":
        prog_categories()   
