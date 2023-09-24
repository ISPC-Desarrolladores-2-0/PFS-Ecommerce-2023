import sqlite3

class Category:
    def __init__(self, id_categories, name):
        self.id_categories = id_categories
        self.name = name

def get_all_categories():
    conn = sqlite3.connect("mi_base_de_datos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categories")
    categories_data = cursor.fetchall()
    categories = [Category(id_categories, name) for id_categories, name in categories_data]
    conn.close()
    return categories

categories = get_all_categories()

for category in categories:
    print(f"ID: {category.id_categories}, Name: {category.name}")