import numpy as np
# +,-,*,/,**,//,%

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print(arr+2,end="\n\n")
print(arr-2,end="\n\n")
print(arr*2,end="\n\n")
print(arr/2,end="\n\n")
print(arr**2,end="\n\n")
print(arr//2,end="\n\n")
print(arr%2,end="\n\n")

#aggregation function

print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
print(np.std(arr)) #standard deviation
print(np.var(arr))