import pandas as pd
data = {
    "Name": ["Ali", "Sara", "Ram", "John", "Emma"],
    "Age": [20, 22, 21, 23, 24],
    "Marks": [85, 92, 78, 88, 95],
    "City": ["Kathmandu", "Pokhara", "Butwal", "Kathmandu", "Chitwan"]
}

df=pd.DataFrame(data)
print(df.head(3))
print(df.tail(3))
df.info()
print(df.describe())
print(df.sample(2))
print(df["City"].value_counts())
print(df["City"].unique())
print(df["City"].nunique())