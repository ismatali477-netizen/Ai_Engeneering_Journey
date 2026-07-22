import joblib
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
wine = load_wine()
X=wine.data
y=wine.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=RandomForestClassifier(random_state=42)
model.fit(X_train,y_train)
joblib.dump(model,"wine_model.pkl")
loaded_model=joblib.load("wine_model.pkl")
print(f"Accuracy: {loaded_model.score(X_test,y_test):.2f}")