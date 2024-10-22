"""
Tìm kiếm chuyến bay rẻ nhất
Viết chương trình tìm chuyến bay rẻ nhất từ một danh sách các chuyến bay. Người dùng sẽ nhập vào điểm xuất phát và điểm đến, chương trình sẽ tìm chuyến bay có giá rẻ nhất.

Yêu cầu:

Người dùng nhập điểm xuất phát và điểm đến.
Chương trình tìm trong danh sách các chuyến bay và trả về chuyến có giá thấp nhất.    
"""

chuyen_bay = [
    {"xuat_phat": "Hanoi", "den": "Danang", "gia": 1200000},
    {"xuat_phat": "Hanoi", "den": "Hochiminh", "gia": 2000000},
    {"xuat_phat": "Danang", "den": "Hochiminh", "gia": 1500000},
    {"xuat_phat": "Hanoi", "den": "Danang", "gia": 1000000},
    {"xuat_phat": "Danang", "den": "Hanoi", "gia": 900000},
]

xuat_phat = input("Nhập điểm xuất phát: ")
den = input("Nhập điểm đến: ")

chuyen_bay_re_nhat = None
for chuyen in chuyen_bay:
    if chuyen["xuat_phat"] == xuat_phat and chuyen["den"] == den:
        if chuyen_bay_re_nhat is None or chuyen["gia"] < chuyen_bay_re_nhat["gia"]:
            chuyen_bay_re_nhat = chuyen

if chuyen_bay_re_nhat:
    print(f"Chuyến bay rẻ nhất từ {xuat_phat} đến {den} có giá: {chuyen_bay_re_nhat['gia']} VND")
else:
    print(f"Không tìm thấy chuyến bay từ {xuat_phat} đến {den}.")
