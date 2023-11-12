"""
1. Find the total number of orders placed by each customer who has placed more than 5 orders.
SELECT customer_id, COUNT(*) as order_count
FROM orders
GROUP BY customer_id
HAVING order_count > 5;

2. Har bir katagoriyada nechtadan product borligini toping va soni 5 tadan ko'p bo'lganlarini ko'rsating.
SELECT category, COUNT(*) as product_count
FROM products
GROUP BY category
HAVING product_count > 10;

3. 3 ta ko'p order bergan userlarni idlarini olib bering
SELECT user_id
FROM orders
GROUP BY user_id
HAVING COUNT(*) > 3;
"""