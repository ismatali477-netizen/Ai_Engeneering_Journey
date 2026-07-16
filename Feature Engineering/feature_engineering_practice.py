import pandas as pd
from sklearn.preprocessing import StandardScaler
data = {
    "Age": [20, 22, None, 25, 24],
    "Gender": ["Male", "Female", "Female", "Male", "Male"],
    "Salary": [25000, 40000, 35000, 60000, 50000]
}
df=pd.DataFrame(data)
df['Age'] = df['Age'].fillna(df['Age'].mean())
print("Missing values handled:")
print(df)
encoded_df= pd.get_dummies(df, columns=['Gender'], drop_first=False)
print("\nOne-Hot Encoded:")
print(encoded_df)

# print("\nScaled Numerical Features:")
# print(scaled_df)