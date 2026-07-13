from sklearn.preprocessing import StandardScaler
import numpy as np
def standardize_data(data):
    scaler=StandardScaler()
    return np.round(scaler.fit_transform(data),2)
if __name__=="__main__":
    data = np.array([[10],[20],[30],[40],[50]])
    print(standardize_data(data))