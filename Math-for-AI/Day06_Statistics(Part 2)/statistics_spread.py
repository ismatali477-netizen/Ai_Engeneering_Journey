import numpy as np
def variance_score(data):
    return np.var(data)
def std_score(data):
    return np.round(np.std(data),2)
scores = np.array([78,79,80,81,82])
if __name__=="__main__":
    print(f"Variance of scores: {variance_score(scores)}")
    print(f"Standard deviation of scores: {std_score(scores)}")