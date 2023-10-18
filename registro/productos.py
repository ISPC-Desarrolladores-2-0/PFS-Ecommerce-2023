class Product:
    def __init__(self, id_products, name, description, price, discount, stock, image, pages, formato, weight, isbn, id_categories):
        self._id_products = id_products
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

    @property
    def id_products(self):
        return self._id_products

    @id_products.setter
    def id_products(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("ID de producto debe ser un entero")
        self._id_products = value

    # Definir propiedades similares para otros atributos

    # Resto del código de la clase