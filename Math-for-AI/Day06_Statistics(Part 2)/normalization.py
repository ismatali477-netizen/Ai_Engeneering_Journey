import numpy as np
def min_max_normalize(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))
data = np.array([10, 20, 30, 40, 50])
if __name__=="__main__":
    print(f"Normalised form: {min_max_normalize(data)}")