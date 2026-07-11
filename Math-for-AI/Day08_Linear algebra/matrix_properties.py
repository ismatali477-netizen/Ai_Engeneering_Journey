import numpy as np
def determinant(matrix):
    return np.linalg.det(matrix)

def inverse(matrix):
    return np.linalg.inv(matrix)

def rank(matrix):
    return np.linalg.matrix_rank(matrix)

A = np.array([
    [4, 7],
    [2, 6]
])
if __name__ == "__main__":
    print(f"Determinant: {determinant(A):.2f}")
    print(f"Inverse:\n{inverse(A)}")
    print(f"Rank: {rank(A)}")