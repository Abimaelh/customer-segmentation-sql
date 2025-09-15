-- Create sales table schema
CREATE TABLE sales (
    InvoiceNo VARCHAR(20),
    StockCode VARCHAR(20),
    Description TEXT,
    Quantity INT,
    InvoiceDate TIMESTAMP,
    UnitPrice NUMERIC,
    CustomerID VARCHAR(20),
    Country VARCHAR(50)
);

-- Create a clean sales table (remove NULL CustomerID values)
DROP TABLE IF EXISTS sales_clean;

CREATE TABLE sales_clean AS
SELECT *
FROM sales
WHERE CustomerID IS NOT NULL
    AND TRIM(CustomerID) <> '';