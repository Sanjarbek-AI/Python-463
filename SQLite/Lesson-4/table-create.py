import sqlite3

conn = sqlite3.connect("mars.db")
c = conn.cursor()

# c.execute("""
# CREATE TABLE IF NOT EXISTS new_users (
#                id INTEGER PRIMARY KEY AUTOINCREMENT,
#                telegram_id INTEGER,
#                full_name TEXT,
#                phone_number TEXT,
#                modme_id INTEGER,
#                group_number INTEGER,
#                group_type TEXT,
#                age INTEGER NULL
# )
# """)

c.execute("""INSERT INTO new_users (telegram_id, full_name, phone_number, modme_id, group_number, group_type)
          VALUES(100001, 'SSASAS','SASASASS',1001,1001,'SSASA')""")

conn.commit()
conn.close()