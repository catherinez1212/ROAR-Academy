import numpy as np

arr = np.array([[0,1,2,3,4,5],
       [10,11,12,13,14,15],
       [20,21,22,23,24,25],
       [30,31,32,33,34,35],
       [40,41,42,43,44,45],
       [50,51,52,53,54,55]
       ])
subarr1 = arr[:,1]
print(subarr1)
subarr2 = arr[1, 2:4]
print(subarr2)
subarr3 = arr[2:4, 4:]
print(subarr3)