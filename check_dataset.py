import pandas as pd

df = pd.read_csv("phishing_site_urls.csv")

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())

print("\nLabel Counts:")
print(df["Label"].value_counts())