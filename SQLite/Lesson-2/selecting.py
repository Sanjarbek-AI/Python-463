import sqlite3

conn = sqlite3.connect('mars.db')
cursor = conn.cursor()

# users = cursor.execute("SELECT id, full_name FROM users").fetchall()
# user = cursor.execute("SELECT full_name FROM users WHERE phone_number='+9989990010101'").fetchone()
# users = cursor.execute("SELECT id, full_name FROM users WHERE id<5").fetchall()

# user = cursor.execute("SELECT full_name FROM users WHERE id=3").fetchone()[0]

# counter = 0

# for char in user:
#     if char  in "aioue":
#         counter  += 1
# print(counter)

# users = cursor.execute("SELECT id, full_name FROM users WHERE id>=5 AND id<= 8").fetchall()
# users = cursor.execute("SELECT id, full_name FROM users WHERE id>5 OR id<8").fetchall()
# users = cursor.execute("SELECT phone_number FROM users WHERE phone_number LIKE '5%'").fetchall()
# users = cursor.execute("SELECT phone_number FROM users WHERE phone_number LIKE '%5'").fetchall()
# users = cursor.execute("SELECT phone_number FROM users WHERE phone_number LIKE '%5%'").fetchall()
# print(users)

# users = cursor.execute("SELECT DISTINCT phone_number FROM users WHERE full_name IN ('Ali', 'Vali', 'Joni')").fetchall()
# users = cursor.execute("SELECT id, full_name FROM users WHERE id BETWEEN 2 AND 5").fetchall()

# print(users)