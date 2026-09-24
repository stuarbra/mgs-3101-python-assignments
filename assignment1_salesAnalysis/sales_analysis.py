import pandas as pd
df = pd.read_excel("Coffee Shop Sales.xlsx")
print(df.head())
print(df.columns)
print(df.info())