from sklearn.ensemble import RandomForestClassifier
def train_forest(hours,result):
    model=RandomForestClassifier()
    model.fit(hours,result)
    return model
def predict_result(model,hours):
    return model.predict(hours)

hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
result = [0, 0, 0, 0, 1, 1, 1, 1]
if __name__ == "__main__":
    model = train_forest(hours, result)

    prediction = predict_result(model, [[5.5]])

    print(f"Prediction: {prediction[0]}")