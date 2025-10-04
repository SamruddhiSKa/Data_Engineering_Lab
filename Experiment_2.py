CREATE DATABASE DMA;
USE DMA;

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(15),
    City VARCHAR(50),
    State VARCHAR(50),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(100) NOT NULL,
    Category VARCHAR(50),
    Price DECIMAL(10,2) NOT NULL CHECK (Price >= 0),
    Stock INT DEFAULT 0 CHECK (Stock >= 0)
);

CREATE TABLE Sales (
    SaleID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL CHECK (Quantity > 0),
    TotalAmount DECIMAL(10,2) NOT NULL CHECK (TotalAmount >= 0),
    SaleDate DATE NOT NULL DEFAULT (CURRENT_DATE),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
        ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
        ON DELETE CASCADE
);

SELECT c.Name, SUM(s.TotalAmount) AS TotalSpent
FROM Sales s
JOIN Customers c ON s.CustomerID = c.CustomerID
GROUP BY c.Name;

SELECT p.ProductName, SUM(s.Quantity) AS TotalSold
FROM Sales s
JOIN Products p ON s.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY TotalSold DESC;

SELECT DATE_FORMAT(SaleDate, '%Y-%m') AS Month, SUM(TotalAmount) AS Revenue
FROM Sales
GROUP BY Month
ORDER BY Month;
