import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = {
    "Department": [
        "AI",
        "Web",
        "AI",
        "Cyber",
        "Web",
        "AI",
        "Cyber",
        "AI"
    ]
}
df=pd.DataFrame(data)
sns.countplot(data=df,x="Department")
plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()