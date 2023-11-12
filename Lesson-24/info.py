"""
O'tilgan mavzularni takrorlash:

- Barcha mavzular yuzasidan ochiqcha suhbat
- kwargs ni tugatish
- Lambda bilan tanishish
- Class mavzusiga kirish

Masalalar:

1. Nomalum key:value data qabul qiling va ularni bir dona dict holatga olib kelib qaytaring.
2. Ham args ham kwargs qabul qiladigan funksiya yozing va argsni listga solib,
   kwargs ni esa bitta dict qilib qaytaring.
3. Odamdan nomalum ravishda kwargs qabul qiling. Va ularni chiroyli qilib print qiling.

1. Ikkita sonni bir birga qoshib beradigan lambda funksiya yozish.
2. ayirish, bolish, kopaytirishni yozish
3. Odamdan text olish va uni ichida nehcta soz borligini topib beradigan lambda yozish
4. Ichida 10 son bor list yarating. Eng kattasini topib beradigan lambda yozing
5. Ichida 10 son bor list yarating. Eng kichkinasini topib beradigan lambda yozing
6. Odamdan ismini sorang va hamma harfini katta qilib qaytarib beradigan lambda yozing.
"""

"""
Maxsus masala:

Oylik hisoblash:

Agar darsga 4 martta ketma ket kelmasa usha 4 kun uchun oylik bermaydi.
Jami darslar uchun tolov miqdori 1090 ming so'm, darslar soni ba'zida 12
ta bazida 13 ta bolishi mumkin. 1 bor 0 yoq degani.

Agar 3 martta kelmasdan 1 martta kelsa ham oylik hisoblanadi.


"""
"""
1. bizz = 3 | bazz = 5 | 1 dan yuzgacha bo'gan sonlardan list hosil qiling. 2 ga bolinadiganini orniga fizz 5 ga esa buzz
  qoyib keting

2. sonni tub yoki tub emasligini aniqlaydigan kod yozing

3. odamdan gap qabul qiling va ularni har bir so'zini teskari qilib qaytaring

4. odamdan har xil katta va kichik harflar aralashgan text so'rang. Kattalarini kichkina kichkinalarini esa katta qilib
  qaytaring

5. rock, paper, scissor o'yinini yasang while orqali

6. Ichida 10 son bor list yarating max va minni o'rnini almashtiring

"""
days = [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1]


def f(a: list):
    a.append(1)

    tolov = 1090
    kunlik = 90
    i = -1
    while i < len(a) - 1:
        i += 1
        if a[i] == 0:
            for i1 in range(i + 1, len(a)):
                if a[i1] == 1:
                    if i1 - i >= 4:
                        tolov -= kunlik * (i1 - i)
                    i = i1

    return tolov


result = f(days)
print(result)
