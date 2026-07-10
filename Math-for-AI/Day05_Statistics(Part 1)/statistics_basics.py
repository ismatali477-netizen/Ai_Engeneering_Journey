import numpy as np
from statistics import mode
def mean_score(data):
    return np.mean(data)
def median_score(data):
    return np.median(data)
def mode_score(data):
    return mode(data)
def range_score(data):
    return np.max(data)-np.min(data)
students =np.array([90, 85, 85, 70, 95])
if __name__=="__main__":
    print(f"Mean:{mean_score(students)}")
    print(f"Median:{median_score(students)}")
    print(f"Mode:{mode_score(students)}")
    print(f"Range:{range_score(students)}")