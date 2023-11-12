import sqlite3

conn = sqlite3.connect("mars.db")
c = conn.cursor()

users = c.execute("SELECT * FROM users;").fetchall()

c.executemany(
    """INSERT INTO new_users (telegram_id, full_name, phone_number, modme_id, group_number, group_type, age)
      VALUES(?,?,?,?,?,?,?)""", users)

c.execute("UPDATE new_users SET age=0;")

conn.commit()
conn.close()
print("Code is successfully runned...")