import pandas as pd

df = pd.read_csv('cereal.csv')

print(df.head())
print(df.info())
print(df.describe())

print(df.columns)
print(df.shape)





