SELECT model, price, 'PC' AS device_type
FROM PC
WHERE price > 500 AND ram = 64

UNION ALL

SELECT model, price, 'Laptop' AS device_type
FROM Laptop
WHERE price > 500 AND ram = 64;
