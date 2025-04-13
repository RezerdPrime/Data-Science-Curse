SELECT model, price
FROM Printer
WHERE price = (
    SELECT MAX(price)
    FROM Printer
);

SELECT AVG(speed) AS average_speed
FROM PC;

SELECT DISTINCT maker
FROM Product
WHERE type = 'PC'
AND maker NOT IN (
    SELECT DISTINCT maker
    FROM Product
    WHERE type = 'Laptop'
);
