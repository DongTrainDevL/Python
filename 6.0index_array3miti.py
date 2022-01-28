import numpy as np


#conseap [depth] [row] [column] 
# ถ้าเป็น array 3 miti จะแบ่งเป็นชุดข้อมูล โดยแต่ละจะแบ่งเป็นชุดข้อมูลย่อย เริ่มจาก 0
num = np.array([[[1,2,3,4],[5,6,7,8]],[[10,20,30,40],[100,1000,10000,100000]]])
print(num.ndim)
print("result search index =",num[1][1][-3])
print(num[0][0][-1]+num[1][0][-4])
print(num[0][1][-4]**num[1][1][-3])