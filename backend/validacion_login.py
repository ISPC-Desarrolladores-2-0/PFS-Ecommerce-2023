# Otra forma de hacer las validaciones del login de usuarios

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


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
        
# valido la contraseña ingresada
    def validate_password(self):
        if len(self.password) >= 6:
            return True
        else:
            print("La contraseña debe tener al menos 6 caracteres.")
            return False

# valido la contraseña de confirmación ingresada
    def validate_password_confirm(self, password_confirm):
        if self.password == password_confirm:
            return True
        else:
            print("Las contraseñas no coinciden.Intenta nuevamente.")
            return False
        

    def user_login(self):
            while True:
                print("\n•·.·•·.·•·.·•·.·• Ingresa los siguientes datos: •·.·•·.·•·.·•·.·•\n")
                self.username = input('Username: ')
                self.password = input('Password: ')
                password_confirm = input('Password confirmación: ')

                if self.validate_username() and self.validate_password() and self.validate_password_confirm(password_confirm):
                    if self.username == self.username and self.password == password_confirm:
                        user = User(self.username, self.password)
                        print("\n•·.·•·.·•·.·•·.·• Inicio de sesión exitoso! •·.·•·.·•·.·•·.·•\n")
                        return user
                    else:
                        print("\n•·.·•·.·•·.·•·.·• Las contraseñas ingresadas no coinciden. •·.·•·.·•·.·•·.·•\n")
                else:
                    print("\n•·.·•·.·•·.·•·.·• No se pudo iniciar sesión correctamente. Vuelva a intentarlo. •·.·•·.·•·.·•·.·•\n")


user = User("JohnDoe", "password")
user.user_login()