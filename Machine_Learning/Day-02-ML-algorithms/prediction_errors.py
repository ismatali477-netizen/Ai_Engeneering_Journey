import numpy as np
def absolute_errors(actual, predicted):
    return np.absolute(actual-predicted)

def mean_absolute_error(actual, predicted):
    return np.mean(absolute_errors(actual,predicted))
if __name__=="__main__":
    actual = np.array([50, 60, 70, 80])
    predicted = np.array([52, 58, 69, 81])
    print("Absolute Errors:", absolute_errors(actual, predicted))
    print("MAE:", mean_absolute_error(actual, predicted))