import pandas as pd
df = pd.read_excel("Coffee Shop Sales.xlsx")
drinks = df[df["product_category"] == "Coffee"]
drinks_sold = drinks["transaction_qty"].sum()
price_per_drink = drinks["unit_price"].mean()
print(drinks_sold, price_per_drink)
bakery = df[df["product_category"] == "Bakery"]
bakery_sold = bakery["transaction_qty"].sum()
price_per_bakery = bakery["unit_price"].mean()
print(bakery_sold, price_per_bakery)
shop_name = "Mug Life"
print (shop_name)
drinks_revenue = drinks_sold * price_per_drink
bakery_revenue = bakery_sold * price_per_bakery
total_revenue = drinks_revenue + bakery_revenue
print(total_revenue)
if total_revenue >= 500:
    print ("revenue is at least 500")
else: 
    print ("revenue is less than 500")
df["revenue"] = df["transaction_qty"] * df["unit_price"]
sales_by_category = df.groupby("product_category")["revenue"].sum()
print(sales_by_category.sort_values(ascending=False))
sales_by_product = df.groupby("product_detail")["revenue"].sum()
print(sales_by_product.sort_values(ascending=False).head(5))
sales_by_store = df.groupby("store_location")["revenue"].sum()
print(sales_by_store.sort_values(ascending=False))