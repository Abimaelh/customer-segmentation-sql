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

-- Total Customers (cleaned)
SELECT COUNT(DISTINCT CustomerID)
FROM sales_clean;

-- Top 10 spenders
SELECT 
    CustomerID,
    SUM(Quantity * UnitPrice) AS total_spend
FROM sales_clean
GROUP BY CustomerID
ORDER BY total_spend DESC
LIMIT 10;

-- RFM Segmentation
SELECT
    CustomerID,
    MAX(InvoiceDate) AS last_purchase,
    COUNT(*) AS frequency,
    SUM(UnitPrice * Quantity) AS monetary
FROM sales_clean
GROUP BY CustomerID;