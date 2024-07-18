import numpy as np

def swap_rows(M, a, b):
    temp_arr = M[a].copy()
    M[a] = M[b]
    M[b] = temp_arr
def swap_cols(M, a, b):
    temp_arr = M[:, a].copy()
    M[:, a] = M[:, b]
    M[:, b] = temp_arr
    
arr = np.array([[0,1,2,3,4,5],
       [10,11,12,13,14,15],
       [20,21,22,23,24,25],
       [30,31,32,33,34,35],
       [40,41,42,43,44,45],
       [50,51,52,53,54,55]
       ])
swap_rows(arr, 0, 1)
print(arr)
swap_cols(arr, 0, 1)
print(arr)