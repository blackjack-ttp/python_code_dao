from turtle import *  # Nhập tất cả các hàm từ thư viện turtle để vẽ hình
import random  # Nhập thư viện random để tạo ra các giá trị ngẫu nhiên

for n in range(60):  # Vòng lặp chạy 60 lần để vẽ 60 cụm vòng tròn
    penup()  # Nâng bút lên để di chuyển mà không vẽ
    goto(
        random.randint(-400, 400), random.randint(-400, 400)
    )  # Di chuyển tới vị trí ngẫu nhiên trên màn hình
    pendown()  # Hạ bút xuống để bắt đầu vẽ

    # Tạo các giá trị ngẫu nhiên cho thành phần màu đỏ, xanh lá và xanh dương
    red_amount = random.randint(0, 30) / 100.0  # Màu đỏ ngẫu nhiên từ 0.0 đến 0.3
    blue_amount = (
        random.randint(50, 100) / 100.0
    )  # Màu xanh dương ngẫu nhiên từ 0.5 đến 1.0
    green_amount = (
        random.randint(0, 30) / 100.0
    )  # Màu xanh lá ngẫu nhiên từ 0.0 đến 0.3
    pencolor(
        (red_amount, green_amount, blue_amount)
    )  # Đặt màu bút vẽ dựa trên các giá trị RGB

    circle_size = random.randint(
        10, 40
    )  # Kích thước vòng tròn ngẫu nhiên từ 10 đến 40 pixel
    pensize(random.randint(1, 5))  # Độ dày bút ngẫu nhiên từ 1 đến 5 pixel

    for i in range(6):  # Lặp 6 lần để vẽ 6 vòng tròn
        circle(circle_size)  # Vẽ một vòng tròn với kích thước đã chọn ngẫu nhiên
        left(60)  # Xoay trái 60 độ sau mỗi lần vẽ, tạo thành hình lục giác
