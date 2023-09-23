from consultas_productos import ConsultasProductos

def buscar_productos(consultas_productos):
    término_de_búsqueda = input("Ingrese el término de búsqueda: ")
    resultados = consultas_productos.buscar_productos(término_de_búsqueda)
    if resultados:
        for producto in resultados:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Precio: {producto[3]}")
        # Permitir al usuario agregar productos al carrito
        id_producto = input("Ingrese el ID del producto que desea agregar al carrito: ")
        cantidad = int(input("Ingrese la cantidad que desea agregar: "))
        if consultas_productos.agregar_al_carrito(id_producto, cantidad):
            print("Producto agregado al carrito con éxito.")
        else:
            print("No se pudo agregar el producto al carrito.")
    else:
        print("No se encontraron resultados.")
