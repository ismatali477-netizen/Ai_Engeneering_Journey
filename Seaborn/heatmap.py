import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = {
    "Height": [150, 160, 170, 180, 190],
    "Weight": [45, 55, 65, 75, 85],
    "Age": [18, 20, 22, 24, 26]
}
df=pd.DataFrame(data)
corr=df.corr()
sns.heatmap(corr,annot=True)
plt.title("Feature Correlation")
plt.show()