class MayTien:
    CURRENCY = "₫"

    GIATRI_XU = {
        "quy": 0.25,
        "dime": 0.10,
        "nickel": 0.05,
        "xu": 0.01
    }

    def __init__(self):
        self.loi_nhuan = 0
        self.tien_nhan = 0

    def bao_cao(self):
        """In ra lợi nhuận hiện tại"""
        print(f"Tiền: {self.CURRENCY}{self.loi_nhuan}")

    def xu_ly_xu(self):
        """Trả về tổng tiền được tính từ số xu được đưa vào."""
        print("Xin vui lòng bỏ xu vào.")
        for xu in self.GIATRI_XU:
            self.tien_nhan += int(
                input(f"Có bao nhiêu {xu}?: ")) * self.GIATRI_XU[xu]
        return self.tien_nhan

    def thuc_hien_thanh_toan(self, gia):
        """Trả về True khi thanh toán được chấp nhận, hoặc False nếu không đủ tiền."""
        self.xu_ly_xu()
        if self.tien_nhan >= gia:
            tien_thua = round(self.tien_nhan - gia, 2)
            print(f"Đây là {self.CURRENCY}{tien_thua} tiền thối.")
            self.loi_nhuan += gia
            self.tien_nhan = 0
            return True
        else:
            print("Xin lỗi, không đủ tiền. Tiền đã được hoàn trả.")
            self.tien_nhan = 0
            return False
