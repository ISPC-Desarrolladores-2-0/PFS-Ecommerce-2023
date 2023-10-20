import mysql.connector
from tabulate import tabulate

class Categoria:
    def __init__(self, host, user, password, database):
        self.conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def cerrar_conexion(self):
        if self.conexion.is_connected():
            self.conexion.close()

    def filtrar_productos_por_categoria(self, nombre_categoria):
        try:
            cursor = self.conexion.cursor(dictionary=True)
            consulta = """
                SELECT p.id_products, p.name, p.price, p.description
                FROM products p
                INNER JOIN categories c ON p.id_categories = c.id_categories
                WHERE c.name = %s
                ORDER BY p.name
            """
            cursor.execute(consulta, (nombre_categoria,))
            productos = cursor.fetchall()
            cursor.close()
            return productos
        except mysql.connector.Error as err:
            print(f"Error al filtrar productos por categoría: {err}")
            return []

    def listar_todos_los_productos_por_categoria(self):
        try:
            cursor = self.conexion.cursor(dictionary=True)
            consulta = """
                SELECT c.name AS categoria, p.name, p.price, p.description
                FROM products p
                INNER JOIN categories c ON p.id_categories = c.id_categories
                ORDER BY c.name, p.name
            """
            cursor.execute(consulta)
            productos = cursor.fetchall()
            cursor.close()
            return productos
        except mysql.connector.Error as err:
            print(f"Error al listar todos los productos por categoría: {err}")
            return []

def def_prog_category():
    host = "tu_host"
    user = "tu_usuario"
    password = "tu_contraseña"
    database = "planetSuperheroesDB"
    categoria = Categoria(host, user, password, database)
    while True:
        print("\nMenú de Categorías:")
        print("1. Filtrar Productos por Categoría (Marvel)")
        print("2. Filtrar Productos por Categoría (DC)")
        print("3. Listar todos los Productos por Categoría")
        print("0. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            productos_marvel = categoria.filtrar_productos_por_categoria("Marvel")
            if productos_marvel:
                print(tabulate(productos_marvel, headers="keys", tablefmt="fancy_grid"))
            else:
                print("No se encontraron productos en la categoría Marvel.")
        elif opcion == "2":
            productos_dc = categoria.filtrar_productos_por_categoria("DC")
            if productos_dc:
                print(tabulate(productos_dc, headers="keys", tablefmt="fancy_grid"))
            else:
                print("No se encontraron productos en la categoría DC.")
        elif opcion == "3":
            productos_todos = categoria.listar_todos_los_productos_por_categoria()
            if productos_todos:
                print(tabulate(productos_todos, headers="keys", tablefmt="fancy_grid"))
            else:
                print("No se encontraron productos en ninguna categoría.")
        elif opcion == "0":
            categoria.cerrar_conexion()
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    def_prog_category()
