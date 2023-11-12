import sqlite3

conn = sqlite3.connect("../mars.db")
c = conn.cursor()


products = [
    (1, '#', 'Olma', '1$', 'yashil', 367, 'BACK'),
    (2, '#', 'Banan', '2$', 'sariq', 367, 'BACK'),
    (3, '#', 'Softili', '1$', 'bor', 367, 'BACK'),
    (4, '#', 'Airpods', '100$', 'oq', 367, 'BACK'),
    (5, '#', 'Iphone', '1000$', 'qora', 367, 'BACK'),
    (6, '#', 'Ipad', '1000$', 'qora', 367, 'BACK'),
    (7, '#', 'MacBook', '2000$', 'qora', 367, 'BACK'),
    (8, '#', 'SmartWatch', '200$', 'qora', 367, 'BACK'),
    (9, '#', 'Notebook', '3$', 'qora', 367, 'BACK'),
    (10, '#', 'PowerBank', '10$', 'oq', 367, 'BACK'),
    (11, '#', 'AirTag', '50$', 'oq', 367, 'BACK'),
    (12, '#', 'Back', '30$', 'qora', 367, 'BACK'),
    (13, '#', 'SmartTV', '500$', 'qora', 367, 'BACK'),
    (14, '#', 'playstation', '400$', 'qora', 367, 'BACK'),
    (15, '#', 'Headphones', '70$', 'qora', 367, 'BACK'),
]

c.executemany("""
INSERT INTO products VALUES(?,?,?,?,?,?,?)
""", products)

conn.commit()
conn.close()

print("Done...")

