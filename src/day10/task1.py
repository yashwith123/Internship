import pandas as pd


df = pd.read_csv("customer_orders.csv")

print("Shape before cleaning:", df.shape)

print("\nMissing values in each column:")
print(df.isna().sum())

numeric_cols = df.select_dtypes(include=['number']).columns
for col in numeric_cols:
    median_value = df[col].median()
    df[col].fillna(median_value, inplace=True)

df = df.drop_duplicates()

print("\nShape after cleaning:", df.shape)
