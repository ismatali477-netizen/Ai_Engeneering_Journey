from sklearn.metrics import r2_score
import numpy as np
from sklearn.linear_model import LinearRegression
def train_model(features, labels):
    model=LinearRegression()
    model.fit(features,labels)
    return model
def evaluate_model(model, features, labels):
    prediction=model.predict(features)
    return np.mean(np.absolute(prediction-labels)),np.mean((prediction-labels)**2),np.sqrt(np.mean((prediction-labels)**2)),r2_score(prediction,labels)
if __name__ == "__main__":
    hours = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
    scores = np.array([35, 45, 55, 65, 75, 85, 92, 96])

    model = train_model(hours, scores)

    mae, mse, rmse, r2 = evaluate_model(model, hours, scores)

    print(f"MAE : {mae:.2f}")
    print(f"MSE : {mse:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R²  : {r2:.3f}")