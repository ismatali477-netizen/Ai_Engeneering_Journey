from sklearn.datasets import load_iris
from sklearn.model_selection import RandomizedSearchCV
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X=iris.data
y=iris.target
model=KNeighborsClassifier()
params = {
    "n_neighbors": [3,5,7,9,11,13]
}
grid=RandomizedSearchCV(
    estimator=model,
    param_distributions=params,
    n_iter=4,
    cv=5,
    random_state=42
)
grid.fit(X,y)
print(f"Best Parameters:\n{grid.best_params_}")
print(f"Best Score: {grid.best_score_:.2f}")