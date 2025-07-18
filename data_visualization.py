import pandas as pd

# Load the dataset
df = pd.read_csv("sample_sales_data.csv")
df.head()
df.info()
df.describe()
df.isnull().sum()
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

import matplotlib.pyplot as plt
import seaborn as sns
#total_revenue_by_category
category_sales = df.groupby("Category")["Total_Amount"].sum().reset_index()
sns.barplot(x="Category", y="Total_Amount", data=category_sales)
plt.title("Total Revenue by Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.savefig("total_revenue_by_category.png")
plt.show()
#orders_over_time
daily_sales = df.groupby("Order_Date")["Total_Amount"].sum().reset_index()
plt.figure(figsize=(12, 5))
sns.lineplot(x="Order_Date", y="Total_Amount", data=daily_sales)
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.savefig("orders_over_time.png")
plt.show()
#quantity_distribution_by_customer
sns.boxplot(x="Customer", y="Quantity", data=df)
plt.title("Quantity Distribution by Customer")
plt.savefig("quantity_distribution_by_customer.png")
plt.show()
#correlation_heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.savefig("correlation_heatmap.png")
plt.show()
#total_revenue_by_customer
customer_sales = df.groupby("Customer")["Total_Amount"].sum().reset_index()
sns.barplot(x="Customer", y="Total_Amount", data=customer_sales)
plt.title("Total Revenue by Customer")
plt.savefig("total_revenue_by_customer.png")
plt.show()






