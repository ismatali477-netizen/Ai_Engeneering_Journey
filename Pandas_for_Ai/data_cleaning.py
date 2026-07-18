import pandas as pd
data = {
    "student_name": ["Ali", "Sara", "Ram", "Ali", "Emma"],
    "age": [20, 22, 21, 20, 24],
    "marks": [85, 92, 78, 85, 95],
    "city": ["Kathmandu", "Pokhara", "Butwal", "Kathmandu", "Chitwan"]
}

df=pd.DataFrame(data)
print(df.duplicated())
print(df.duplicated().sum())
df=df.drop_duplicates()
df= df.rename(columns={
    "student_name":"Name",
    "age":"Age",
    "marks":"Marks",
    "city":"City"    
})
df["Age"]=df["Age"].astype(int)
df=df.drop(columns=["City"])
df=df.sort_values(by="Marks",ascending=False)
df=df.reset_index(drop=True)
print(df)