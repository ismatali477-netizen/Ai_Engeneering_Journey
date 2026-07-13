from sklearn.preprocessing import MinMaxScaler
import numpy as np

def minmax_scale(data):
    scale=MinMaxScaler()
    return np.round(scale.fit_transform(data),2)
if __name__=="__main__":
    data = np.array([[10], [20], [30], [40], [50]])
    print(minmax_scale(data))