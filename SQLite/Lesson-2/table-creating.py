import sqlite3

conn = sqlite3.connect('mars.db')
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS TEST (
               id INTEGER,
               telegram_id INTEGER,
               full_name TEXT,
               phone_number TEXT,
               modme_id INTEGER,
               group_number INTEGER,
               group_type TEXT
)
""")