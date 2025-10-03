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

# Remove null values
df = df[df['total_spend'] > 0]

# break into quintiles
df['R_quartile'] = pd.qcut(df['recency'], 5, labels=[5,4,3,2,1])
df['F_quartile'] = pd.qcut(df['frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
df['M_quartile'] = pd.qcut(df['total_spend'], 5, labels=[1,2,3,4,5]) #monetary

# compute RFM score
df['RFM_Score'] = df['R_quartile'].astype(str) + df['F_quartile'].astype(str) + df['M_quartile'].astype(str)

# computer RFM score
df['RFM_Sum'] = df['R_quartile'].astype(int) + df['F_quartile'].astype(int) + df['M_quartile'].astype(int)

# plot RFM score
plt.figure(figsize=(8,6))
sns.histplot(df['RFM_Sum'], bins = 15, kde = True)
plt.title("Distribution of RFM Scores")
plt.xlabel("RFM Sum")
plt.ylabel("Number of Customers")
plt.show