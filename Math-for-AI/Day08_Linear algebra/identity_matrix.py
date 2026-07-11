import numpy as np
def create_identity(size):
    return np.eye(size)
if __name__=="__main__":
    print(f"A 3X3 matrix is:\n{create_identity(3)}")