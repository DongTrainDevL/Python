import numpy as np
# array 0 มิติ
arr = np.array(1)
print(arr)

arr1 = np.array(2)
arr.ndim
print(arr)

# array 1 มิติ
# type list
lst = [1,2,3,4,5]
b = np.array(lst)
print("size",b.ndim)
print(b)

#tuple to array
tup = (1,3,4,5,5,6,6,7,7,7,8,8,)
c = np.array(tup)
print("size",c)