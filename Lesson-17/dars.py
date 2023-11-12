x_o = [
    [["-"], ["-"], ["-"]],
    [["-"], ["-"], ["-"]],
    [["-"], ["-"], ["-"]]
]


def printer(numbers: list):
    for i in numbers:
        print(i, end="\n")


printer(x_o)


def checker(x, y):
    if x_o[x][y][0] != "-":
        return False
    return True


attempt = 1

while True:
    if attempt % 2 == 1:
        print("Bu x ni navbati !")
        user_input = input("1 dan 9 gacha: ")
        if user_input == "1":
            if checker(0, 0):
                x_o[0][0][0] = "x"
            else:
                attempt += 1
                print("Bu joy band")
        elif user_input == "2":
            x_o[0][1][0] = 'x'
        elif user_input == "3":
            x_o[0][2][0] = 'x'
        elif user_input == "4":
            x_o[1][0][0] = 'x'
        elif user_input == "5":
            x_o[1][1][0] = 'x'
        elif user_input == "6":
            x_o[1][2][0] = 'x'
        elif user_input == "7":
            x_o[2][0][0] = 'x'
        elif user_input == "8":
            x_o[2][1][0] = 'x'
        elif user_input == "9":
            x_o[2][2][0] = 'x'
    else:
        print("Bu 0 ni navbati !")
        user_input = input("1 dan 9 gacha: ")
        if user_input == "1":
            if user_input == "1":
                if checker(0, 0):
                    x_o[0][0][0] = "0"
                else:
                    attempt += 1
                    print("Bu joy band")
        elif user_input == "2":
            x_o[0][1][0] = '0'
        elif user_input == "3":
            x_o[0][2][0] = '0'
        elif user_input == "4":
            x_o[1][0][0] = '0'
        elif user_input == "5":
            x_o[1][1][0] = '0'
        elif user_input == "6":
            x_o[1][2][0] = '0'
        elif user_input == "7":
            x_o[2][0][0] = '0'
        elif user_input == "8":
            x_o[2][1][0] = '0'
        elif user_input == "9":
            x_o[2][2][0] = '0'
    printer(x_o)
    attempt += 1
