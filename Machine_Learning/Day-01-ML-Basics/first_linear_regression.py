from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
def train_model(features, labels):
    X_train,X_test,y_train,y_test=train_test_split(features,labels)
    model=LinearRegression()
    model.fit(X_train,y_train)
    return model

def predict_score(model, hours):
    return model.predict(hours)
hours = [[2], [4], [6], [8]]
scores = [45, 60, 75, 90]
if __name__ == "__main__":
    model = train_model(hours, scores)
    prediction = predict_score(model, [[5]])
    print(f"Predicted score: {prediction[0]:.2f}")
    