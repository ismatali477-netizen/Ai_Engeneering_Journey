import numpy as np
def student_matrix_info(matrix):
    return (matrix.shape,float(np.linalg.det(matrix)),int(np.linalg.matrix_rank(matrix)))

def transform_scores(matrix):
    return np.round(np.linalg.inv(matrix),3)

def is_invertible(matrix):
    return np.linalg.det(matrix)!=0
students = np.array([
    [90, 85],
    [78, 88]
])
if __name__ == "__main__":
    print(f"Matrix Info: {student_matrix_info(students)}")
    print(f"\nInverse Matrix:\n{transform_scores(students)}")
    print(f"\nInvertible: {is_invertible(students)}")