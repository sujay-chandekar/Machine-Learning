import numpy as np

arr = np.array([[1,2,3],
               [4,5,6]])

#number of diamensions

arr1= np.array([1,3,4,5])
print("Arr 1 diamension")
print(arr1.ndim)
print("Arr 2 diamension")
print(arr.ndim)

#chaning type 

arr  = arr.astype(float)
print(arr.dtype)
print(arr)
