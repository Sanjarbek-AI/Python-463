"""
O'tiladigan mavzular:

- Funksiyalar bilan ishlash
- set va funksiya bilan ishlash
- tuple va funksiya bilan ishlash

Masalalar:

1. Instagram usernamelarini saqlaydigan malumot turini yarating. Va shunday funksiya yozing:
   - odamdan input sifatida username kiritishini sorang agar bunday username bor bolsa
   uni mavjud deng yoq bolsa bazaga qoshing.

2. Korzinkada mahsulotlarni olib ichiga solib ketadigan savat uchun malumot turini yarating. Unda malumot nomlari
   taqrorlanmasligi kerak. Bitta ogan narsasini qayta olmasligi kerak.

3. Kanalga subscribe qilgan qilmaganini tekshirish va unga qoshilish imkonini berish

4. Pitsa time ga royxatdan o'tgan bollarni ismlarini malumotlar bazasifda saqlang. Ular bir martta qoshilishi kerak
   holos.

Tuple

5. Bitta kitob haqida malumot toplaydigan malumot turini yarating. Uni nomi, narxi, beti, yozuvchini saqlasin.

6. Passworsni validate qilish: kamida 8 ta uzunlikda bolishi, oxiri raqam bilan tugamasligi, faqat harf bolmasligi
  orasida bosh joy yoqligi

"""


# def gmail_checker(gmail: str):
#     gmail = gmail.strip().replace(" ", "")
#     text = ""
#     if len(gmail) > 10:
#         if not gmail.endswith('@gmail.com'):
#             text += "Oxiriga @gmail.com qoyilmagan\n"
#         if gmail.count('@') != 1:
#             text += "Kuchukcha odatdagidan kop, yoki oz\n"
#     else:
#         text += "Gmail uzunligi kamida 11 ta bo'lishi kerak\n"
#     return text
#
#
# while True:
#     email = input("Gmail: ")
#     result = gmail_checker(email)
#     print(result)
