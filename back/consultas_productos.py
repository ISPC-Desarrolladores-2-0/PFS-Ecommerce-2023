import sqlite3

class ConsultasProductos:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def buscar_productos(self, término_de_búsqueda):
        # Buscar productos que coincidan con el término de búsqueda
        self.cursor.execute("SELECT * FROM products WHERE name LIKE ? OR description LIKE ?", ('%' + término_de_búsqueda + '%', '%' + término_de_búsqueda + '%'))
        productos = self.cursor.fetchall()
        return productos

    def mostrar_detalles_producto(self, id_producto):
        # Obtener detalles de un producto específico por su ID
        self.cursor.execute("SELECT * FROM products WHERE id_products = ?", (id_producto,))
        producto = self.cursor.fetchone()
        return producto

    def agregar_al_carrito(self, id_producto, cantidad):
        # Lógica para agregar un producto al carrito de compras
        try:
            # Obtener el producto por su ID
            self.cursor.execute("SELECT * FROM products WHERE id_products = ?", (id_producto,))
            producto = self.cursor.fetchone()

            if producto:
                # Calcular el precio total
                precio_unitario = producto[3]  # El precio del producto
                precio_total = precio_unitario * cantidad

                # Agregar el producto al carrito (puedes implementar esta lógica en una tabla separada)
                # Por ejemplo, puedes tener una tabla "carrito" con campos como "id_producto", "cantidad", "precio_total", etc.
                self.cursor.execute("INSERT INTO carrito (id_producto, cantidad, precio_total) VALUES (?, ?, ?)", (id_producto, cantidad, precio_total))
                self.conn.commit()
                return True  # Producto agregado al carrito con éxito
            else:
                return False  # El producto no se encontró en la base de datos

        except sqlite3.Error as e:
            print("Error al agregar al carrito:", e)
            return False  # Error al agregar el producto al carrito

    def ver_carrito(self):
        # Lógica para mostrar el contenido del carrito de compras
        try:
            # Consulta para obtener los productos en el carrito (puedes usar una tabla "carrito")
            self.cursor.execute("SELECT * FROM carrito")
            productos_carrito = self.cursor.fetchall()
            return productos_carrito

        except sqlite3.Error as e:
            print("Error al ver el carrito:", e)
            return []  # Devuelve una lista vacía en caso de error

    def cerrar_conexion(self):
        # Cierra la conexión a la base de datos cuando ya no la necesitas
        self.conn.close()
