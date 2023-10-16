import mysql.connector
from mysql.connector import Error
from connection import create_db_connection, close_db_connection

class Product:
    def __init__(self, id_products, name, description, price, discount, stock, image, pages, formato, weight, isbn, id_categories):
        self.id_products = id_products
        self.name = name
        self.description = description
        self.price = price
        self.discount = discount
        self.stock = stock
        self.image = image
        self.pages = pages
        self.formato = formato
        self.weight = weight
        self.isbn = isbn
        self.id_categories = id_categories
        
    def get_id_products(self):
        return self.id_products

    def set_id_products(self, id_products):
        self.id_products = id_products

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_discount(self):
        return self.discount

    def set_discount(self, discount):
        self.discount = discount

    def get_stock(self):
        return self.stock

    def set_stock(self, stock):
        self.stock = stock

    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = image

    def get_pages(self):
        return self.pages

    def set_pages(self, pages):
        self.pages = pages

    def get_formato(self):
        return self.formato

    def set_formato(self, formato):
        self.formato = formato

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn

    def get_id_categories(self):
        return self.id_categories

    def set_id_categories(self, id_categories):
        self.id_categories = id_categories

def create_product(connection, product):
    try:
        cursor = connection.cursor()
        query = """
            INSERT INTO products
            (name, description, price, discount, stock, image, pages, formato, weight, isbn, id_categories)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (product.name, product.description, product.price, product.discount, product.stock,
                  product.image, product.pages, product.formato, product.weight, product.isbn, product.id_categories)
        cursor.execute(query, values)
        connection.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error al crear un producto: {e}")
        return None

def read_all_products(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM products"
        cursor.execute(query)
        products = []

        for row in cursor.fetchall():
            product = Product(*row)
            products.append(product)

        return products
    except Error as e:
        print(f"Error al leer productos: {e}")

def update_product(connection, product):
    try:
        cursor = connection.cursor()
        query = """
            UPDATE products
            SET name = %s, description = %s, price = %s, discount = %s, stock = %s,
                image = %s, pages = %s, formato = %s, weight = %s, isbn = %s, id_categories = %s
            WHERE id_products = %s
        """
        values = (product.name, product.description, product.price, product.discount, product.stock,
                  product.image, product.pages, product.formato, product.weight, product.isbn,
                  product.id_categories, product.id_products)
        cursor.execute(query, values)
        connection.commit()
    except Error as e:
        print(f"Error al actualizar el producto: {e}")

def delete_product(connection, product_id):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM products WHERE id_products = %s"
        cursor.execute(query, (product_id,))
        connection.commit()
    except Error as e:
        print(f"Error al eliminar el producto: {e}")
        

def print_product(product):
    print("\nDetalles del producto:")
    print(f"ID: {product.get_id_products()}")
    print(f"Nombre: {product.get_name()}")
    print(f"Descripción: {product.get_description()}")
    print(f"Precio: {product.get_price()}")
    print(f"Descuento (%): {product.get_discount()}")
    print(f"Stock: {product.get_stock()}")
    print(f"Imagen: {product.get_image()}")
    print(f"Número de páginas: {product.get_pages()}")
    print(f"Formato: {product.get_formato()}")
    print(f"Peso (kg): {product.get_weight()}")
    print(f"ISBN: {product.get_isbn()}")
    print(f"ID de categoría: {product.get_id_categories()}")

def read_product_by_id(connection, product_id):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM products WHERE id_products = %s"
        cursor.execute(query, (product_id,))
        row = cursor.fetchone()

        if row:
            return Product(*row)
        else:
            print("Producto no encontrado")
            return None
    except Error as e:
        print(f"Error al leer producto por ID: {e}")
        return None

def list_of_products(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT id_products, name, price, stock FROM products"
        cursor.execute(query)
        products = cursor.fetchall()

        if products:
            print("\nListado de productos por ID, Nombre, Precio y Stock:")
            for product in products:
                product_id, name, price, stock = product
                print(f"ID: {product_id}, Nombre: {name}, Precio: {price}, Stock: {stock}")
        else:
            print("No hay productos disponibles.")
    except Error as e:
        print(f"Error al obtener la lista de productos: {e}")

def manage_products(connection):
    while True:
        print("\nMenú:")
        print("1. Crear producto")
        print("2. Leer productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Lista de productos")  
        print("6. Salir")  

        choice = input("Selecciona una opción: ")
        if choice == "1":
            # Crear producto
            name = input("Nombre del producto: ")
            description = input("Descripción del producto: ")
            price = float(input("Precio del producto: "))
            discount = int(input("Descuento (%): "))
            stock = int(input("Cantidad en stock: "))
            image = input("Ruta de la imagen: ")
            pages = int(input("Número de páginas: "))
            formato = input("Formato: ")
            weight = float(input("Peso (kg): "))
            isbn = input("ISBN: ")
            id_categories = int(input("ID de categoría: "))

            new_product = Product(None, name, description, price, discount, stock, image, pages, formato, weight, isbn, id_categories)
            product_id = create_product(connection, new_product)
            if product_id:
                print(f"Producto creado con ID: {product_id}")

        elif choice == "2":
            # Leer productos
            products = read_all_products(connection)
            if products:
                print("\nListado de productos:")
                for product in products:
                    print_product(product)

        elif choice == "3":
            # Actualizar producto
            product_id = int(input("ID del producto a actualizar: "))
            product_to_update = read_product_by_id(connection, product_id)
            if product_to_update:
                print(f"Producto a actualizar:")
                print_product(product_to_update)
                name = input("Nuevo nombre (dejar en blanco para mantener el mismo): ")
                description = input("Nueva descripción (dejar en blanco para mantener la misma): ")
                price = float(input("Nuevo precio (0 para mantener el mismo): "))
                discount = int(input("Nuevo descuento (%): ").strip()) if input("Nuevo descuento (%): ").strip() else product_to_update.discount
                stock = int(input("Nueva cantidad en stock (0 para cambiar a cero): ").strip())


                image = input("Nueva ruta de la imagen (dejar en blanco para mantener la misma): ")
                pages = int(input("Nuevo número de páginas (0 para mantener el mismo): "))
                formato = input("Nuevo formato (dejar en blanco para mantener el mismo): ")
                weight = float(input("Nuevo peso (kg) (0 para mantener el mismo): "))
                isbn = input("Nuevo ISBN (dejar en blanco para mantener el mismo): ")
                id_categories = int(input("Nuevo ID de categoría (0 para mantener el mismo): "))

                if name:
                    product_to_update.name = name
                if description:
                    product_to_update.description = description
                if price > 0:
                    product_to_update.price = price
                if discount >= 0:
                    product_to_update.discount = discount
                if stock >= 0:
                    product_to_update.stock = stock
                if image:
                    product_to_update.image = image
                if pages > 0:
                    product_to_update.pages = pages
                if formato:
                    product_to_update.formato = formato
                if weight > 0:
                    product_to_update.weight = weight
                if isbn:
                    product_to_update.isbn = isbn
                if id_categories > 0:
                    product_to_update.id_categories = id_categories

                update_product(connection, product_to_update)
                print("Producto actualizado")

        elif choice == "4":
            # Eliminar producto
            product_id = int(input("ID del producto a eliminar: "))
            delete_product(connection, product_id)
            print("Producto eliminado")

        elif choice == "5":
            # Lista de productos (List of products)
            list_of_products(connection)

        elif choice == "6":
            break
        
        
if __name__ == "__main__":
    connection = create_db_connection()

    if connection:
        manage_products(connection)
        close_db_connection(connection)
    else:
        print("No se pudo establecer una conexión a la base de datos.")
