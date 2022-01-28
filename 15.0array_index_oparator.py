import numpy as np


x = np.arange(1,10)
print(x)

#ใช้ดึงสมาชิกใน array x โดยการสร้าง array เพื่อที่จะดึงสมาชิก
# ระบุสามชิกหมายเลข index ของ array
index = np.array([-1,-2,-3])
print(x[index])

arr1 = np.array([[1,2,3,4],[10,20,30,40],[50,60,70,80]])
print(arr1[1,0],[0])
print(arr1[2,0])