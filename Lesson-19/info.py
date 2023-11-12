"""
O'tiladigan mavzular:

1. O'tilgan mavzularni takrorlash.
2. Funksiyani qaytarish, parametr va argument
3. Return ni yaxshilb tushuntirish
4. Try Except ba eng ko'p ishlatiladigan xato turlari
----------------------------------------------------------------------------
1.
try:
    # Code that may raise an exception
    # ...
except ExceptionType:
    # Code to handle the exception
    # ...

----------------------------------------------------------------------------

2.
try:
    x = 10 / 0  # This division will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero!")

-----------------------------------------------------------------------------------

3.

try:
    # Code that may raise an exception
    # ...
except ExceptionType1:
    # Code to handle ExceptionType1
    # ...
except ExceptionType2:
    # Code to handle ExceptionType2
    # ...
except:
    # Code to handle any other exception
    # ...

--------------------------------------------------------------------------------------------

4.

try:
    file = open("myfile.txt", "r")  # This may raise a FileNotFoundError or IOError
    content = file.read()
    file.close()
except FileNotFoundError:
    print("Error: File not found!")
except IOError:
    print("Error: I/O error occurred!")

-------------------------------------------------------------------------------------

5.

try:
    # Code that may raise an exception
    # ...
except ExceptionType:
    # Code to handle the exception
    # ...
else:
    # Code to execute if no exception occurs
    # ...


--------------------------------------------------------------------------------------

6.

try:
    # Code that may raise an exception
    # ...
except ExceptionType:
    # Code to handle the exception
    # ...
finally:
    # Code to be executed regardless of exceptions
    # ...

---------------------------------------------------------------------------------------

"""

"""
Mashqlar:

1. Odamdan input sifatida yoshini sorang va inputga text kiritib yuboring
   Usha paytda xato chiqish oldini oling.

2. Odamdan bitta raqam va text so'rang ularni bir biriga qo'shib javobi
   qaytaring. Lekin unda xato beradi. Siz usha xatoni oldini oluvchi kod yozing.

3. Ichida 5 ism bor list yarating va odamdan qaysi indexdagi ism kerakligini
   sorang. Agar odam kiritgan raqam listni indexlaridan katta bolib ketsa xato 
   chiqadi. Siz shu xatoni oldini oling.

4. Oila azolaringiz ism va yoshini dictda saqlang. ism:yosh, keyin odamdan 
   kimni yoshi kerakligini sorang. Agar notogri ism kiritsa xato chiqadi.
   Siz shu xatoni oldini oladigan kod yozing.

5. Odamdan ikkita son kiritishini sorang va ularni bolib javobini qaytaring.
   Agar ikkinchi sonni 0 qilib qoysa xato chiqadi. Siz shu xatoni oldini 
   oladigan kod yozing.


Jamoviy masalalar:

1. Ikkita sonni bir birga bo'lib beradigan funksiya yozing. har xil xatolar chiqishini
   oldini ham oling.
   Masalan: 
   Raqam emas text kiritib yuborishi
   Ikkinchi sonni 0 qilib qoyishi
   Integer emas float son kiritishi.

2. Odamdan bittta raqam sorang 0 dan boshqa shu odam kiritgan raqamgacha 
   barcha juft sonlarni yigindisini topib beradigan funksiya yozing.
   Xatoliklarni oldini ham oling.
   Masalan: 
   Son emas text kiritishi
   0 dan kichkina son kiritishi -> buni if bilan tekshirsa ham boladi

"""
