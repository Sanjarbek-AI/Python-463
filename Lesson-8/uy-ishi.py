"""
1. Ichida 15 son bor list yarating va ularni ichidagi eng kattasini 5 ga ko'paytiring.
2. Ichida 10 ta son bor list yarating va eng katta va eng kichkina sonlarni uni ichida olib tashlang
3. Ichida 5 ta meva nomlari bor list yarating va nomi eng uzun mevani toping.
4. Ichida 10 ta son bo'lgan list yarating va ularni yig'indisini eng kattasi bilan almashtirib qo'ying.
5.Ichida 10 ism bo'lgan list yarating va 3-indexdagi ism o'rniga "Marsjon" degan so'zni qo'yib qo'ying
"""

# lists = [14,45,74,97,54,64,67,78,43,12,47,45,12,41,38,]

# numbers = max(lists)

# print(numbers * 5)

# lists = [14, 45, 74, 97, 54, 64, 67, 78, 43, 12, 47, 45, 12, 41, 38, ]
# num = 0
# max_num = lists[0]
#
# while num < len(lists):
#     if max_num < lists[num]:
#         max_num = lists[num]
#     num += 1
# print(max_num)

# lists = [14, 45, 74, 97, 54, 64, 67, 78, 43, 12, ]
#
# max_num = max(lists)
# min_num = min(lists)
#
# lists.remove(max_num)
# lists.remove(min_num)

# print(lists)

# lists = ["olma ", "olxori","olcha", "anor","uzum"]

# count = 0


# for check in lists:
#     if check ==  :
#         print(check)


# lists = ["ali" , "odil", "alisher" , "davron" , "umid" , "sobir" , "azamat" , "nodir" , "avaz" , "sharof "]

# lists.pop(3)
# lists.insert( 3 ,"marsjon")

# print(lists)

# lists = ["olma ", "olxori", "olcha", "anor", "uzum"]
# long_fruit = lists[0]
#
# for meva in lists:
#     if len(meva) > len(long_fruit):
#         long_fruit = meva
# print(long_fruit)

numbers = [12, 3, 5, 33, 67]
toq = 0
juft = 0

for index in range(len(numbers)):
    if index % 2 == 0:
        juft += numbers[index]
    else:
        toq += numbers[index]

print(toq - juft)
