import sqlite3

conn = sqlite3.connect("../mars.db")
c = conn.cursor()

users = c.execute("""
SELECT id, title, SUM(price) AS sum_modme
FROM products
GROUP BY color;
""").fetchall()
print(users)


conn.commit()
conn.close()