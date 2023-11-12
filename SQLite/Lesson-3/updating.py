import sqlite3

conn = sqlite3.connect("mars.db")
c = conn.cursor()

# c.execute("UPDATE users SET full_name='Begzod opa', modme_id=00001 WHERE id=11")
max_tg, min_tg = c.execute("SELECT MAX(telegram_id), MIN(telegram_id) FROM users;").fetchone()
min_modme, max_modme = c.execute(f"SELECT modme_id FROM users WHERE telegram_id IN ({min_tg}, {max_tg})").fetchall()
if min_modme[0] > max_modme[0]:
    c.execute(f"UPDATE users SET full_name='sanjarbek' WHERE modme_id={min_modme}")
else:
    c.execute(f"UPDATE users SET full_name='sanjarbek' WHERE modme_id={max_modme}")
    
conn.commit()
conn.close()
print("Code is successfully runned...")