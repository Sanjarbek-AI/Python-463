# def text_upper(text: str):
#     x = text.upper()
#     return x
#
#
# def text_lower(text: str):
#     x = text.lower()
#     return x
#
#
# def text_replace(text: str, old: str, new: str):
#     x = text.replace(old, new)
#     return x
#
#
# print("1: Hammasini kichkina qilish.")
# print("2: Hammasini katta qilish.")
# print("3: Replace qilish.")
#
# while True:
#     user_text = input("Text: ")
#     choose = int(input("Choose: "))
#
#     if choose == 1:
#         res = text_lower(user_text)
#         print(res)
#     elif choose == 2:
#         res = text_upper(user_text)
#         print(res)
#     elif choose == 3:
#         old_char = input("Nimani o'rniga: ")
#         new_char = input("Nimani: ")
#         res = text_replace(user_text, old_char, new_char)
#         print(res)

print("1: Qo'shish.")
print("2: Ayirish.")
print("3: Bo'lish.")


def n_add(num1: int, num2: int):
    res = num1 + num2
    return res


def n_minus(num1: int, num2: int):
    res = num1 == num2
    return res


while True:
    son1 = int(input("Son1: "))
    son2 = int(input("Son2: "))
    choose = int(input("Choose: "))

    if choose == 1:
        res = n_add(son1, son2)
        print(res)
    elif choose == 2:
        res = n_minus(son1, son2)
        print(res)

