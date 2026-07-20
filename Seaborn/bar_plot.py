import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = {
    "Course": [
        "Python",
        "Python",
        "AI",
        "AI",
        "Web",
        "Web"
    ],
    "Score": [80, 90, 85, 95, 70, 75]
}
df=pd.DataFrame(data)
sns.barplot(data=df,x="Course",y="Score")
plt.title("Average Score by Course")
plt.xlabel("Course")
plt.ylabel("Average Score")
plt.show()