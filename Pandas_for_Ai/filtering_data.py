import pandas as pd
data = {
    "Name": ["Ali", "Sara", "Ram", "John", "Emma"],
    "Age": [20, 22, 21, 23, 24],
    "Marks": [85, 92, 78, 88, 95],
    "City": ["Kathmandu", "Pokhara", "Butwal", "Kathmandu", "Chitwan"]
}

df=pd.DataFrame(data)
print(df[df["Marks"]>90])
print(df[df["City"]=="Kathmandu"])
print(df[df["Age"]>=22])
print(df[df["Marks"]<90])
print(df[(df["Marks"]>90)&(df["Age"]>21)])
print(df[(df["Marks"]>90)|(df["City"]=="Butwal")])
print(df[~(df["City"]=="Kathmandu")])
print(df[df["City"].isin(["Kathmandu","Chitwan"])])
print(df[df["Marks"].between(80,90)])
print(df.loc[df["Marks"]>85,["Name","Marks"]])