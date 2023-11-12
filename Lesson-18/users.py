time = 0


def checker(username: str, password: str):
    with open('ketmonbek.txt', 'r') as reader:
        users = reader.readlines()

        for user in users:
            user_split = user.split()
            if user_split[1].strip() == password and user_split[0] == username:
                return user_split
    return False


while True:
    choice = int(input("1: Register | 2: Login: "))
    if choice == 1:
        user_username = input("Username: ")
        user_phone_number = input("Password: ")
        text = f"{user_username} {user_phone_number}\n"
        with open('ketmonbek.txt', 'a') as appender:
            appender.write(text)
            print("Seni bazaga qo'shdim bolakay, endi login qila olasiz")
    elif choice == 2:
        user_username = input("Username: ")
        user_phone_number = input("Password: ")
        if checker(user_username, user_phone_number):
            print("Xush kelibsiz xo'jayin")
        else:
            print("Meni shantaj mantaj qilaman deb o'ylamang, parol yoki username notogri")
    else:
        print("Xato raqam.")
    time += 1
