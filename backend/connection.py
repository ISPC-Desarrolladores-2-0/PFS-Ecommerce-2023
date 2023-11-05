import mysql.connector
from mysql.connector import Error

def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='planetSuperheroesDB'
        )
        if connection.is_connected():
            print("Conexión a la base de datos exitosa")
        return connection
    except Error as e:
        print(f"Error durante la conexión a la base de datos: {e}")
        return None

def close_db_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Conexión a la base de datos cerrada")