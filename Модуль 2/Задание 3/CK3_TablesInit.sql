CREATE TABLE Product (
    maker VARCHAR(50),
    model VARCHAR(50),
    type VARCHAR(20)
);

CREATE TABLE PC (
    code INT,
    model VARCHAR(50),
    speed INT,
    ram INT,
    hdd DECIMAL(5,2),
    cd VARCHAR(10),
    price DECIMAL(10,2)
);

CREATE TABLE Laptop (
    code INT,
    model VARCHAR(50),
    speed INT,
    ram INT,
    hdd DECIMAL(5,2),
    screen DECIMAL(3,1),
    price DECIMAL(10,2)
);

CREATE TABLE Printer (
    code INT,
    model VARCHAR(50),
    color CHAR(1),
    type VARCHAR(20),
    price DECIMAL(10,2)
);


