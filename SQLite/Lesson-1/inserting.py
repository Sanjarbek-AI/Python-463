import sqlite3


conn = sqlite3.connect('mars.db')
cursor = conn.cursor()

users = [
    (2, 232323, 'Ali', '889999999999', 2323, 345, 'BACK'),
    (3, 343434, 'Vali', '889999999999', 4323, 345, 'BACK'),
    (4, 545454, 'Gani', '75756372383', 5433, 456, 'BACK'),
]

# cursor.execute("""
# INSERT INTO users VALUES(1, 121212, 'Sanjarbek', '+9989990010101', 1212, 463, 'BACK')
# """)


cursor.executemany("""
INSERT INTO users VALUES(?,?,?,?,?,?,?)
""", users)

conn.commit()
conn.close()
