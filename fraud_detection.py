import pandas as pd

data = pd.read_csv("creditcard.csv")

print(data.head())

print("Rows:", len(data))