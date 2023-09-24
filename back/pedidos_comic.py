class Pedido:
    def __init__(self, id_pedido, fecha_pedido, id_usuario, detalle):
        self.id_pedido = id_pedido
        self.fecha_pedido = fecha_pedido
        self.id_usuario = id_usuario
        self.detalle = detalle

    def calcular_total(self):
        total = 0
        for producto, cantidad, precio_unitario in self.detalle:
            total += cantidad * precio_unitario
        return total

    def mostrar_detalle(self):
        print("Detalle del pedido:")
        for producto, cantidad, precio_unitario in self.detalle:
            print(f"Producto: {producto}, Cantidad: {cantidad}, Precio Unitario: {precio_unitario}")

# Función para crear un nuevo pedido
def crear_pedido():
    id_pedido = int(input("Ingrese el ID del pedido: "))
    fecha_pedido = input("Ingrese la fecha del pedido: ")
    id_usuario = int(input("Ingrese el ID del usuario: "))
    detalle = []

    while True:
        producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if producto.lower() == "fin":
            break
        cantidad = int(input("Ingrese la cantidad: "))
        precio_unitario = float(input("Ingrese el precio unitario: "))
        detalle.append((producto, cantidad, precio_unitario))

    pedido = Pedido(id_pedido, fecha_pedido, id_usuario, detalle)
    pedidos.append(pedido)
    print("Pedido creado exitosamente!")

# Función para listar todos los pedidos
def listar_pedidos():
    if not pedidos:
        print("No se ha realizado ningún pedido.")
        print("ingrese al sector pedidos.")
    else:
        for idx, pedido in enumerate(pedidos, start=1):
           print(f"Pedido {idx}:")
           print(f"ID del Pedido: {pedido.id_pedido}")
           print(f"Fecha del Pedido: {pedido.fecha_pedido}")
           print(f"ID del Usuario: {pedido.id_usuario}")
           pedido.mostrar_detalle()
           print(f"Total del Pedido: ${pedido.calcular_total()}")
           print()

# Lista para almacenar los pedidos
pedidos = []

# Menú principal

def menu_pedidos():
    while True:
        print("\n--- TIENDA DE COMIC PLANET SUPERHEROES ---")
        print("\n--- SECCION PEDIDOS ---")
        print("\n--- MENU PRINCIPAL ---")
        print("1. Crear Pedido")
        print("2. Listar Pedidos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            crear_pedido()
        elif opcion == '2':
            listar_pedidos()
        elif opcion == '3':
            print("¡Sr. usuario ud salio del sector pedido,Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    
menu_pedidos()
