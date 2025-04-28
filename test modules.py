import pandas as pd
import numpy as np


a = np.array([[0,1],[2,3]])
print(a)

b = pd.DataFrame(a, index = ["A", "B"])
print(b)



import numpy as np
def determinant(matrix):
    det = 0
    if matrix.shape[0]==1:
        det = matrix[0][0]
    if matrix.shape[0]==2:
        det = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    else:
        for i in range(matrix.shape[0]):
            if i == 0:
                submatrix = matrix[i+1:,1:]
            elif i == matrix.shape[0]:
                submatrix = matrix[:i-1,1:]
            else :
                submatrix1 = matrix[i+1:,1:]
                submatrix2 = matrix[i+1:,1:]
                submatrix = np.array(submatrix1,submatrix2)
            det += (-1)**i * matrix[0][i] * determinant(submatrix)
    return det


a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
det_a = determinant(a)
print(det_a)