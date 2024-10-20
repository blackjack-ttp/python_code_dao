"""
Quản lý chi tiêu cá nhân
Viết chương trình quản lý chi tiêu cá nhân, giúp theo dõi số tiền đã chi tiêu và các 
hạng mục chi tiêu (ăn uống, giải trí, mua sắm, v.v.).

Yêu cầu:

Cho phép người dùng nhập vào số tiền đã chi và danh mục chi tiêu.
Hiển thị tổng số tiền đã chi tiêu theo từng danh mục và tổng chi tiêu.
"""

chi_tieu = {}

while True:
    lua_chon = input("Bạn muốn làm gì? (thêm/xem tổng chi tiêu/thoát): ").lower()

    if lua_chon == "thêm":
        danh_muc = input("Nhập danh mục chi tiêu (ăn uống, mua sắm, giải trí, ...): ")
        so_tien = float(input("Nhập số tiền chi tiêu: "))
        chi_tieu[danh_muc] = chi_tieu.get(danh_muc, 0) + so_tien
        print(f"Đã thêm {so_tien} vào danh mục {danh_muc}.")
    
    elif lua_chon == "xem tổng chi tiêu":
        tong_chi_tieu = sum(chi_tieu.values())
        print("Tổng chi tiêu của bạn là:", tong_chi_tieu)
        for dm, tien in chi_tieu.items():
            print(f"Danh mục {dm}: {tien}")
    
    elif lua_chon == "thoát":
        break
    else:
        print("Lựa chọn không hợp lệ.")
