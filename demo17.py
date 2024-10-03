"""Tính thời gian thực hiện để thực thi một đoạn code trong Python

Đoạn code sau sử dụng thư viện time để dễ dàng giúp chúng ta tính thời 
gian thực để thực thi một đoạn code trong Python."""
# import thư viện time
import time

# Kiểm tra thời gian bắt đầu
start_time = time.time()

# Code cần kiểm tra
a, b = 1, 2
c = a + b

# Kiểm tra thời gian kết thúc
end_time = time.time()

# Tính thời gian chênh lệch
time_taken_in_micro = (end_time - start_time)*(10**6)

# In kết quả
print(time_taken_in_micro)
