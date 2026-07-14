from sklearn.ensemble import RandomForestClassifier
def train_forest(students,passed):
    model=RandomForestClassifier()
    model.fit(students,passed)
    return model
def predict_result(model,students):
    return model.predict(students)
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
    model = train_forest(students, passed)

    prediction = predict_result(model, [[6, 82]])

    print(f"Prediction: {prediction[0]}")