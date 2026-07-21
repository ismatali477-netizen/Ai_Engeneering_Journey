from sklearn.datasets import load_wine
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
wine = load_wine()
X=wine.data
y=wine.target
selector=SelectKBest(
    score_func=f_classif,
    k=5
)
X_new=selector.fit_transform(X,y)
print(f"Original Shape: {X.shape}")
print(f"New Shape: {X_new.shape}")
print(f"Selected Feature Indices: {selector.get_support(indices=True)}")
print(f"Feature Scores: {selector.scores_}")