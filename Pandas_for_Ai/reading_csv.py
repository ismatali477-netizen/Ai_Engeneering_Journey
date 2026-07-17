import pandas as pd
df=pd.read_csv("Pandas_for_Ai/students.csv")
print(df)
print(pd.read_csv("Pandas_for_Ai/students.csv",usecols=["Name","Marks"]))
print(pd.read_csv("Pandas_for_Ai/students.csv",nrows=3))
df.to_csv("Pandas_for_Ai/output.csv",index=False)