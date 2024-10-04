class ThucDonMon:
    """Mô hình mỗi món trong thực đơn."""

    def __init__(self, ten, nuoc, sua, ca_phe, gia):
        self.ten = ten
        self.gia = gia
        self.nguyen_lieu = {
            "nuoc": nuoc,
            "sua": sua,
            "ca_phe": ca_phe
        }


class ThucDon:
    """Mô hình thực đơn với các món uống."""

    def __init__(self):
        self.thuc_don = [
            ThucDonMon(ten="latte", nuoc=200, sua=150, ca_phe=24, gia=2.5),
            ThucDonMon(ten="espresso", nuoc=50, sua=0, ca_phe=18, gia=1.5),
            ThucDonMon(ten="cappuccino", nuoc=250, sua=50, ca_phe=24, gia=3),
        ]

    def lay_mon(self):
        """Trả về tên của tất cả các món có trong thực đơn"""
        lua_chon = ""
        for mon in self.thuc_don:
            lua_chon += f"{mon.ten}/"
        return lua_chon

    def tim_mon(self, ten_mon):
        """Tìm món uống trong thực đơn theo tên. Trả về món nếu có, nếu không trả về None."""
        for mon in self.thuc_don:
            if mon.ten == ten_mon:
                return mon
        print("Xin lỗi, món này không có sẵn.")
