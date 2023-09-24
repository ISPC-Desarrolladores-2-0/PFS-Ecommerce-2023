class pedidos:
    def __init__(self, idProducto, nombre, descripcion, precio, stock, imagen, categoria):
        self.idProducto = idProducto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.imagen = imagen
        self.categoria = categoria

        def getIdProducto(self):
            return self.idProducto
        def getNombre(self):
            return self.nombre
        def getDescripcion(self):
            return self.descripcion
        def getPrecio(self):
            return self.precio
        def getStock(self):
            return self.stock
        def getImagen(self):
            return self.imagen
        def getCategoria(self):
            return self.categoria
        

idProducto = input(int("Id Producto"))
fechaPedido = input ("Fecha de Pedido")
idUsuario = input (int("Id Usuario:"))
detalleTotal = input ("Detalle: ")

