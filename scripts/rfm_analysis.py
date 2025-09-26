import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = psycopg2.connect(
    dbname = "ecommerce",
    user = "abimael",
    host="localhost",
    port = "5432"
)

query = """
SELECT
    CustomerID,
    DATE_PART('day', CURRENT_DATE - MAX(InvoiceDate)) AS recency,
    COUNT(*) AS frequency,
    SUM(UnitPrice * Quantity) AS total_spend
FROM sales_clean
GROUP BY CustomerID;
"""

df = pd.read_sql(query, conn)
conn.close()

#print(df.head())
#print(df.info())
#print(df.columns)

plt.figure(figsize=(10,6))
sns.barplot(data=df, x = "customerid", y = "total_spend")
plt.xticks(rotation = 45)
plt.title("RFM Segmentation")
plt.tight_layout()
plt.show()
