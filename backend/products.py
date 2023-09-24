class Product:
    id_products = ""
    name = ""
    description = ""
    price = 0
    discount = 0
    stock = 0
    image = ""
    pages = 0
    formato = ""
    weight = 0
    isbn = ""
    id_categories = ""

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
        return self.discount_

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
