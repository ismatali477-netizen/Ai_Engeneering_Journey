import numpy as np
def mean_squared_error(actual, predicted):
    return  np.mean(np.absolute(actual-predicted)**2)
def root_mean_squared_error(actual, predicted):
    return np.sqrt(mean_squared_error(actual,predicted))
if __name__=="__main__":
    actual = np.array([50, 60, 70, 80])
    predicted = np.array([52, 58, 69, 81])
    print(f"MSE: {mean_squared_error(actual, predicted):.2f}")
    print(f"RMSE: {root_mean_squared_error(actual, predicted):.2f}")