from sklearn.linear_model import LogisticRegression
def train_classifier(features, labels):
    model = LogisticRegression()
    model.fit(features,labels)
    return model

def predict_result(model, hours):
    return model.predict(hours)
if __name__=="__main__":
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0,0,0,0,1,1,1,1]
    model = train_classifier(hours, result)
    prediction = predict_result(model, [[5.5]])
    print(f"Prediction: {prediction[0]}")