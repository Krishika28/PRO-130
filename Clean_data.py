import pandas as pd

df = pd.read_csv("merged_data.csv")
print(df[0:5])
print(df.columns)

df.drop(["Unnamed: 0", "Star_name.1", "Luminosity","Distance.1", "Radius.1", "Mass.1" ], axis=1, inplace=True)
df = df.dropna()


df.to_csv("main.csv")

data = pd.read_csv("main.csv")

print(df[0:5])