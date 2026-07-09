def multiply_matrix(A, B):
    if len(A)!=len(B[0]):
        raise ValueError("Row of matrix A must be equal to column of matrix B!!")
    result=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(B[0])):
            total=0
            for k in range(len(A[0])):
                total+=A[i][k]*B[k][j]
            row.append(total)
        result.append(row)
    return result
if __name__=="__main__":
    A = [
        [1,2],
        [3,4]
    ]
    B = [
        [5,6],
        [7,8]
    ]
    print(multiply_matrix(A,B))