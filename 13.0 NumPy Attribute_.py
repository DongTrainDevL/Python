import numpy as np

# array 1 miti
arr = np.array(10)
print(arr)

arr1 = np.array([[1,2,3,4,5]])
print(arr1)

# chk size array 2 miti
print(arr1.ndim)

arr2 = np.array([[[10,20,30,40,50]]])
print(arr2)
# chk size array 3 miti
print(arr2.ndim)

# chk shape array 3 miti
print(arr1.shape)
print(arr2.shape)

# size บอกขนาด array
print(arr1.size)
print(arr2.size)

# itemsize อยากทราบ bye
print(arr1.itemsize)
print(arr2.itemsize)

# array data type
num = np.array([[1,2,3,4,5,6,7,8,9,10]],dtype = "int")
print(num)
print(num.itemsize)
print(num.shape)
print(num.ndim)

num1 = np.array([[[10,20,30,40,50]]],dtype = "complex")
print(num1.itemsize)
print(num1.shape)
print(num1.ndim)