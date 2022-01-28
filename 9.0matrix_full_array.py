import numpy as np

# method full คือค่าคงที่ 
# consape ##1ตัวแรก = column, 2ตัวที่2 = ค่าคงที่
num = np.full(20,10)
print(num)

# array 2 miti # ตัวข้างหลังคือค่าคง
num1 = np.full([5,5],10)
print(num1)

num1 = np.full([3,3],5.5)
print(num1)