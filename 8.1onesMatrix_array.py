import numpy as np


# method ones สมาชิกทุกตัวใน array จะเป็น 1 ทั้งหมด

# array 1 miti
num = np.ones(10)
print(num)

# data type
arr = np.ones(20,dtype = "int")
print(arr)

# array 2 miti
#ถ้า matrix แบบ จรัตุรัต # จะมีด้านเท่ากัน
num1 = np.ones([5,5])
print(num1.ndim)
print(num1)

