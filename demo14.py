from art import logo

# Bảng chữ cái với các ký tự lặp lại để dễ dàng xử lý dịch chuyển
bang_chu_cai = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ma_hoa_Caesar(vao_text, luong_dich_chuyen, huong_ma_hoa):
    ket_qua_text = ""
    if huong_ma_hoa == "giai_ma":
        luong_dich_chuyen *= -1
    for ky_tu in vao_text:
        # Kiểm tra xem ký tự có nằm trong bảng chữ cái không
        if ky_tu in bang_chu_cai:
            vi_tri = bang_chu_cai.index(ky_tu)
            vi_tri_moi = vi_tri + luong_dich_chuyen
            ket_qua_text += bang_chu_cai[vi_tri_moi]
        else:
            # Nếu không, giữ nguyên các ký tự không phải chữ cái (như số, ký hiệu, khoảng trắng)
            ket_qua_text += ky_tu
    print(f"Kết quả {huong_ma_hoa} là: {ket_qua_text}")


# In logo từ module art khi chương trình bắt đầu
print(logo)

# Vòng lặp cho phép người dùng chọn lặp lại chương trình
ket_thuc = False
while not ket_thuc:

    huong = input("Nhập 'ma_hoa' để mã hóa, nhập 'giai_ma' để giải mã:\n")
    van_ban = input("Nhập tin nhắn của bạn:\n").lower()
    dich_chuyen = int(input("Nhập số lần dịch chuyển:\n"))

    # Xử lý trường hợp người dùng nhập số lớn hơn số ký tự trong bảng chữ cái
    dich_chuyen = dich_chuyen % 26

    ma_hoa_Caesar(vao_text=van_ban,
                  luong_dich_chuyen=dich_chuyen, huong_ma_hoa=huong)

    # Hỏi người dùng có muốn lặp lại chương trình không
    lam_lai = input(
        "Nhập 'co' nếu bạn muốn tiếp tục. Nếu không, nhập 'khong'.\n")
    if lam_lai == "khong":
        ket_thuc = True
        print("Tạm biệt!")
