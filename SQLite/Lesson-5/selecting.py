import sqlite3

conn = sqlite3.connect("../mars.db")
c = conn.cursor()


def get_all_products():
    products = c.execute("""SELECT * FROM products;""").fetchall()
    text = ""
    for product in products:
        text += f"{product[0]}\t{product[1]}\t{product[2]}\t{product[3]}\t{product[4]}\n"
    return text


def search_product_by_name(name: str):
    products = c.execute(f"""SELECT * FROM products WHERE title LIKE '%{name}%';""").fetchall()
    text = ""
    for product in products:
        text += f"{product[0]}\t{product[1]}\t{product[2]}\t{product[3]}\t{product[4]}\n"
    return text


def get_products_by_color():
    products = c.execute(f"""SELECT title, color, SUM(price) FROM products GROUP BY color; """).fetchall()
    text = ""
    for product in products:
        text += f"{product[0]}\t{product[1]}\t{product[2]}\n"
    return text


def get_products_in_tuple(products_list: tuple):
    products = c.execute(f"""SELECT title, price FROM products WHERE title IN {products_list}; """).fetchall()
    text = ""
    for product in products:
        text += f"{product[0]}\t{product[1]}\n"
    return text


def get_products_order_by_price():
    products = c.execute(f"""SELECT title, price FROM products ORDER BY title DESC; """).fetchall()
    text = ""
    for product in products:
        text += f"{product[0]}\t{product[1]}\n"
    return text


def get_products():
    products = c.execute(f"""SELECT title, price FROM products ORDER BY title; """).fetchall()[:3]
    product = products[0]
    for item in products:
        print(item)
        print(product)
        if int(item[1][:-1]) > int(product[1][:-1]):
            product = item
    return product[0], product[1]


print(get_products())
#
# print("1. Hamma mahsulotlarni ko'rish")
# print("2. Nomi bo'yicha qidirish")
# print("3. Eng qimmat va eng arzon mahsulotlar")
# print("4. Ikkita narx orasidagini olish")
# print("5. Eng kam qolgan mahsulotni nomini olish")
# print("6. Eng ko'p qolgan mahsulotni nomi, nechta qolgani va narxini olish")
# print("7. Eng qimmat va eng arzon mahsulotlarning farqini olish")
# print("8. Nomi ushbu tuple ichida borlarini nomlarini va narxlarini olish (Airtag, SmartWatch)")
# print("9. Rangi qora bo'lgan mahsulotlarni umumiy narxini olish")
# print("10. Eng qimmat 3 ta mahsulotni olish")
# print("11. Arzondan qimmatga qarab tartiblab olish")
# print("12. Qimmatdan arzonga qarab tartiblab olish")
# print("13. Nomi bo'yicha tartiblab olish kerak, eng tepada turgan 3 ta mahsulotning eng qimmatini topish kerak")
#
# while True:
#     option = input("enter your option: to close enter x: ")
#     if option == "x":
#         print("Welcome...")
#         break
#     elif option == "1":
#         res = get_all_products()
#         print(res)
#     elif option == "2":
#         product_nam = input("Product name: ")
#         res = search_product_by_name(name=product_nam)
#         print(res)
#     elif option == "9":
#         res = get_products_by_color()
#         print(res)
#     elif option == "8":
#         products_tuple = ("Airtag", "SmartWatch", "SmartTV")
#         res = get_products_in_tuple(products_tuple)
#         print(res)
#
#     elif option == "11":
#         res = get_products_order_by_price()
#         print(res)
#
# # c.executemany("""
# # """)
#
# conn.commit()
# conn.close()
#
# print("Done...")
#
# bobo = [('ali', 10), ('vali', 9), ('gani', 11)]
