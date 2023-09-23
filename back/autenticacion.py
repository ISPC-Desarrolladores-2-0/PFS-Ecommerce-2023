import sqlite3

class Autenticacion:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def iniciar_sesion(self, email, contraseña):
        # Verificar las credenciales del usuario en la base de datos
        self.cursor.execute("SELECT * FROM usuarios WHERE email = ? AND contraseña = ?", (email, contraseña))
        usuario = self.cursor.fetchone()

        if usuario:
            print(f"Bienvenido, {usuario[1]}!")  # Suponiendo que el nombre del usuario está en la segunda columna
        else:
            print("Credenciales incorrectas. Por favor, inténtelo de nuevo.")

    def cerrar_conexion(self):
        self.conn.close()
