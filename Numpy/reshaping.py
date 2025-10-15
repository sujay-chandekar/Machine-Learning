import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])
print("Array :")
print(arr)

#1 arr reshape
#reshape(rows,column)
print("Reshape : ")
print(arr.reshape(3,3))

#2 2D
arr_2d = np.array([[1,2,3],[4,5,6]])
print("2D array: ")
print(arr_2d)
print("Convert into 1D: ")
print(arr_2d.reshape(1,6))
print(arr_2d)
del arr_2d

#multi Diamension into single
# 1-> .reval() = original array get modified
# 2-> .flatten() = return a copy
arr_2d = np.array([[1,2,3],[4,5,6]])
print("Flatten array: ")
print(arr_2d.flatten())
print("original array: ")
print(arr_2d)
print("Ravel array: ")
print(arr_2d.ravel())
print(arr_2d)