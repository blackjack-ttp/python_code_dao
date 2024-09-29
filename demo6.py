"""
Tìm số lớn nhất trong hai số a và b mà không dùm if, else và các phép so sánh >,<,=
"""

a = int(input("Enter :a: "))
b = int(input("Enter :a: "))
lon = ((a + b) + abs(a - b))/2
print(lon)
