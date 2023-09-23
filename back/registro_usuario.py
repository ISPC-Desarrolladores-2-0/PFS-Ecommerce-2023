import sqlite3
import hashlib

class Usuario:
    def __init__(self, nombre, email, contraseña):
        self.nombre = nombre
        self.email = email
        self.contraseña = self._encriptar_contraseña(contraseña)

    def _encriptar_contraseña(self, contraseña):
        # Utiliza una función de hash (por ejemplo, hashlib) para encriptar la contraseña
        return hashlib.sha256(contraseña.encode()).hexdigest()

    def crear_cuenta(self):
        try:
            # Conexión a la base de datos
            conn = sqlite3.connect("mi_base_de_datos.db")
            cursor = conn.cursor()

            # Verificar si el usuario ya existe
            cursor.execute("SELECT * FROM usuarios WHERE email = ?", (self.email,))
            existente = cursor.fetchone()

            if existente:
                return "El usuario ya existe."

            # Si no existe, insertar el nuevo usuario
            cursor.execute("INSERT INTO usuarios (nombre, email, contraseña) VALUES (?, ?, ?)",
                           (self.nombre, self.email, self.contraseña))
            conn.commit()
            return "Cuenta creada con éxito."

        except sqlite3.Error as error:
            return f"Error al crear la cuenta: {str(error)}"
        finally:
            conn.close()

    def validar_contraseña(self, contraseña_ingresada):
        # Lógica para comparar las contraseñas encriptadas
        return self.contraseña == self._encriptar_contraseña(contraseña_ingresada)

    def guardar_información(self):
        try:
            # Conexión a la base de datos
            conn = sqlite3.connect("mi_base_de_datos.db")
            cursor = conn.cursor()

            # Actualizar información del usuario
            cursor.execute("UPDATE usuarios SET nombre = ?, email = ? WHERE email = ?",
                           (self.nombre, self.email, self.email))
            conn.commit()
            return "Información actualizada con éxito."

        except sqlite3.Error as error:
            return f"Error al guardar la información: {str(error)}"
        finally:
            conn.close()

