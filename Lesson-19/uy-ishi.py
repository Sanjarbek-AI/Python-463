"""
1. Odamdan ismini kiritishi so'rang. Va uning ismini ichida nechta a harfi borligini topib beradigan funksiya yozing.
   Xatolarni oldini ham oling. Masalarn ismini emas raqam kiritib yuborishi mumkin

2. Odamdan ismini kiritishini sorang va shu ismi bilan txt fayl ochib beradigan funksiya yozing. Agar bunaqa nomli
   fayl bor bolsa xato berishi mumkin siz shu xatoni oldini oling.

3. O'yinchini ismini key uning balini esa value qilib saqlab ketadigan dict yarating. Odamdan oyinchini ismini
   kiritishini sorang agar bunaqa ismli oyinchi yoq bolsa key error berishi mumkin siz shuni oldini oling.

"""
#
# while True:
#     def a_counter(name: str):
#         try:
#             name = int(name)
#             return "Wrong Value"
#         except ValueError:
#             return name.lower().count('a')
#
#
#     user_name = input("Name: ")
#     result = a_counter(user_name)
#     print(result)

# while True:
#     name = input("Name: ")
#
#     try:
#         with open(f"{name}.txt", 'x'):
#             pass
#         print("Fayl yaratildi")
#     except FileExistsError:
#         print("Already exists")


# players = {
#     'ali': 10,
#     'vali': 20,
#     'gani': 100
# }

# while True:
#     name = input("Name: ")
#
#     try:
#         print(players[name])
#     except KeyError:
#         print("Wrong key")
