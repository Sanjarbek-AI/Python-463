def adder(num1: int, num2: int):
    result = num1 + num2
    return result


def ayirish(num1: int, num2: int):
    result = num1 - num2
    return result



def kop(num1: int, num2: int):
    result = num1 + num2
    return result


def bol(num1: int, num2: int):
    result = num1 - num2
    return result


first_num = int(input("Num1: "))
amal = input("Amalni kiriting: ")
second_num = int(input("Num2: "))

if amal == "+":
    print(adder(first_num, second_num))
elif amal == "-":
    print(ayirish(first_num, second_num))
elif amal == "*":
    print(kop(first_num, second_num))
elif amal == "/":
    print(bol(first_num, second_num))
