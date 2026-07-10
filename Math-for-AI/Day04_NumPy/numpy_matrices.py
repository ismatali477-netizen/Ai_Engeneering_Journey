import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print(f"Addition of matrix is {A+B}")
print(f"Subtraction of matrix is {A-B}")
print(f"matrix multiplication is {A@B}")
print(f"Dimension of matrix A:{A.shape}")
print(f"Dimension of matrix B:{B.shape}")
print(f"Transpose of matrix A is {A.T}")