"""
Sắp xếp danh sách số theo thứ tự tăng dần hoặc giảm dần
Viết chương trình yêu cầu người dùng nhập một danh sách các số và sắp xếp chúng 
theo thứ tự tăng dần hoặc giảm dần dựa trên sự lựa chọn của người dùng.
"""

so_list = input("Nhập các số, cách nhau bởi dấu phẩy: ").split(',')
so_list = [int(x) for x in so_list]

thu_tu = input("Bạn muốn sắp xếp theo thứ tự tăng dần hay giảm dần? (tăng/giảm): ")

if thu_tu.lower() == 'tăng':
    so_list.sort()
elif thu_tu.lower() == 'giảm':
    so_list.sort(reverse=True)
else:
    print("Lựa chọn không hợp lệ")

print("Danh sách sau khi sắp xếp:", so_list)
