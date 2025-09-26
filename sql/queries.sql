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
    SUM(UnitPrice * Quantity) AS total_spend
FROM sales_clean
GROUP BY CustomerID;

-- Average Order Value (AOV) per customer
SELECT
    CustomerID,
    COUNT(*) AS frequency,
    SUM(UnitPrice * Quantity) AS total_spend,
    SUM(UnitPrice * Quantity)/COUNT(*) AS avg_order_value
FROM sales_clean
GROUP BY CustomerID
ORDER BY avg_order_value DESC
LIMIT 10; 
