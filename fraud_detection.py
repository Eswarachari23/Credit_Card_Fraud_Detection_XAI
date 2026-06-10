import pandas as pd

data = pd.read_csv("creditcard.csv")

print("Dataset Loaded Successfully")
print(data.head())
print("Rows:", len(data))
print("Columns:", len(data.columns))