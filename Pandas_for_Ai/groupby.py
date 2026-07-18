import pandas as pd
data = {
    "Name": ["Ali", "Sara", "Ram", "John", "Emma", "David"],
    "City": ["Kathmandu", "Pokhara", "Kathmandu", "Pokhara", "Chitwan", "Kathmandu"],
    "Marks": [85, 92, 78, 88, 95, 91],
    "Age": [20, 22, 21, 23, 24, 22]
}

df=pd.DataFrame(data)
print(df.groupby(["City"])["Marks"].mean())
print(df.groupby(["City"])["Marks"].max())
print(df.groupby(["City"])["Marks"].min())
print(df.groupby(["City"])["Marks"].sum())
print(df.groupby(["City"])["Marks"].count())
print(df.groupby(["City"])["Marks"].agg(["mean","max","min","sum","count"]))
print(df.groupby(["City"])["Marks"].size())
print(df.groupby(["City"])["Marks"].mean().reset_index())