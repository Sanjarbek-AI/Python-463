"""
O'tiladigan mavzular:

1. args va kwargs bilan tanishish
2. funksiyani takrorlash
3. parametr va argument
4. birdaniga bir nechta qiymat return qilish


Masalalar:

1. Nomalum ravishda argument qabul qoladigan funksiya yozing va ularni eng kattasini return qiling.
2. Nomalum ravishda harf va raqamlar aralash argument qabul qiladigan funksiya yozing va raqamlarni alohida
   harflarni alohida qilib qaytarib bering. Bitta returnda ikkita narsani return qiling.
3. Nomalum ravishda argument qabul qoladigan funksiya yozing va ularni eng o'rta arifmetikini return qiling.
4. Odamdan nomalum ravishda kwargs qabul qiling. Va ularni chiroyli qilib print qiling.
5. Odamdan bir qancha string malumot qabul qiladigan funksiya yozing va jami hamma stringlarni ichida nechta unli
   harf borligini return qiling
6. Nomalum key:value data qabul qiling va ularni bir dona dict holatga olib kelib qaytaring.
7. Nomalum miqdorga argument qabul qiladigan funksiya yozing. Va ularni ichidan duplicatlarini olib tashlang.
   SET dan foydalanish mumkin emas.
8. Ham args ham kwargs qabul qiladigan funksiya yozing va argsni listga solib, kwargs ni esa bitta dict qilib qaytaring.

"""

def foo(*args, **kwargs):
    for key, value in kwargs.items():
        print(key, value)
    print("Positional arguments (*args):", args)
    print("Keyword arguments (**kwargs):", kwargs)

foo(1, 2, 3, name="Alice", age=30)