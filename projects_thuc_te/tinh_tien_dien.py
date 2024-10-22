"""
Tính tiền điện
Viết chương trình tính tiền điện theo bậc thang lũy tiến cho một hộ gia đình.

Yêu cầu:

Các bậc tính tiền điện như sau:
0-50 kWh: 1.678 đồng/kWh
51-100 kWh: 1.734 đồng/kWh
101-200 kWh: 2.014 đồng/kWh
201-300 kWh: 2.536 đồng/kWh
Trên 300 kWh: 2.927 đồng/kWh
Người dùng nhập vào số điện đã sử dụng trong tháng, và chương trình sẽ tính tổng số tiền phải trả.
"""

def tinh_tien_dien(so_dien):
    tien_dien = 0
    if so_dien <= 50:
        tien_dien = so_dien * 1678
    elif so_dien <= 100:
        tien_dien = 50 * 1678 + (so_dien - 50) * 1734
    elif so_dien <= 200:
        tien_dien = 50 * 1678 + 50 * 1734 + (so_dien - 100) * 2014
    elif so_dien <= 300:
        tien_dien = 50 * 1678 + 50 * 1734 + 100 * 2014 + (so_dien - 200) * 2536
    else:
        tien_dien = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + (so_dien - 300) * 2927
    return tien_dien

so_dien = int(input("Nhập số điện tiêu thụ trong tháng (kWh): "))
tien = tinh_tien_dien(so_dien)
print(f"Số tiền điện phải trả là: {tien} đồng")
