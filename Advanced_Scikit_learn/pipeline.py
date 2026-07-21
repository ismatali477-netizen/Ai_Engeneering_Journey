from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.pipeline import Pipeline

iris=load_iris()
X=iris.data
y=iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
pipeline=Pipeline([
    ("scaler",StandardScaler()),
    ("tree",DecisionTreeClassifier())
])
pipeline.fit(X_train,y_train)
accuracy=pipeline.score(X_test,y_test)
print(f"Accuracy:{accuracy:.2f}")