import numpy as np

arr1 = np.array([[6,-9, 1], [4,24,8]])
print(arr1*2)
arr2 = np.array([[1,0], [0, 1]])
result1 = np.dot(arr2, arr1)
print(result1)
arr3 = np.array([[4,3], [3, 2]])
arr4 = np.array([[-2, 3], [3, -4]])
result2 = np.dot(arr3, arr4)
print(result2)