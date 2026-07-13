from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
def prepare_data(features, labels):
    return train_test_split(features,labels,test_size=0.25,random_state=42)
def train_model(X_train, y_train):
    model=LinearRegression()
    model.fit(X_train,y_train)
    return model
def evaluate_model(model, X_test, y_test):
    return r2_score(y_test,model.predict(X_test))
def predict_marks(model, hours):
    return model.predict(hours)
if __name__ == "__main__":
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    scores = [35, 45, 55, 65, 75, 85, 92, 96]
    X_train, X_test, y_train, y_test = prepare_data(hours, scores)
    model = train_model(X_train, y_train)
    r2 = evaluate_model(model, X_test, y_test)
    prediction = predict_marks(model, [[5.5]])
    print(f"Test R² Score: {r2:.3f}")
    print(f"Predicted marks for 5.5 hours: {prediction[0]:.2f}")