from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
def train_knn(hours,result):
    model=KNeighborsClassifier(n_neighbors=3)
    model.fit(hours,result)
    return model
def evaluate(model,hours,result):
    return accuracy_score(result,model.predict(hours))
hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
result = [0, 0, 0, 0, 1, 1, 1, 1]
if __name__ == "__main__":
    model = train_knn(hours, result)

    accuracy = evaluate(model, hours, result)

    print(f"Accuracy: {accuracy:.2f}")