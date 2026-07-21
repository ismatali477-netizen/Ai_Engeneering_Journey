import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "Department": ["AI", "AI", "Web", "Web", "Cyber", "AI"],
    "Salary": [60000, 70000, 50000, 55000, 65000, 72000],
    "Age": [24, 26, 23, 25, 27, 28],
    "Experience": [2, 3, 1, 2, 4, 5]
}
df=pd.DataFrame(data)
corr=df.select_dtypes(include=["number"]).corr()
sns.countplot(data=df,x="Department")
plt.title("Employees by Department")
plt.show()
sns.barplot(data=df,x="Department",y="Salary")
plt.title("Average Salary by Department")
plt.show()
sns.histplot(data=df,x="Age")
plt.title("Age Distribution")
plt.show()
sns.boxplot(data=df,y="Salary")
plt.title("Salary Distribution")
plt.show()
sns.scatterplot(data=df,x="Experience",y="Salary")
plt.title("Experience vs Salary")
plt.show()
sns.heatmap(corr,annot=True)
plt.title("Feature Correlation")
plt.show()