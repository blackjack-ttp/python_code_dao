# Lib
from turtle import *

# Tạo danh sách màu sắc
colors = ["red", "purple", "blue", "green", "yellow", "orange"]
# Khởi tạo vòng lập 
for x in range(360):
    # Thay đổi màu sắc của bút vẽ
    pencolor(colors[x % 6])
    # Thay đổi độ dày của nét vẽ
    width(x / 100 + 1)
    # Di chuyển con trỏ về phía trước
    forward(x)
    # Xoay con trỏ về bên trái một góc 90 độ
    left(59)
