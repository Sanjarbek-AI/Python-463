import sqlite3

conn = sqlite3.connect('mars.db')
c = conn.cursor()

# users = c.execute("""
# SELECT * FROM users;
# """).fetchall()

# users = c.execute("""
# SELECT full_name, phone_number FROM users WHERE id=6;
# """).fetchone()


conn.commit()
print("done...")
