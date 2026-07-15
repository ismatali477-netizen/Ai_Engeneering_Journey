from sklearn.neighbors import KNeighborsClassifier
def train_knn(hours,result):
    model=KNeighborsClassifier(n_neighbors=3)
    model.fit(hours,result)
    return model
def predict_result(model,hours):
    return model.predict(hours)
students = [
    [1, 70],
    [2, 60],
    [3, 75],
    [4, 65],
    [5, 80],
    [6, 85],
    [7, 90],
    [8, 95]
]

passed = [0, 0, 0, 0, 1, 1, 1, 1]
if __name__ == "__main__":
    model = train_knn(students, passed)

    prediction = predict_result(model, [[6, 82]])

    print(f"Prediction: {prediction[0]}")