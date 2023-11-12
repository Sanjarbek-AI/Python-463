"""
Dars davomida o'tiladigan mavzular:

- List methodlari bilan tanishish
- List haqida to'liq ma'lumot va boshqa shunga o'xshash ma'lumot turlari ham borligini eslatish
- Listga doir masalalar yechish
- max, min, len
- spacedagi uyga vazifalarni 3tasini bajarish


Mashqalar:

- ichida 10 ta son bor list yarating va ularni faqat toqlarini print qiling
- for va range orqali 3 va 5 ga bo'linadigan sonalrni yangi list ochib ushanga qo'shib boring va uni print qiling
- ichida 5 ta meva nomi bor list yarating va o'zingiz yoqtirmagan mevani uni ichidan olib tashlang.
    - ichida 10 ta son bor list yarating va o'zingiz yoqtirgan sonning indexini toping
    - ichida 5 ta ism bor list yarating va 0-indexga o'zingizni ismingizni qo'shing
- ikkita list yarating va ularni ichidagi elementlarini birlashtiring
- ichida 10 son bor list yarating va eng kichkina va eng katta sonni o'rnini almashtiring

-  Butun tipli 10 ta (ikki xonali sonlar) elementdan iborat massiv kiriting.
   Kiritilgan massiv sonlari raqamlarini ayirmasidan yangi massiv hosil
   qiling.
- Butun tipli 15 ta elementdan iborat massiv kiriting. Shunday saralangki
  massivni manfiy sonlari boshida o`sish tartibida, musbat sonlari
  oxirida kamayish tartibida bo`lsin.
"""
numbers = [12, 11, 23, 15, 23, 43, 5, 67, 65, 23, 43, 22]
numbers.append(1212)  # listning oxiriga yangi element qo'shadi
numbers.insert(0, 1212)  # yangi elementni index bo'yicha qo'shadi
numbers.index(-1)  # o'ziga berilgan elementni qidiradi topsa indexini qaytaradi
numbers.remove(-1)  # o'ziga berilgan elementni nomi bo'yicha o'chiradi
numbers.pop(0)  # o'ziga berilgan elementni index bo'yicha o'chiradi, agar hech nima bermasa oxiridan o'chiradi
numbers.count(-1)  # o'ziga berilgan elementni list ichida nechta ekanligini sanab qaytaradi

numbers.extend(numbers)  # ikkita list ichidagi elementlarni birlashtiradi
numbers.clear()  # listni barcha elementlarini o'chirib tashlaydi
numbers.sort()  # list ichida sonlar bo'lsa tartib bo'yicha harflar bo'lsa alifbe bo'yicha tartiblab beradi
numbers.reverse()  # listni teskari qilib beradi
numbers.copy()  # listni o'zidan nusxa yasaydi va qaytaradi

nums = ["Salom", "Ayubxon", "Bobur"]

nums.remove("Salom")
print(nums)
