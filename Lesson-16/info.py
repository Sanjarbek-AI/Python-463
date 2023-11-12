"""
O'tiladigan mavzular:


- spacedagi vazifallarni tugatish
- for ichida for yozishni o'rganish
- list ichida list ochish va x_o oyinini yasash
- funksiya bilan ishlashni davom ettirish
- o'tilgan mavzularni takrorlash
- if ni ichida if ishlatish va buni mashq qilish
- dict, tuple, set, list ni takrorlash
- umumiy malumot turlarini bir martta qayta korib chiqish
- har bir malumot turining methodlari borlogini tushuntirish va asosiylarini korib chiqish
- operatorlarni takrorlash

"""

"""
names = ['behruz', 'bobur', 'behruz', 'olim', 'nodir', 'zokir', 'bobur']
1. Ushbu list ichida takrorlangan ismlarni olib tashlang. Bittasi qolsin.

2. Tepada berilgan list ichidagi ismlarni b harfi bilan boshlanadigan eng kam harfligini toping.

3. 1 dan 1000 gacha sonlar orasida 9 va 8 ga bo'linadigan sonlarni 2 ga bo'lib
 faqat butun qismini yangi listga qo'shib keting.

4. Sinfdagi bollarni ismi, familiyasi, yoshi va bahosini saqlaydigan dict yarating. 
   Userdan input orqali bolani ismini sorang agar u dictni ichida bor bolsa unga malumotlarini korsating.
   Yo'q bo'lsa uni dictga qo'shib qo'ying
   
5. Ko'paytrish jadvalini yasash

6. Paskal formulasiga togri keladigan sonlar ketma ketligini bir nechtasini chiqarib bering.
   3 4 5
   6 8 10
   9 12 15
   
7. Yulduzchalardan shakllar chizishni boshash
   - 90 gradusli uchburchak
   - peramida
   - 5x5 kvadrat
   - robm
   - yurakcha chizish


Jamoaviy masala:

- 1 dan 100 gacha sonlar orasiga 4 va 6 ga birdaniga bo'linadigan sonalrni bitta listga qo'shib eting.
Keyin usha list ichidagi sonlarni toq indexda joylashganlarini 3-darajaga oshiring. Keyin esa usha listdagi
sonlarni yig'indisini toping.

- 1 dan 100 gacha hamma tub sonlarni topib beradigan dastur tuzing.

"""

students = {
    'abdulloh': {
        'name': "Abdulloh",
        'score': 70,
        'last_name': "Asqarov",
        'age': 16,
    }
}
while True:
    name = input("Name: ")
    if name in students.keys():
        student = students[name]
        text = f"Name: {student['name']}\nAge: {student['age']}"
        print(text)
    else:
        age = int(input("Age: "))
        students[name] = {
            "name": name,
            "age": age
        }
        print("Qo'shildi")
