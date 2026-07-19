import pandas as pd
data = {
    "Name": ["Ali", "Sara", "Ram", "John", "Emma"],
    "Math": [85, 92, 78, 88, 95],
    "Science": [80, 94, 75, 90, 98],
    "Age": [20, 22, 21, 23, 24]
}

df=pd.DataFrame(data)
df["Total"]=df["Math"]+df["Science"]
df["Average"]=df[["Math","Science"]].mean(axis=1)
df["Result"]=df["Average"]>=80
df["Result"]=df["Result"].map({True:"Pass",False:"Fail"})
df["Age_Group"]=pd.cut(df["Age"],bins=[0,20,22,30],labels=["Young","Adult","Senior"])
df["Average"]=df["Average"].round(1)
df["Math"]=df["Math"].apply(lambda x: x+5)
df=df.sort_values("Average",ascending=False)
df=df.reset_index(drop=True)
print(df)