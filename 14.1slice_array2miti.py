import numpy as np

# array 2 miti
# ต้องระบุ column ด้วย
# conspe = [row][column]
arr = np.array([[1,2,3,4,5],[10,20,30,40,50]])
#print(arr.ndim)

# 1
print(arr[:,:])

#2 start :,sotop:step

print(arr[1:,0:])

#3 เริ่มจากแถวที่กำหนดเป็นต้นไป เช่น [1:,2:]
# จะได้ค่าทีี่เริ่มจาก row1 column ที่ 2 ทั้งหมด
arr1 = np.array([[1,2,3,4,5,6,7,8,9,10],[106,20,30,40,50,0,70,80,90,100]])
print(arr1[0:,2:-1])

#4 อยากได้ตัวเลขเฉพาะใน column ท้งหมด
print(arr1[:,-3:])

#5 อยากได้ตัวเลขเฉพาะแถว
print(arr1[0:,:])
#6 ระบุจุดท้าย
print(arr1[:,-1:])
# 7 [start][stop][start][stop] #[:]เอาทุกแถว
# 50 onlyone
print(arr1[0:1,0:5])
arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(arr2[2::5])


