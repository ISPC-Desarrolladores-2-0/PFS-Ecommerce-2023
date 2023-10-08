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
        
        
def print_user(user):
    print("\nDetalles del usuario:")
    print(f"ID: {user.get_id_users()}")
    print(f"Nombre: {user.get_first_name()} {user.get_last_name()}")
    print(f"Email: {user.get_email()}")
    print(f"Dirección: {user.get_address()}")
    print(f"Imagen: {user.get_image()}")

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

def manage_users(connection):
    while True:
        print("\nMenú de Usuarios:")
        print("1. Crear usuario")
        print("2. Leer usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            first_name = input("Nombre: ")
            last_name = input("Apellido: ")
            email = input("Email: ")
            password = input("Contraseña: ")
            address = input("Dirección: ")
            image = input("URL de la imagen de perfil: ")

            new_user = User(None, first_name, last_name, email, password, address, image)
            user_id = create_user(connection, new_user)
            if user_id:
                print(f"Usuario creado con ID: {user_id}")

        elif choice == "2":
            users = read_all_users(connection)
            if users:
                print("\nListado de Usuarios:")
                for user in users:
                    print_user(user)

        elif choice == "3":
            user_id = int(input("ID del usuario a actualizar: "))
            user_to_update = read_user_by_id(connection, user_id)
            if user_to_update:
                print(f"Usuario a actualizar:")
                print_user(user_to_update)
                first_name = input("Nuevo nombre (dejar en blanco para mantener el mismo): ")
                last_name = input("Nuevo apellido (dejar en blanco para mantener el mismo): ")
                email = input("Nuevo email (dejar en blanco para mantener el mismo): ")
                password = input("Nueva contraseña (dejar en blanco para mantener la misma): ")
                address = input("Nueva dirección (dejar en blanco para mantener la misma): ")
                image = input("Nueva URL de imagen de perfil (dejar en blanco para mantener la misma): ")

                if first_name:
                    user_to_update.first_name = first_name
                if last_name:
                    user_to_update.last_name = last_name
                if email:
                    user_to_update.email = email
                if password:
                    user_to_update.password = password
                if address:
                    user_to_update.address = address
                if image:
                    user_to_update.image = image

                update_user(connection, user_to_update)
                print("Usuario actualizado")

        elif choice == "4":
            user_id = int(input("ID del usuario a eliminar: "))
            delete_user(connection, user_id)
            print("Usuario eliminado")

        elif choice == "5":
            break