import pandas as pd

df = pd.read_csv('cereal.csv')
print(df.describe())
print(df.describe()["Sugars"])




