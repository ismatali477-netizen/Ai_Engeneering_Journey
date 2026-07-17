import pandas as pd
data = {
    "Name": ["Ali", "Sara", "Ram", "John", "Emma"],
    "Age": [20, None, 21, 23, 24],
    "Marks": [85, 92, None, 88, 95],
    "City": ["Kathmandu", "Pokhara", "Butwal", None, "Chitwan"]
}

df=pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.isnull().sum())
print(df.isnull().sum().sum())
print(df.dropna())
print(df.dropna(axis=1))
print(df.fillna(0))
print(df["Age"].fillna(df["Age"].mean()))
print(df["City"].fillna("Unknown"))
print(df.isnull().any())
