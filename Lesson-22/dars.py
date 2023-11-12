# def name_checker(name: str):
#     more_letter = list()
#     one_letter = set()
#
#     for letter in name:
#         count = name.count(letter)
#         if count == 1:
#             one_letter.add(letter)
#         else:
#             more_letter.append(letter)
#     return more_letter, one_letter
#
#
# user_name = input("Name: ")
# letter_list, letter_set = name_checker(user_name)
# print(letter_set)
# print(letter_list)


# def set_def(data: set):
#     nums = list()
#     for num in data:
#         if num % 2 == 0:
#             nums.append(num * 2)
#     return data, nums
#
#
# data_set = {1, 2, 4, 5, 6, 6}
# set_data, list_data = set_def(data_set)
# print(list_data)

# usernames = set()
#
#
# def username_check(username: str):
#     if username in usernames:
#         return "Bunday username bor"
#     else:
#         usernames.add(username)
#         return "Added"
#
#
# while True:
#     name = input("Username: ")
#     result = username_check(name)
#     print(result)


def phone_checker(phone: str):
    try:
        text = ""
        if len(phone) != 13:
            return "Uzunligi 13 bo'lsin"
        else:
            if phone[:4] != '+998':
                text += "Boshidagi kod noto'g'ri\n"
            if int(phone[4:6]) not in (99, 90, 91, 95, 94, 93):
                text += "Kod noto'gri"
            if not phone[6:].isdigit():
                text += "Raqam notori"
        return text
    except ValueError:
        return "Kod noto'gri"


while True:
    phone_number = input("Phone: ")
    res = phone_checker(phone_number)
    print(res)

# def password_checker(password: str):
#     text = ""
#     if len(password) < 8:
#         text += "8 tadan kam\n"
#     if password.isalpha() is True or password.isdigit():
#         text += "Ham harf ham raqam bolishi kerak\n"
#     if password.islower():
#         text += "Kamida bittasi katta harf bo'lsin\n"
#     return text
#
#
# while True:
#     user_pass = input("Pass: ")
#     result = password_checker(user_pass)
#     print(result)
