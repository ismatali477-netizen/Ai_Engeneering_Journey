from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier
wine=load_wine()
X=wine.data
y=wine.target
model=KNeighborsClassifier()
scores=cross_val_score(model,X,y,cv=5)
print(scores)
print(f"Average Accuracy:\n{scores.mean():.2f}")