from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
def train_student_knn(students,result):
    model=KNeighborsClassifier(n_neighbors=3)
    model.fit(students,result)
    return model
def predict_student(model,students):
    return model.predict(students)
def evaluate(model,students,result):
    return accuracy_score(result,model.predict(students))

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
    model = train_student_knn(students, passed)

    prediction = predict_student(model, [[5.5, 82]])

    accuracy = evaluate(model, students, passed)

    print(f"Prediction: {'Pass' if prediction[0] else 'Fail'}")
    print(f"Accuracy: {accuracy:.2f}")