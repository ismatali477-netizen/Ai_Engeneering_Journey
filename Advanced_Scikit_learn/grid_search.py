from sklearn.datasets import load_wine
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

wine = load_wine()
X=wine.data
y=wine.target
model=DecisionTreeClassifier()
params={
    "max_depth":[3,5,7,9]
}
grid=GridSearchCV(
    estimator=model,
    param_grid=params,
    cv=5
)
grid.fit(X,y)
print(f"Best Parameters:\n{grid.best_params_}")
print(f"Best Score: {grid.best_score_:.2f}")