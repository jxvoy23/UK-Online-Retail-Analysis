import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -------------------------------
# Load dataset
# -------------------------------
file_path = '/Users/j.xvoy/Downloads/Online Retail.xlsx'
df = pd.read_excel(file_path)

# -------------------------------
# Preprocessing
# -------------------------------
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df = df[df["Description"].notna()]
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

sns.set_style("whitegrid")

# -------------------------------
# Create output folders
# -------------------------------
figures_folder = "figures"
csv_folder = "csv_reports"
os.makedirs(figures_folder, exist_ok=True)
os.makedirs(csv_folder, exist_ok=True)

# -------------------------------
# 1. Top country by products bought
# -------------------------------
top_country = df.groupby("Country")["Quantity"].sum().idxmax()
print("Country with the most products bought:", top_country)

# -------------------------------
# 2. Top product overall
# -------------------------------
top_product = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(1)
top_product_df = top_product.reset_index()
top_product_df.columns = ["Product", "Total_Quantity"]
top_product_df.to_csv(f"{csv_folder}/top_product_overall.csv", index=False)
print("Top product saved to CSV.")

# -------------------------------
# 3. Top product in Holiday Season (Dec 2010)
# -------------------------------
df_dec2010 = df[(df["InvoiceDate"].dt.year == 2010) & (df["InvoiceDate"].dt.month == 12)]
if not df_dec2010.empty:
    top_holiday_product = df_dec2010.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(1)
    top_holiday_df = top_holiday_product.reset_index()
    top_holiday_df.columns = ["Product", "Total_Quantity"]
    top_holiday_df.to_csv(f"{csv_folder}/top_holiday_product_dec2010.csv", index=False)
    print("Top holiday product saved to CSV.")
else:
    print("No data available for December 2010.")

# -------------------------------
# 4. Average revenue per day
# -------------------------------
daily_revenue = df.groupby(df["InvoiceDate"].dt.date)["Revenue"].sum()
avg_revenue_per_day = daily_revenue.mean()
avg_revenue_df = pd.DataFrame({"Average_Revenue_Per_Day": [avg_revenue_per_day]})
avg_revenue_df.to_csv(f"{csv_folder}/average_revenue_per_day.csv", index=False)
print("Average revenue per day saved to CSV.")

# -------------------------------
# 5. Top 5 countries by products sold
# -------------------------------
top_countries_by_quantity = df.groupby("Country")["Quantity"].sum().sort_values(ascending=False).head(5)
top_countries_df = top_countries_by_quantity.reset_index()
top_countries_df.columns = ["Country", "Total_Quantity"]
top_countries_df.to_csv(f"{csv_folder}/top_5_countries_products.csv", index=False)
print("Top 5 countries by products saved to CSV.")

# -------------------------------
# 6. Average daily revenue for top 5 countries
# -------------------------------
avg_daily_rev_list = []
for country in top_countries_by_quantity.index:
    daily_rev = df[df["Country"] == country].groupby(df["InvoiceDate"].dt.date)["Revenue"].sum()
    avg_daily_rev_list.append({"Country": country, "Average_Revenue_Per_Day": daily_rev.mean()})

avg_daily_rev_df = pd.DataFrame(avg_daily_rev_list)
avg_daily_rev_df.to_csv(f"{csv_folder}/top_5_countries_avg_daily_revenue.csv", index=False)
print("Average daily revenue per top country saved to CSV.")

# -------------------------------
# 7. Total revenue per top country for a specific year (2011)
# -------------------------------
year = 2011
yearly_rev_list = []
for country in top_countries_by_quantity.index:
    yearly_rev = df[(df["Country"] == country) & (df["InvoiceDate"].dt.year == year)]["Revenue"].sum()
    yearly_rev_list.append({"Country": country, "Year": year, "Total_Revenue": yearly_rev})

yearly_rev_df = pd.DataFrame(yearly_rev_list)
yearly_rev_df.to_csv(f"{csv_folder}/top_5_countries_yearly_revenue.csv", index=False)
print("Yearly revenue per top country saved to CSV.")

# -------------------------------
# 8. Visualizations (PNG)
# -------------------------------

# Daily revenue over time
plt.figure(figsize=(12,5))
daily_revenue.plot()
plt.title("Daily Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(f"{figures_folder}/daily_revenue_over_time.png")
plt.close()

# Top 10 products by quantity
top_products_chart = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_products_chart.values, y=top_products_chart.index, palette="viridis")
plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Units Sold")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(f"{figures_folder}/top_10_products.png")
plt.close()

# Top 5 countries by revenue
top_countries_rev = df.groupby("Country")["Revenue"].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(8,5))
sns.barplot(x=top_countries_rev.values, y=top_countries_rev.index, palette="coolwarm")
plt.title("Top 5 Countries by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig(f"{figures_folder}/top_5_countries_revenue.png")
plt.close()

# Daily revenue trend for top 5 countries
plt.figure(figsize=(12,6))
for country in top_countries_rev.index:
    daily_rev_country = df[df["Country"] == country].groupby(df["InvoiceDate"].dt.date)["Revenue"].sum()
    daily_rev_country.plot(label=country)
plt.title("Daily Revenue Trend for Top 5 Countries")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.legend()
plt.tight_layout()
plt.savefig(f"{figures_folder}/daily_revenue_top_countries.png")
plt.close()

print(f"All figures saved in '{figures_folder}' and CSV reports saved in '{csv_folder}'")
