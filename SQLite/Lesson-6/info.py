"""
relationlar haqida gaplashish postgresql haqida gapirib berish
class lar mavzusiga kirish

misollar: counter-strike | qurollar, odamlar,


- properties -> hususiyatlari, otlari
- methods -> funksiyalar, harakatlari fellari

Quyidagi classlarni yarating

Name: Animals
Properties: name, type, color, kg
Methods: run(), jump()

Name: Cars
Properties: name, color, year, company
Methods: start(), stop()

Bookshop

Name: Books
Properties: title, author, year, bar_code, quantity
Methods: get_book()
"""


class Books:
    def __init__(self, title, author, year, bar_code, quantity):
        self.title = title
        self.author = author
        self.year = year
        self.bar_code = bar_code
        self.quantity = quantity

    def get_book(self, title):
        if self.title == title:
            return self.quantity

    def increase_quantity(self):
        self.quantity += 1


book1 = Books('A', 'a', 4444, 4444444444, 34)
book2 = Books('S', 's ', 3333, 333333333, 21)
book3 = Books('Q', 'q', 2222, 2222222222, 14)
book4 = Books('E', 'e', 1111, 111111111, 12)

book1.increase_quantity()
book1.increase_quantity()
book1.increase_quantity()
book1.increase_quantity()
book1.increase_quantity()
data = book1.get_book()
print(data)
