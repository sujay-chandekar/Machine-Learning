import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
#positive slicing
print("Indexing :")
print(arr[2:7:])

#-ve indexing
print("Negative Indexing") 
print(arr[-1:-5:-1])

#2D
arr_2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Slicing in 2D")
print(arr_2D[0:1:1])

#fancy Indexing
#arr[[index1,index2,.....]]
print("Fancy Indexing")
print(arr[[0,3,6]])

#boolean masking

print("Boolean Masking : ")
print(arr[arr<4])