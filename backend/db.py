import sqlite3
import os

DB_PATH = "data/database.db"

def init_db():
    if not os.path.exists("data"):
        os.makedirs("data")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create menu table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            category TEXT,
            price REAL,
            stock INTEGER,
            image TEXT
        )
    ''')

    # Create orders table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            table_number TEXT,
            item_name TEXT,
            quantity INTEGER,
            status TEXT
        )
    ''')

    # Insert sample data only if menu table is empty
    cursor.execute("SELECT COUNT(*) FROM menu")
    if cursor.fetchone()[0] == 0:
        sample_menu = [
            ("Margherita Pizza", "Classic cheese and tomato pizza", "Main", 9.99, 10, ""),
            ("Caesar Salad", "Romaine, croutons, Caesar dressing", "Starter", 6.50, 15, ""),
            ("Grilled Chicken Sandwich", "Served with lettuce and mayo", "Main", 8.75, 8, ""),
            ("Chocolate Lava Cake", "Warm chocolate cake with molten center", "Dessert", 5.25, 5, ""),
            ("Lemonade", "Freshly squeezed", "Drinks", 2.99, 20, "")
        ]

        cursor.executemany('''
            INSERT INTO menu (name, description, category, price, stock, image)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', sample_menu)

    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect(DB_PATH)