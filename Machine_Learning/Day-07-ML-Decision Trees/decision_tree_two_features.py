from sklearn.tree import DecisionTreeClassifier
def train_tree(hours,result):
    model=DecisionTreeClassifier()
    model.fit(hours,result)
    return model
def predict_result(model,hours):
    return model.predict(hours)
hours = [
    [1, 70],
    [2, 60],
    [3, 75],
    [4, 65],
    [5, 80],
    [6, 85],
    [7, 90],
    [8, 95]
]

result = [0, 0, 0, 0, 1, 1, 1, 1]
if __name__ == "__main__":
    model = train_tree(hours, result)

    prediction = predict_result(model, [[6, 82]])

    print(f"Prediction: {prediction[0]}")