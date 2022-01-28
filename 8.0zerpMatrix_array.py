import numpy as np

#การสร้าง  array 1 miti
# Zero_matrix array สมาขิกทั้งหมดเป็น 0 #ข้อมูลทั้งหมดจะมีค่าเป็น 0


#เเบบเก็บค่าลงในตัวแปร
num = np.zeros(10)
print(num)

# แบบระบุชนิดข้อมูล
number1 = np.zeros(1000000,dtype = "int")
number2 = np.zeros(10000,dtype = "float")
number3 = np.zeros(10000,dtype = "complex")
print(number1 )
print(number2)
print(number3)

# array 2 miti
num = np.zeros([4,10])
print("size = ",num.ndim)
print(num)

# array 3 miti
num1 = np.zeros((5,5))
print("size = ",num1.ndim)
print(num1)