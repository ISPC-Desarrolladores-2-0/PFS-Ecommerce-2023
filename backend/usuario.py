class Usuario:
    dni = 0
    name = ""
    lastName = ""
    emailAdress = ""
    password = ""

    def __init__(self, dni, name, lastName, emailAdress, password):
        self.dni = dni
        self.name = name
        self.lastName = lastName
        self.emailAdress = emailAdress
        self.password = password

        def getDni(self):
            return self.dni

        def getName(self):
            return self.name

        def getLastName(self):
            return self.lastName

        def getEmailAdress(self):
            return self.emailAdress

        def getPassword(self):
            return self.password

        
        def setDni(self, dni):
         self.dni = dni

        def setName(self, name):
            self.name = name

        def setLastName(self, lastName):
            self.lastName = lastName

        def setEmailAdress(self, emailAdress):
            self.emailAdress = emailAdress

        def setPassword(self, password):
            self.password = password


name = input("Nombre:")
lastName = input("Apellido:")
dni = input("DNI:")
emailAdress = input("Email: ")
password = input("Contraseña: ")
