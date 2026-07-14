from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
def train_tree(hours,result):
    model=DecisionTreeClassifier()
    model.fit(hours,result)
    return model
def evaluate_tree(model,hours,result):
    return accuracy_score(result, model.predict(hours))

hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
result = [0, 0, 0, 0, 1, 1, 1, 1]
if __name__ == "__main__":
    model = train_tree(hours, result)
    accuracy = evaluate_tree(model, hours, result)
    print(f"Accuracy: {accuracy:.2f}")