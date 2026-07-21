from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
iris=load_iris()
X=iris.data
pca=PCA(n_components=3)
X_new=pca.fit_transform(X)
print(f"Original Shape: {X.shape}")
print(f"New Shape: {X_new.shape}")
print(f"Explained Variance Ratio: {pca.explained_variance_ratio_}")