from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
def train_model(features, labels):
    model=LogisticRegression()
    model.fit(features,labels)
    return model

def evaluate_model(model, features, labels):
    return accuracy_score(labels,model.predict(features))

def predict_student(model, study_hours):
    return model.predict(study_hours)
hours = [
    [1], [2], [3], [4],
    [5], [6], [7], [8]
]
result = [
    0, 0, 0, 0,
    1, 1, 1, 1
]
if __name__ == "__main__":
    model = train_model(hours, result)
    accuracy = evaluate_model(model, hours, result)
    prediction = predict_student(model, [[6]])
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Prediction for 6 hours: {'Pass' if prediction[0] == 1 else 'Fail'}")