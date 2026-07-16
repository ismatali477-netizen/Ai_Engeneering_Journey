import pandas as pd
data = {
    "Student": ["Ali", "Sara", "Ram", "John"],
    "Age": [20, 22, 21, 23],
    "Marks": [85, 92, 78, 88]
}

df=pd.DataFrame(data)
print(df)
print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)