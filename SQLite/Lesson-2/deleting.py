import sqlite3

conn = sqlite3.connect('mars.db')
cursor = conn.cursor()


cursor.execute("DROP TABLE TEST")