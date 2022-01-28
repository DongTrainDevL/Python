import numpy as np

# สำหรับสำรับ port graf เพราะมันจะมีการเว้นช่วงเท่าๆกัน ตอนที่ทำการกำหนดสมาชิกขึ้นมา
# function linspase
# conspae = start = stop
# คือการกำหนดช่วงของตัวเลข เช่น 1 กว่าจะถึงตัวเลขปลายทางค่ามีค่าเท่าไร่

num = np.linspace(1,10)
print(num)

# กำหนดว่าจะเท่าไร่ เช้น 5
num1 = np.linspace(1,20,5)
print(num1)

# endpoint คือไม่เอาตัวสุดท้ายกำหนดให้เป็น False

num2 = np.linspace(1,5,endpoint=False)
print(num2)