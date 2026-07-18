import pandas as pd
students = {
    "StudentID": [1, 2, 3, 4],
    "Name": ["Ali", "Sara", "Ram", "John"]
}

marks = {
    "StudentID": [1, 2, 3, 5],
    "Marks": [85, 92, 78, 90]
}

df_students=pd.DataFrame(students)
df_marks=pd.DataFrame(marks)
print(pd.merge(df_students,df_marks,on="StudentID"))
print(pd.merge(df_students, df_marks, on="StudentID", how="outer"))
print(pd.merge(df_students,df_marks,on="StudentID",how="left"))
print(pd.merge(df_students,df_marks,on="StudentID",how="right"))
students = {
    "ID": [1, 2, 3, 4],
    "Name": ["Ali", "Sara", "Ram", "John"]
} 
df_student=pd.DataFrame(students)
print(pd.merge(df_student,df_marks,left_on="ID",right_on="StudentID"))
