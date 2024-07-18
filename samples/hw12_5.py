import numpy as np


def set_array(L, rows, cols):
    index = 0
    result = np.zeros(shape=(rows, cols))
    for i in range(rows):
        for j in range(cols):
            result[i][j] = L[index]
            index += 1
    return result
    
L = [1,2,3,4,5,6]
result = set_array(L, 2, 3)
print(result)
        