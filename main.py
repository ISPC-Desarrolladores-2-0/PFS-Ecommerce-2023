# Definición de las clases Usuario, Pedido, Producto, Categoria y Facturacion
class Usuario:
    def __init__(self, dni, nombre, apellido, email, contraseña):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.pedidos = []

    # Métodos de Usuario aquí

class Pedido:
    def __init__(self, id_pedido, fecha_pedido, id_usuario):
        self.id_pedido = id_pedido
        self.fecha_pedido = fecha_pedido
        self.id_usuario = id_usuario
        self.productos = []

    # Métodos de Pedido aquí

class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio, stock, imagen, categoria):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.imagen = imagen
        self.categoria = categoria
        self.pedidos = []

    # Métodos de Producto aquí

class Categoria:
    def __init__(self, id_categoria, nombre_categoria):
        self.id_categoria = id_categoria
        self.nombre_categoria = nombre_categoria
        self.productos = []

    # Métodos de Categoria aquí

class Facturacion:
    def __init__(self, id_factura, nombre, apellido, dni, direccion, numero_de_calle, localidad, metodo_de_pago):
        self.id_factura = id_factura
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.numero_de_calle = numero_de_calle
        self.localidad = localidad
        self.metodo_de_pago = metodo_de_pago
        self.pedido = None

    # Métodos de Facturacion aquí

# Creación de instancias de las clases
usuario1 = Usuario(12345678, "John", "Doe", "john.doe@example.com", "contraseña123")
pedido1 = Pedido(1, "2023-09-23", usuario1.dni)
producto1 = Producto(1, "Comic A", "Descripción del Comic A", 9.99, 100, "imagen1.jpg", None)
categoria1 = Categoria(1, "Superhéroes")
facturacion1 = Facturacion(1, "John", "Doe", usuario1.dni, "123 Calle Principal", 42, "Ciudad Ejemplo", "Tarjeta de crédito")

# Establecimiento de relaciones
usuario1.pedidos.append(pedido1)
pedido1.productos.append(producto1)
categoria1.productos.append(producto1)
facturacion1.pedido = pedido1

# Ejemplo de uso de las clases
print(f"Usuario: {usuario1.nombre} {usuario1.apellido}")
print(f"Pedidos de {usuario1.nombre}: {len(usuario1.pedidos)}")

print(f"Pedido #{pedido1.id_pedido} ({pedido1.fecha_pedido}):")
print(f"Productos en el pedido: {', '.join([producto.nombre for producto in pedido1.productos])}")

print(f"Producto en la categoría {categoria1.nombre_categoria}: {', '.join([producto.nombre for producto in categoria1.productos])}")

print(f"Facturación para {facturacion1.nombre} {facturacion1.apellido}:")
print(f"Dirección de facturación: {facturacion1.direccion}, {facturacion1.numero_de_calle}, {facturacion1.localidad}")
print(f"Método de pago: {facturacion1.metodo_de_pago}")
