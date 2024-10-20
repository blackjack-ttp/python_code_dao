"""
Quản lý kho hàng

Viết một chương trình để quản lý kho hàng. Người dùng có thể thêm sản phẩm mới, cập nhật số lượng, và kiểm tra hàng tồn kho.

Yêu cầu:

Cho phép người dùng nhập tên sản phẩm và số lượng.
Khi một sản phẩm đã tồn tại, chương trình phải cập nhật số lượng thay vì tạo sản phẩm mới.
Người dùng có thể kiểm tra số lượng sản phẩm trong kho.
"""

kho_hang = {}

while True:
    lua_chon = input("Bạn muốn làm gì? (thêm/cập nhật/kiểm tra/thoát): ").lower()

    if lua_chon == "thêm" or lua_chon == "cập nhật":
        ten_sp = input("Nhập tên sản phẩm: ")
        so_luong = int(input("Nhập số lượng: "))
        kho_hang[ten_sp] = kho_hang.get(ten_sp, 0) + so_luong
        print(f"{ten_sp} đã được cập nhật. Số lượng hiện tại: {kho_hang[ten_sp]}")
    
    elif lua_chon == "kiểm tra":
        ten_sp = input("Nhập tên sản phẩm muốn kiểm tra: ")
        if ten_sp in kho_hang:
            print(f"Số lượng của {ten_sp} là: {kho_hang[ten_sp]}")
        else:
            print(f"{ten_sp} không có trong kho.")
    
    elif lua_chon == "thoát":
        break
    else:
        print("Lựa chọn không hợp lệ.")
