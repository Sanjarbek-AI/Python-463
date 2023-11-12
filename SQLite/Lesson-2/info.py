"""
Inserting bilan ishlash
Select bilan ishlashni boshlash

where, and, like, between, in, count, max, min

Darsda o'tiladigan mavzular:

SELECT => malumotlar bazasidan malumot olish uchun ishlatiladigan kod
    SELECT * FROM Customers;

AS => column name ni o'zgartirib olish uchun kerak

SELECT DISTINCT => bunday vaziyatda ikki bir xil value larni olmaydi
    SELECT DISTINCT Country FROM Customers;

COUNT => sorovdan qaytgan narsani nechta ekanligini sanash uchun ishlatiladi
    SELECT COUNT(DISTINCT Country) FROM Customers;

WHERE => so'rovga qandaydir shart berish uchun ishlatiladi, xuddi kodda if yozganimiz kabi
    SELECT column1, column2 FROM table_name WHERE condition;

LIKE =>
    SELECT * FROM Customers WHERE City LIKE 's%';

BETWEEN => 
    SELECT * FROM Products WHERE Price BETWEEN 50 AND 60;

IN => 
    SELECT * FROM Customers WHERE City IN ('Paris','London');

WHERE bilan ishlatiladigan operatorlar
LIKE
BETWEEN
IN
"""