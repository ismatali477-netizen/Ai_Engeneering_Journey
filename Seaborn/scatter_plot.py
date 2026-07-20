import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = {
    "Hours_Slept": [5, 6, 7, 8, 9, 10],
    "Energy_Level": [45, 55, 68, 80, 90, 95]
}
df=pd.DataFrame(data)
sns.scatterplot(data=df,x="Hours_Slept",y="Energy_Level")
plt.title("Sleep vs Energy Level")
plt.xlabel("Hours_Slept")
plt.ylabel("Energy_Level")
plt.show()