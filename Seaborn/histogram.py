import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = {
    "Marks": [55, 60, 62, 65, 70, 72, 75, 80, 82, 85, 90, 95]
}
df=pd.DataFrame(data)
sns.histplot(data=df,x="Marks")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Count")
plt.show()