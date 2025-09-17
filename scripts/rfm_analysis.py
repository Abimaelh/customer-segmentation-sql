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
    SUM(UnitPrice * Quantity) AS total_spend
FROM sales_clean
GROUP BY CustomerID
ORDER BY total_spend DESC
LIMIT 10;
"""

df = pd.read_sql(query, conn)
conn.close()

#print(df.head())
#print(df.info())
#print(df.columns)

plt.figure(figsize=(10,6))
sns.barplot(data=df, x = "customerid", y = "total_spend")
plt.xticks(rotation = 45)
plt.title("Top 10 Customers by Total Spend")
plt.tight_layout()
plt.show()

# rfm analysis next