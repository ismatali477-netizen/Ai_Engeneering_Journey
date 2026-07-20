import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = {
    "Age": [18, 19, 20, 21, 22, 22, 23, 24, 25, 60]
}
df=pd.DataFrame(data)
sns.boxplot(data=df,y="Age")
plt.title("Age Distribution")
plt.ylabel("Age")
plt.show()