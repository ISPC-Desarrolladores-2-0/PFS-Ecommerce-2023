from connection import create_db_connection
from mysql.connector import Error

class User:
    def __init__(self, id_users, first_name, last_name, email, password, address, image):
        self.id_users = id_users
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.address = address
        self.image = image

        
    def get_id_users(self):
        return self.id_users

   
    def set_id_users(self, id_users):
        self.id_users = id_users

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = image
        
def create_user(connection, user):
    try:
        cursor = connection.cursor()
        query = """
            INSERT INTO users
            (first_name, last_name, email, password, address, image)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (user.first_name, user.last_name, user.email, user.password, user.address, user.image)
        cursor.execute(query, values)
        connection.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error al crear un usuario: {e}")
        return None

def read_all_users(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM users"
        cursor.execute(query)
        users = []

        for row in cursor.fetchall():
            user = User(*row)
            users.append(user)

        return users
    except Error as e:
        print(f"Error al leer usuarios: {e}")

def read_user_by_id(connection, user_id):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id_users = %s"
        cursor.execute(query, (user_id,))
        row = cursor.fetchone()

        if row:
            return Usuario(*row)
        else:
            print("Usuario no encontrado")
            return None
    except Error as e:
        print(f"Error al leer usuario por ID: {e}")
        return None

def update_user(connection, user):
    try:
        cursor = connection.cursor()
        query = """
            UPDATE users
            SET first_name = %s, last_name = %s, email = %s, password = %s, address = %s, image = %s
            WHERE id_users = %s
        """
        values = (user.first_name, user.last_name, user.email, user.password, user.address, user.image, user.id_users)
        cursor.execute(query, values)
        connection.commit()
    except Error as e:
        print(f"Error al actualizar el usuario: {e}")

def delete_user(connection, user_id):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM users WHERE id_users = %s"
        cursor.execute(query, (user_id,))
        connection.commit()
    except Error as e:
        print(f"Error al eliminar el usuario: {e}")
        
        

def read_user_by_id(connection, user_id):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id_users = %s"
        cursor.execute(query, (user_id,))
        row = cursor.fetchone()

        if row:
            return User(*row)
        else:
            print("Usuario no encontrado")
            return None
    except Error as e:
        print(f"Error al leer usuario por ID: {e}")
        return None

def is_valid_string(value):
    return bool(value.strip())

def is_valid_email(value):
    return "@" in value

def is_valid_password(value):
    return len(value) >= 6

def is_valid_role(value):
    return value.lower() in ["admin", "user"]

def print_user(user):
    print("\nDetalles del usuario:")
    print(f"ID: {user.id_users}")
    print(f"Nombre: {user.first_name} {user.last_name}")
    print(f"Correo electrónico: {user.email}")
    print(f"Dirección: {user.address}")
    print(f"Imagen: {user.image}")


def manage_users(connection):
    while True:
        print("\nMenú:")
        print("1. Crear usuario")
        print("2. Leer usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            first_name = input("Primer nombre: ")
            last_name = input("Apellido: ")
            while not is_valid_string(first_name) or not is_valid_string(last_name):
                print("El nombre y el apellido no pueden estar en blanco.")
                first_name = input("Primer nombre: ")
                last_name = input("Apellido: ")

            email = input("Correo electrónico: ")
            while not is_valid_email(email):
                print("El correo electrónico no es válido.")
                email = input("Correo electrónico: ")

            password = input("Contraseña (mínimo 6 caracteres): ")
            while not is_valid_password(password):
                print("La contraseña debe tener al menos 6 caracteres.")
                password = input("Contraseña (mínimo 6 caracteres): ")

            address = input("Dirección: ")
            while not is_valid_string(address):
                print("La dirección no puede estar en blanco.")
                address = input("Dirección: ")

            image = input("Imagen: ")
            while not is_valid_string(image):
                print("La imagen no puede estar en blanco.")
                image = input("Imagen: ")

            new_user = User(None, first_name, last_name, email, password, address, image)
            user_id = create_user(connection, new_user)
            if user_id:
                print(f"Usuario creado con ID: {user_id}")
            else:
                print("Error al crear el usuario")

        elif choice == "2":
            users = read_all_users(connection)
            if users:
                print("\nListado de usuarios:")
                for user in users:
                    print_user(user)
            else:
                print("No hay usuarios registrados.")

        elif choice == "3":
            user_id = input("ID del usuario a actualizar: ")
            if user_id.isdigit():
                user_id = int(user_id)
                user_to_update = read_user_by_id(connection, user_id)
                if user_to_update:
                    print(f"Usuario a actualizar:")
                    print_user(user_to_update)

                    first_name = input(f"Nuevo primer nombre (deja en blanco para mantener el mismo: {user_to_update.first_name}): ")
                    last_name = input(f"Nuevo apellido (deja en blanco para mantener el mismo: {user_to_update.last_name}): ")
                    email = input(f"Nuevo correo electrónico (deja en blanco para mantener el mismo: {user_to_update.email}): ")
                    password = input("Nueva contraseña (deja en blanco para mantener la misma): ")

                    address = input(f"Nueva dirección (deja en blanco para mantener el mismo: {user_to_update.address}): ")
                    while not is_valid_string(address):
                        print("La dirección no puede estar en blanco.")
                        address = input("Dirección: ")

                    image = input(f"Nueva imagen (deja en blanco para mantener la misma: {user_to_update.image}): ")
                    while not is_valid_string(image):
                        print("La imagen no puede estar en blanco.")
                        image = input("Imagen: ")

                    if is_valid_string(first_name):
                        user_to_update.first_name = first_name
                    if is_valid_string(last_name):
                        user_to_update.last_name = last_name
                    if is_valid_email(email):
                        user_to_update.email = email
                    if is_valid_password(password):
                        user_to_update.password = password
                    if is_valid_string(address):
                        user_to_update.address = address
                    if is_valid_string(image):
                        user_to_update.image = image

                    update_user(connection, user_to_update)
                    print("Usuario actualizado")

                else:
                    print("Usuario no encontrado.")

            else:
                print("ID de usuario no válido.")

        elif choice == "4":
            user_id = input("ID del usuario a eliminar: ")
            if user_id.isdigit():
                user_id = int(user_id)
                delete_user(connection, user_id)
                print("Usuario eliminado")
            else:
                print("ID de usuario no válido.")

        elif choice == "5":
            break