# Otra forma de hacer las validaciones del registro de usuarios
import re

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.password = password
        self.email = email

    def user_register(self):
        while True:
            print("\n•·.·•·.·•·.·•·.·• Ingresa los siguientes datos: •·.·•·.·•·.·•·.·•\n")
            self.username = input('Username: ')
            self.password = input('Password: ')
            self.email = input('Email: ')

            if self.validate_username() and self.validate_password() and self.validate_email():
                user = User(self.username, self.email, self.password)
                print("\n•·.·•·.·•·.·•·.·• Tu cuenta ha sido registrada con éxito. •·.·•·.·•·.·•·.·•\n")
                return user
            else:
                print("\n•·.·•·.·•·.·•·.·• No se pudo registrar tu cuenta. Intente nuevamente. •·.·•·.·•·.·•·.·•\n")
            
        
# valido el nombre de usuario que ingresa
    def validate_username(self):
        if len(self.username) == 0:
            print("El nombre de usuario no puede estar en blanco.")
            return False
        if len(self.username) >= 3:
            return True
        else:
            print("El nombre de usuario debe tener al menos 3 caracteres.")
            return False
        
# valido la contraseña que ingresa
    def validate_password(self):
        if len(self.password) >= 6:
            return True
        else:
            print("La contraseña debe tener al menos 6 caracteres.")
            return False

# valido el correo que ingresa
    def validate_email(self):
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(email_regex, self.email):
            return True
        else:
            print("Correo no válido, debe tener un @ y un punto.")
            return False


user = User("JohnDoe", "johndoe@example.com", "password")
user.user_register()