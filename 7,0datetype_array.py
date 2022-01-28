import numpy as np

#data type array
#1. Integer
#2. Folat
#3. String
#4. Boolean
#5. complex
#6. Object

# array 1 miti1 
num = np.array([1,2,3,4,5],dtype = "int")
print(num.dtype)
num = np.array([10,20,30,40,50],dtype = "float")
print(num.dtype)

# array 2 miti
num = np.array([[1,2,3,4,5,6,7,8,9,10]],dtype = "complex")
print(num.ndim)
print(num.dtype)
# array 3 miti
arr = np.array([[[300,400,500,600,1000]]],dtype = "int");
print(arr.ndim)
print(arr.dtype)
#####
arry1 = np.array([[[10,20,30,40],[50,60,70,80,90]]])
print(arry1.ndim)
print(arry1.shape)
print(arry1.size)