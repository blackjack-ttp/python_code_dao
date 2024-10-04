class MayPhaCaPhe:
    """Mô hình máy pha cà phê"""

    def __init__(self):
        self.nguyen_lieu = {
            "nuoc": 300,
            "sua": 200,
            "ca_phe": 100,
        }

    def bao_cao(self):
        """In báo cáo về tất cả các nguyên liệu."""
        print(f"Nước: {self.nguyen_lieu['nuoc']}ml")
        print(f"Sữa: {self.nguyen_lieu['sua']}ml")
        print(f"Cà phê: {self.nguyen_lieu['ca_phe']}g")

    def du_nguyen_lieu(self, mon_uong):
        """Trả về True nếu có thể pha chế món uống, False nếu nguyên liệu không đủ."""
        co_the_pha = True
        for item in mon_uong.nguyen_lieu:
            if mon_uong.nguyen_lieu[item] > self.nguyen_lieu[item]:
                print(f"Xin lỗi, không đủ {item}.")
                co_the_pha = False
        return co_the_pha

    def pha_ca_phe(self, don_hang):
        """Trừ nguyên liệu cần thiết từ kho nguyên liệu."""
        for item in don_hang.nguyen_lieu:
            self.nguyen_lieu[item] -= don_hang.nguyen_lieu[item]
        print(f"Đây là ly {don_hang.ten} ☕️ của bạn. Thưởng thức nhé!")
