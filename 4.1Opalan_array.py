import numpy as np

#accesssibility to data in array 

num = np.array([20,30,40,50])
print("result = ",num[-1]+num[-2])
print("result = ",num[-4]+num[1])


# addsice ค่า 
num[-4] = 10 # ค่าใหม่ที่เพิ่มแทนที่ idex กำหนด
print(num)
