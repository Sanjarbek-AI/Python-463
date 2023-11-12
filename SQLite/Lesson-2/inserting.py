import sqlite3

conn = sqlite3.connect('mars.db')
cursor = conn.cursor()


users = [
    (5, 232323, 'Joni', '889999999999', 2323, 345, 'BACK'),
    (6, 35, 'Gofur', '884429999999', 456, 345, 'BACK'),
    (7, 545535454, 'bOBUR', '7654', 653, 456, 'FRONT'),
    (8, 5335523, 'Ali', '899876', 2334523, 345, 'FRONT'),
    (9, 43, 'Vali', '56789876', 3222, 345, 'BACK'),
    (10, 754, 'Doni', '4567898765', 7654, 456, 'FRONT'),
    (11, 353, 'Ali', '3456789', 456, 345, 'BACK'),
    (12, 53535, 'lolo', '0987654', 765, 345, 'BACK'),
    (13, 65754, 'Pipi', '34567890', 567, 456, 'BACK'),
]

cursor.executemany("""
INSERT INTO users VALUES(?,?,?,?,?,?,?)
""", users)

conn.commit()
conn.close()



