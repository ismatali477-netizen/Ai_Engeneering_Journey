from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
def train_student_model(features, labels):
    model=LinearRegression()
    model.fit(features,labels)
    return model
def predict_marks(model, study_hours):
    return model.predict(study_hours)
if __name__ == "__main__":
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    scores = [35, 45, 55, 65, 75, 85, 92, 96]

    model = train_student_model(hours, scores)

    prediction = predict_marks(model, [[5.5]])

    print(f"Predicted marks for 5.5 study hours: {prediction[0]:.2f}")
