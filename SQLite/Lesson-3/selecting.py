import sqlite3

conn = sqlite3.connect("mars.db")
c = conn.cursor()

# users = c.execute("SELECT MAX(id) FROM users;").fetchone()
# print(users)

# users = c.execute("SELECT MIN(id) FROM users;").fetchone()
# print(users)

# users = c.execute("SELECT SUM(modme_id) FROM users;").fetchone()
# print(users)

# users = c.execute("SELECT modme_id FROM users ORDER BY modme_id DESC;").fetchall()
# print(users)

# users = c.execute("SELECT COUNT(DISTINCT full_name) FROM users;").fetchone()[0]
# print(users)

# users = c.execute("SELECT MAX(modme_id), MIN(modme_id) FROM users;").fetchone()
# print(users[0] - users[1])


conn.close()
print("Code is successfully runned...")