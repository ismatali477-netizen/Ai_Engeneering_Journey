import pandas as pd
data = {
    "Name": ["Ali", "Sara", "Ram", "John", "Emma"],
    "Age": [20, 22, 21, 23, 24],
    "Marks": [85, 92, 78, 88, 95],
    "City": ["Kathmandu", "Pokhara", "Butwal", "Biratnagar", "Chitwan"]
}

df=pd.DataFrame(data)
print(df["Name"])
print(df[["Name","Marks"]])
print(df.loc[3])
print(df.loc[[1,4]])
print(df.loc[1:3,["Name","Age"]])
print(df.iloc[3])
print(df.iloc[[0,2]])
print(df.iloc[1:4,0:3])
