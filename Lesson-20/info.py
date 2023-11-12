"""
O'tiladigan mavzular:
- spacedagi mavzularni yuklash
- masalalar yechish

Masalalar yechish:

nums = [1,3,42,45,112,5523,-12,442,-12,-2, -33, -43]

1. Odamdan bitta raqam so'rang va u kiritgan raqamdan katta bo'lgan birinchi
   sonni kvadratga oshiring.

2. 100 dan 999 gacha bo'lgan sonlarni o'rtasida turgan sonlarini kubga
   oshirib print qiling. Masalan: 124 = 1 2 4 > bunda o'rtada turga son
   2 uning kubi esa 8 shunda son 1 8 3 ga o'zgaradi va 184 chiqadi.

3. 1 dan 1000 gacha bo'lgan sonlarni raqamlari yigindisi orqa oldiga ham bir xil
   bo'lganlarini listga qo'shib keting. Masalan: 985 > bularni yigindisi
   9 + 8 + 5 = 22 boladi va u orqa oldiga bir xil oqiladi.

4. Bir minut ichida har bir bakteriya ikkiga bo`linadi. Boshlang`ich
   holatda bitta bakteriya mavjud. Siz bergan vaqt (15 min, 7 min va h.k)
   ichida bakteriyalar soni nechtaga yetishini hisoblovchi dastur tuzing.

5. Navbat bilan n ta sinf o`quvchilarini bo`yini uzunligi kiritiladi. Sinf
   o`quvchilarining o`rtacha bo`yini toping.

6. Siz kiritayotgan butun musbat bo`lgan son qancha raqamdan tashkil
   topganini sanovchi dastur tuzing.

7. Odamdan son sorang shu sonni bolsa boladigan barcha sonlarni kamayish
   tartibida listga saqlang.

8. Berilgan m va n o`zgaruvchilarning qiymatlari oralig`idagi juft
   sonlarning kvadratlari yig`indisini toping.

9. 1 dan N gacha bo`lgan sonlar kvadratlari summasi S ni xisoblang

10. 10 dan N gacha bo`lgan natural sonlar berilgan. Ular orasidan eng
   kichik butun o`nxonalik sonni toping.
"""

# nums = [1, 3, 42, 45, 112, 5523, -12, 442, -12, -2, -33, -43]
#
# try:
#     num = int(input("Enter number: "))
#     temp_list = list()
#     for i in nums:
#         if i > num:
#             temp_list.append(i)
#     temp_list.sort()
#     print(temp_list[0] ** 3)
#
#
# except ValueError:
#     print("Wrong value")


# for num in range(100, 999):
#     num_str = str(num)
#     middle_num = int(num_str[1]) ** 2
#     result = num_str[0] + str(middle_num) + num_str[-1]
#     print(int(result))

# numbers = []
# for num in range(1, 1000):
#     temp_num = 0
#     for i in str(num):
#         temp_num += int(i)
#     numbers.append(temp_num)
# print(numbers)


# try:
#     summa = 0
#     num = int(input("Number: "))
#     for i in str(num):
#         i = int(i)
#         if i % 2 == 0:
#             summa += i
#     print(summa)
#
# except ValueError:
#     print("Wrong value")
