def add_matrix(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions.")
    return [[(A[i][j]+B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
def subtract_matrix(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions.")
    return [[(A[i][j]-B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
A = [
    [1,2],
    [3,4]
]
B = [
    [5,6],
    [7,8]
]
print(add_matrix(A,B))
print(subtract_matrix(A,B))