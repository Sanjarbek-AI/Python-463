import sqlite3


conn = sqlite3.connect('mars.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
               id INTEGER,
               telegram_id INTEGER,
               full_name TEXT,
               phone_number TEXT,
               modme_id INTEGER,
               group_number INTEGER,
               group_type TEXT
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
               id INTEGER,
               photo_url TEXT,
               title TEXT,
               price REAL,
               color TEXT,
               quantity INTEGER,
               description TEXT
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
               id INTEGER,
               order_id INTEGER,
               telegram_id INTEGER,
               status TEXT,
               date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS order_products (
               id INTEGER,
               order_id INTEGER,
               title TEXT,
               quantity INTEGER,
               color INTEGER,
               price REAL
)
""")

conn.commit()
conn.close()
