import pandas as pd
import numpy as np

data = {
    "Student_ID": [101, 102, 103, 104, 105, 105],
    "Name": ["Ali", "Sara", "Ram", "John", "Emma", "Emma"],
    "Math": [85, 92, np.nan, 88, 95, 95],
    "Science": [80, 94, 75, np.nan, 98, 98],
    "Age": [20, 22, 21, 23, np.nan, np.nan],
    "City": ["Kathmandu", "Pokhara", "Kathmandu", "Pokhara", "Chitwan", "Chitwan"]
}
df=pd.DataFrame(data)
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df.isnull().sum())
print(df.isnull().sum().sum())
df["Math"]=df["Math"].fillna(df["Math"].mean())
df["Science"]=df["Science"].fillna(df["Science"].mean())
df["Age"]=df["Age"].fillna(df["Age"].mean())
df=df.drop_duplicates()
df["Total"]=df["Math"]+df["Science"]
df["Average"]=df[["Math","Science"]].mean(axis=1)
df["Result"]=(df["Average"]>=80).map({True:"Pass",False:"Fail"})
df["Age_Group"]=pd.cut(df["Age"],bins=[0,20,22,30],labels=["Young","Adult","Senior"])
df=df.sort_values("Average",ascending=False)
df=df.reset_index(drop=True)
print(df)
print(df.groupby(["City"])[["Math","Science"]].mean())