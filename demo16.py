"""Sử dụng Khối try-except-else

Xử lý lỗi trong Python có thể được thực hiện dễ dàng bằng cách sử dụng khối try / except.

Thêm một câu lệnh else vào khối này rất hữu ích. Nó sẽ chạy khi không có ngoại lệ xảy ra trong khối try.

Nếu bạn cần chạy một cái gì đó không phân biệt ngoại lệ, hãy sử dụng finaly."""

a, b = 1, 0

try:
    print(a/b)
    # Ngoại lệ xảy ra khi b == 0
except ZeroDivisionError:
    print("Chia cho số 0")
else:
    print("Không có ngoại lệ xảy ra")
finally:
    print("Luôn luôn chạy lệnh này!")
