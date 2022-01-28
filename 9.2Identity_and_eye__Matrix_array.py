import numpy as np


# Identity Matrix เอกลักษณ์
# เส้นทะแยงมุมมีค่าเป็น 1 ที่เหลือมีค่าเป็น 0
num = np.identity(10)
print(num)

# data type
num1 = np.identity(20,dtype = "int")
print(num1)

# function eye ความสามารถมีต่าง conlumn ได้ เช่น 3,4 

num2 = np.eye(4,5,dtype = "int")
print(num2)

# k = 0 #ความหมายคือ: เป็นการย้ายตำแหน่งของเส้นทะแยงมุมให้เคลื่อนที่ ขึ้นลง
# ขึ้นจะเป็นค่าบวก
# ลงไปค่าลบ
num3 = np.eye(20,20,k = 19,dtype = "int")
print(num3)