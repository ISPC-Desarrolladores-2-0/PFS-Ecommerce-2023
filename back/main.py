from registro_usuario import Usuario
from consultas_productos import ConsultasProductos
from autenticacion import Autenticacion
from buscar_productos import buscar_productos
import configurar_bd # Importar el script de configuración de la base de datos

# Ejecutar el script para configurar las tablas de la base de datos
configurar_bd.configurar_base_de_datos()

# Resto de tu código sin cambios
def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    email = input("Ingrese su email: ")
    contraseña = input("Ingrese su contraseña: ")
    nuevo_usuario = Usuario(nombre, email, contraseña)
    if nuevo_usuario.crear_cuenta():
        print("Registro exitoso.")
    else:
        print("Error al registrar el usuario.")

def iniciar_sesion():
    email = input("Ingrese su email: ")
    contraseña = input("Ingrese su contraseña: ")
    autenticacion = Autenticacion()
    if autenticacion.iniciar_sesion(email, contraseña):
        print("Sesión iniciada con éxito.")
    else:
        print("Error al iniciar sesión. Verifique sus credenciales.")

def buscar_productos():
    término_de_búsqueda = input("Ingrese el término de búsqueda: ")
    consultas_productos = ConsultasProductos()
    resultados = consultas_productos.buscar_productos(término_de_búsqueda)
    if resultados:
        for producto in resultados:
            print(f"Nombre: {producto[1]}, Descripción: {producto[2]}, Precio: {producto[3]}")
    else:
        print("No se encontraron resultados.")

def ver_carrito():
    consultas_productos = ConsultasProductos()
    carrito = consultas_productos.ver_carrito()
    if carrito:
        print("Contenido del carrito:")
        for item in carrito:
            print(f"Producto: {item[0]}, Cantidad: {item[1]}, Precio Total: {item[2]}")
    else:
        print("El carrito está vacío.")

def menu_principal():
    print("Bienvenido a la tienda de cómics")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Buscar productos")
    print("4. Ver carrito de compras")
    print("5. Salir")

def main():
    while True:
        menu_principal()
        opcion = input("Elija una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            buscar_productos()
        elif opcion == "4":
            ver_carrito()
        elif opcion == "5":
            print("Gracias por usar nuestra tienda. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
