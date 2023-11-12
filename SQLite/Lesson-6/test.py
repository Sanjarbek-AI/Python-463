# class Car:
#     def __init__(self, color, speed, name):
#         self.name = name
#         self.speed = speed
#         self.color = color
#
#     def stop(self):
#         print(f"Car is stopped {self.name}")
#
#
# matiz = Car('black', 1000, 'Black Pantera')
# matiz.stop()
import sqlite3


class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
               id INTEGER,
               telegram_id INTEGER,
               full_name TEXT,
               phone_number TEXT,
               modme_id INTEGER,
               group_number INTEGER,
               group_type TEXT
        )""")
        self.conn.commit()
        self.conn.close()


db_manager = DatabaseManager('botaloqlar.db')
db_manager.create_table()