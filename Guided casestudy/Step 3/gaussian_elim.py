import numpy as np
import math

## Forming Hilbert matrix of order 10x10
s = 10
H = np.zeros((s, s))

for c in range(s):
    for r in range(s):
        H[c, r] = 1 / (c + r + 1)

n = len(H)     
print(n)   

## Inverse of Hilbert Matrix

a1 = np.linalg.det(H)
# print(1/a1)

import numpy as np
   
def matrix_cofactor(matrix):
 
    try:
        determinant = np.linalg.det(matrix)
        if(determinant!=0):
            cofactor = None
            cofactor = np.linalg.inv(matrix).T * determinant
            # return cofactor matrix of the given matrix
            return cofactor
        else:
            raise Exception("singular matrix")
    except Exception as e:
        print("could not find cofactor matrix due to",e)
   
p = matrix_cofactor(H).T
print(p)