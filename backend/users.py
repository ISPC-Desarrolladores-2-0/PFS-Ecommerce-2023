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
name = input("Nombre:")
lastName = input("Apellido:")
dni = input("DNI:")
emailAdress = input("Email: ")
password = input("Contraseña: ")
