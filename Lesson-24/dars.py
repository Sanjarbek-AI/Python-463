# text = "salom botaloqlar"
#
# text1 = lambda text2: text2.upper()
# print(text1(text))

# num1 = int(input("Num1: "))
# num2 = int(input("Num2: "))
# amal = input("Amal: ")
# if amal == "+":
#     result = lambda number1, number2: number1 + number2
#     print(result(num1, num2))
# elif amal == "-":
#     result = lambda number1, number2: number1 - number2
#     print(result(num1, num2))

# user_text = input("Text: ")
# result = lambda text: len(text.split())
# print(result(user_text))
#
# import random
#
# actions = ('tosh', 'qaychi', "qog'oz")
#
# while True:
#     action = random.choice(actions)
#
#     user_action = input("Tanlang: ")
#
#     if user_action == action:
#         print("Teng")
#     elif user_action == "qaychi" and action == "qog'oz" or user_action == "tosh" and action == "qaychi" or user_action == "qog'oz" and action == "tosh":
#         print(f"Siz yutdingiz {action} | {user_action}")
#     else:
#         print(f"Komyuter win {action} | {user_action}")

# yutuq = {
#     "1": "2",
#     "2": "3",
#     "3": "1"
# }
#
# from random import choice
#
# while True:
#     a = input("1 - Tosh| 2 - qaychi| 3 - qog'oz: ")
#
#     b = choice(list("123"))
#
#     if a == b:
#         print("hichkim yutmadi")
#
#     elif yutuq.get(a) == b:
#         print("yutdiz")
#     else:
#         print("yutqizdiz")

name = input("Name: ").strip().lower()
for harf in name:
    if harf in "aioue":
        name = name.replace(harf, "")
print(name)