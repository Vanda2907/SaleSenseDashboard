import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
df = pd.read_excel("ecommerce_sales_dataset.xlsx")
df["Order Date"] = pd.to_datetime(df["Order Date"])
# Top 5 Products by Sales
product_analysis = df.groupby("Item Name")["Sales"].sum().reset_index()
product_analysis = product_analysis.sort_values(by="Sales", ascending=False).head(5)
print(product_analysis)
plt.figure(figsize=(10,5))
ax = sns.barplot(data=product_analysis,x="Item Name",y="Sales")
for i in ax.containers:
    ax.bar_label(i, fmt='{:,.0f}')
plt.ylim(0, product_analysis["Sales"].max()*1.2)
plt.title("Top 5 Products by Sales")
plt.xticks(rotation=45)
plt.show()