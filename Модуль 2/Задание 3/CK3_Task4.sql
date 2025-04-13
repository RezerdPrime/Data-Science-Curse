CREATE TABLE Printer_New (
    code INTEGER,
    model INTEGER,
    color_type VARCHAR(10),
    type VARCHAR(20),
    price NUMERIC(10,2)
);

INSERT INTO Printer_New (code, model, color_type, type, price)
SELECT code, model, color, type, price
FROM Printer;

DROP TABLE Printer;

ALTER TABLE Printer_New RENAME TO Printer;
