WITH DuplicatePCs AS (
    SELECT
        code,
        model,
        speed,
        ram,
        hdd,
        cd,
        price,
        ROW_NUMBER() OVER (PARTITION BY model, speed, ram, hdd, cd, price ORDER BY code) AS RowNum
    FROM PC
)
SELECT *
FROM DuplicatePCs
WHERE RowNum > 1;


WITH DuplicateLaptops AS (
    SELECT
        code,
        model,
        speed,
        ram,
        hdd,
        screen,
        price,
        ROW_NUMBER() OVER (PARTITION BY model, speed, ram, hdd, screen, price ORDER BY code) AS RowNum
    FROM Laptop
)
SELECT *
FROM DuplicateLaptops
WHERE RowNum > 1;


WITH DuplicatePrinters AS (
    SELECT
        code,
        model,
        color,
        type,
        price,
        ROW_NUMBER() OVER (PARTITION BY model, color, type, price ORDER BY code) AS RowNum
    FROM Printer
)
SELECT *
FROM DuplicatePrinters
WHERE RowNum > 1;
