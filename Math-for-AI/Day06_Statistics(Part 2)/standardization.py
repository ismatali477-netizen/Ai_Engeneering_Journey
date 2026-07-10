import numpy as np
def standarize(data):
    return np.round((data-np.mean(data))/np.std(data),2)

data = np.array([10, 20, 30, 40, 50])
if __name__=="__main__":
    print(f"Standarized form: {standarize(data)}")