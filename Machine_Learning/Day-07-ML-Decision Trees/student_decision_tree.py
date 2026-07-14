from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
def train_student_tree(students,passed):
    model=DecisionTreeClassifier()
    model.fit(students,passed)
    return model
def predict_student(model,students):
    return model.predict(students)
def evaluate(model,students,passed):
    return accuracy_score(passed,model.predict(students))

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
    model = train_student_tree(students, passed)

    prediction = predict_student(model, [[5.5, 82]])

    accuracy = evaluate(model, students, passed)

    print(f"Prediction: {'Pass' if prediction[0] else 'Fail'}")
    print(f"Accuracy: {accuracy:.2f}")