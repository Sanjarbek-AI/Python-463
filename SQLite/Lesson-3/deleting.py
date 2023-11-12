import sqlite3

conn = sqlite3.connect("mars.db")
c = conn.cursor()

# c.execute("DROP TABLE products;")
# c.execute("DELETE FROM users;")
c.execute("DELETE FROM users WHERE id=11;")

conn.commit()
conn.close()
print("Code is successfully runned...")