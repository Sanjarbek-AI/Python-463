import sqlite3

conn = sqlite3.connect('mars.db')
c = conn.cursor()

# user = (15, 21133133, 'hayr', '1212121212', 2121, 234, 'back')

# c.execute("""
# INSERT INTO users VALUES(?,?,?,?,?,?,?)
# """, user)

users = [
    (16, 34543, 'jhghbnj', '7898765', 232, 234, 'back'),
    (17, 34567898, 'vdsfbdgnfhm', '5677654', 3232, 234, 'back')
]

c.executemany("""
INSERT INTO users VALUES (?,?,?,?,?,?,?)
""", users)

conn.commit()
conn.commit()
print("done...")
