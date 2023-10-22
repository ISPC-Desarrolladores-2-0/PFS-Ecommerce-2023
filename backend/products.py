import mysql.connector
from mysql.connector import Error
from categories import Category
from tabulate import tabulate


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


def get_categories(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM categories"
        cursor.execute(query)
        categories = []

        for row in cursor.fetchall():
            category = Category(*row)
            categories.append(category)

        return categories
    except Error as e:
        print(f"Error al obtener las categorías: {e}")


def select_valid_category(connection):
    cursor = connection.cursor()
    while True:
        print("Categorías disponibles:")
        categories = get_categories(connection)
        for category in categories:
            print(f"{category.id_categories}: {category.name}")

        category_id = input("Selecciona el ID de la categoría: ")

        if category_id.isdigit():
            category_id = int(category_id)

            check_category_query = "SELECT id_categories FROM categories WHERE id_categories = %s"
            cursor.execute(check_category_query, (category_id,))

            if cursor.fetchone():
                return category_id
            else:
                print(
                    "ID de categoría no válido. La categoría no existe en la base de datos.")
        else:
            print("ID de categoría no válido. Debe ser un número entero.")


def create_product(connection, product):
    try:
        cursor = connection.cursor()

        print("Categorías disponibles:")
        category_id = select_valid_category(connection)
        insert_query = """
            INSERT INTO products
            (name, description, price, discount, stock, image,
             pages, formato, weight, isbn, id_categories)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (product.name, product.description, product.price, product.discount, product.stock,
                  product.image, product.pages, product.formato, product.weight, product.isbn, category_id)

        cursor.execute(insert_query, values)
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

        print("Categorías disponibles:")
        category_id = select_valid_category(connection)

        if category_id == 0:
            category_id = product.id_categories
        else:
            try:
                category_id = int(category_id)

                check_category_query = "SELECT id_categories FROM categories WHERE id_categories = %s"
                cursor.execute(check_category_query, (category_id,))

                if cursor.fetchone():
                    product.id_categories = category_id
                else:
                    print(
                        "ID de categoría no válido. La categoría no existe en la base de datos.")
            except ValueError:
                print(
                    "ID de categoría no válido. Debe ser un número entero o 0 para mantener la misma categoría.")

        update_query = """
            UPDATE products
            SET name = %s, description = %s, price = %s, discount = %s, stock = %s,
                image = %s, pages = %s, formato = %s, weight = %s, isbn = %s, id_categories = %s
            WHERE id_products = %s
        """
        values = (product.name, product.description, product.price, product.discount, product.stock,
                  product.image, product.pages, product.formato, product.weight, product.isbn,
                  product.id_categories, product.id_products)

        cursor.execute(update_query, values)
        connection.commit()
        return product.id_products
    except Error as e:
        print(f"Error al actualizar el producto: {e}")
        return None


def delete_product(connection, product_id):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM products WHERE id_products = %s"
        cursor.execute(query, (product_id,))
        connection.commit()
    except Error as e:
        print(f"Error al eliminar el producto: {e}")


def print_product(product):
    print("\n****************************")
    print("Detalles del producto:")
    print("****************************")
    print(f"\nID: {product.id_products}")
    print(f"Nombre: {product.name}")
    print(f"Descripción: {product.description}")
    print(f"Precio: {product.price}")
    print(f"Descuento (%): {product.discount}")
    print(f"Stock: {product.stock}")
    print(f"Imagen: {product.image}")
    print(f"Número de páginas: {product.pages}")
    print(f"Formato: {product.formato}")
    print(f"Peso (kg): {product.weight}")
    print(f"ISBN: {product.isbn}")
    print(f"ID de categoría: {product.id_categories}")
    print("****************************")


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


def is_valid_string(value):
    return bool(value.strip())


def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_valid_discount(value):
    return value.isdigit() and 0 <= int(value) <= 100


def is_valid_stock(value):
    return value.isdigit() and int(value) >= 0


def is_valid_pages(value):
    return value.isdigit() and int(value) > 0


def is_valid_weight(value):
    return is_valid_number(value) and float(value) > 0


def is_valid_id_categories(value):
    return value.isdigit() and int(value) > 0


def print_products_with_stock(products):
    in_stock_products = [product for product in products if product.stock > 0]

    if in_stock_products:
        product_data = []
        for product in in_stock_products:
            product_data.append(
                [product.id_products, product.name, product.stock])

        headers = ["ID", "Nombre", "Stock"]
        table = tabulate(product_data, headers, tablefmt="grid")
        print(table)
    else:
        print("No hay productos disponibles en stock.")


def manage_products(connection):
    while True:
        print("\nMenú:")
        print("1. Crear producto")
        print("2. Ver productos en stock")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Informacion completa de productos")
        print("6. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            name = input("Nombre del producto: ").lower()
            while not name:
                print("El nombre no puede estar en blanco.")
                name = input("Nombre del producto: ").lower()

            description = input("Descripción del producto: ").lower()
            while not description:
                print("La descripción no puede estar en blanco.")
                description = input("Descripción del producto: ").lower()

            price = input("Precio del producto: ")
            while not is_valid_number(price):
                print("El precio no es válido. Ingresa un número válido.")
                price = input("Precio del producto: ")

            discount = input("Descuento (%): ")
            while not is_valid_discount(discount):
                print("El descuento no es válido. Ingresa un número entre 0 y 100.")
                discount = input("Descuento (%): ")

            stock = input("Cantidad en stock: ")
            while not is_valid_stock(stock) or int(stock) <= 0:
                if not is_valid_stock(stock):
                    print(
                        "La cantidad en stock no es válida. Ingresa un número válido mayor o igual a 0.")
                else:
                    print("Error: El stock debe ser mayor que cero.")
                stock = input("Cantidad en stock: ")

            image = input("Ruta de la imagen: ").lower()
            while not is_valid_string(image):
                print("La ruta de la imagen no puede estar en blanco.")
                image = input("Ruta de la imagen: ").lower()

            pages = input("Número de páginas: ")
            while not is_valid_pages(pages):
                print(
                    "El número de páginas no es válido. Ingresa un número válido mayor a 0.")
                pages = input("Número de páginas: ")

            formato = input("Formato: ").lower()
            while not is_valid_string(formato):
                print("El formato no puede estar en blanco.")
                formato = input("Formato: ").lower()

            weight = input("Peso (kg): ")
            while not is_valid_weight(weight):
                print("El peso no es válido. Ingresa un número válido mayor a 0.")
                weight = input("Peso (kg): ")

            isbn = input("ISBN: ").lower()
            while not is_valid_string(isbn):
                print("El ISBN no puede estar en blanco.")
                isbn = input("ISBN: ").lower()

            id_categories = input("ID de categoría: ")
            while not is_valid_id_categories(id_categories):
                print(
                    "El ID de categoría no es válido. Ingresa un número válido mayor a 0.")
                id_categories = input("ID de categoría: ")

            if float(stock) > 0:
                new_product = Product(None, name, description, float(price), int(discount), int(stock), image,
                                      int(pages), formato, float(weight), isbn, int(id_categories))
                product_id = create_product(connection, new_product)
                if product_id:
                    print(f"Producto creado con ID: {product_id}")
                else:
                    print("Error al crear el producto.")
            else:
                print("No se puede crear un producto con stock no disponible.")
        elif choice == "2":
            products = read_all_products(connection)
            print_products_with_stock(products)

        elif choice == "3":
            while True:
                product_id = input("ID del producto a actualizar: ")
                if product_id.isdigit():
                    product_id = int(product_id)
                    product_to_update = read_product_by_id(
                        connection, product_id)
                    if product_to_update:
                        print(f"Producto a actualizar:")
                        print_product(product_to_update)

                        name = input(
                            "Nuevo nombre : ").lower()
                        while not is_valid_string(name):
                            print("El nombre no puede estar en blanco.")
                            name = input(
                                "Nuevo nombre : ").lower()

                        description = input(
                            "Nueva descripción : ").lower()
                        while not is_valid_string(description):
                            print("La descripción no puede estar en blanco.")
                            description = input(
                                "Nueva descripción : ").lower()

                        price = input(
                            "Nuevo precio : ")
                        while not is_valid_number(price):
                            print(
                                "El precio no es válido. Ingresa un número válido.")
                            price = input(
                                "Nuevo precio : ")

                        discount = input("Nuevo descuento (%): ")
                        while not is_valid_discount(discount):
                            print(
                                "El descuento no es válido. Ingresa un número entre 0 y 100.")
                            discount = input("Nuevo descuento (%): ")

                        stock = input(
                            "Nueva cantidad en stock : ")
                        if stock.strip() and stock.isdigit() and int(stock) < 0:
                            print(
                                "La cantidad en stock no es válida. Ingresa un número válido mayor o igual a 0.")
                        elif stock:
                            product_to_update.stock = int(stock)

                        image = input(
                            "Nueva ruta de la imagen : ").lower()
                        while not is_valid_string(image):
                            print("La ruta de la imagen no puede estar en blanco.")
                            image = input(
                                "Nueva ruta de la imagen : ").lower()

                        pages = input(
                            "Nuevo número de páginas : ")
                        while not is_valid_pages(pages):
                            print(
                                "El número de páginas no es válido. Ingresa un número mayor que 0.")
                            pages = input(
                                "Nuevo número de páginas : ")

                        formato = input(
                            "Nuevo formato : ").lower()
                        while not is_valid_string(formato):
                            print("El formato no puede estar en blanco.")
                            formato = input(
                                "Nuevo formato : ").lower()

                        weight = input(
                            "Nuevo peso (kg) : ")
                        if weight.strip() and not is_valid_weight(weight):
                            print(
                                "El peso no es válido. Ingresa un número mayor que 0.")
                        elif weight:
                            product_to_update.weight = float(weight)

                        isbn = input(
                            "Nuevo ISBN : ").lower()
                        while not is_valid_string(isbn):
                            print("El ISBN no puede estar en blanco.")
                            isbn = input(
                                "Nuevo ISBN : ").lower()

                        id_categories = input(
                            "Nuevo ID de categoría : ")
                        while not is_valid_id_categories(id_categories):
                            print(
                                "El ID de categoría no es válido. Ingresa un número válido mayor a 0.")
                            id_categories = input(
                                "Nuevo ID de categoría (0 para mantener el mismo): ")

                        updated_product_id = update_product(
                            connection, product_to_update)
                        if updated_product_id is not None:
                            print(
                                f"Producto actualizado con ID: {updated_product_id}")
                        else:
                            print("Error al actualizar el producto.")
                        break
                    else:
                        print("Producto no encontrado.")
                else:
                    print("ID de producto no válido.")
        elif choice == "4":
            product_id = input("ID del producto a eliminar: ")
            if product_id.isdigit():
                product_id = int(product_id)
                delete_product(connection, product_id)
                print("Producto eliminado")
            else:
                print("ID de producto no válido.")

        elif choice == "5":
            products = read_all_products(connection)
            if products:
                print("\nListado de productos:")
            for product in products:
                if product.stock > 0:
                    print_product(product)
            if all(product.stock == 0 for product in products):
                print("No hay productos disponibles.")

        elif choice == "6":
            break