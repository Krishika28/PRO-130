import pandas as pd

df = pd.read_csv("merged_data.csv")


del df["Distance"]
del df["Mass"]
del df["Radius"]
del df["Star_name"]

print(df.columns)

df.to_csv("main.csv")

data = pd.read_csv("main.csv")

print(df[0:5])
