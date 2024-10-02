import random

# Danh sách ký tự, số, và ký tự đặc biệt
chu_cai = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
so = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ky_hieu = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Chào mừng đến với chương trình tạo mật khẩu PyPassword!")
so_chu_cai = (input("Bạn muốn có bao nhiêu chữ cái trong mật khẩu?\n"))
so_ky_hieu = (input("Bạn muốn có bao nhiêu ký hiệu?\n"))
so_so = (input("Bạn muốn có bao nhiêu số?\n"))

# Kiểm tra xem người dùng có nhập đúng số hay không
if not so_chu_cai.isdigit() or not so_ky_hieu.isdigit() or not so_so.isdigit():
    print("Giá trị không hợp lệ, vui lòng nhập số.")
else:
    mat_khau = []

    chu_cai_ngau_nhien = random.randint(0, 51)
    for i in range(0, int(so_chu_cai)):
        chu_cai_ngau_nhien = random.randint(0, 51)
        mat_khau.append(chu_cai[chu_cai_ngau_nhien])

    so_ngau_nhien = random.randint(0, 9)
    for i in range(0, int(so_so)):
        so_ngau_nhien = random.randint(0, 9)
        mat_khau.append(so[so_ngau_nhien])

    ky_hieu_ngau_nhien = random.randint(0, 8)
    for i in range(0, int(so_ky_hieu)):
        ky_hieu_ngau_nhien = random.randint(0, 8)
        mat_khau.append(ky_hieu[ky_hieu_ngau_nhien])

    # Xáo trộn mật khẩu
    random.shuffle(mat_khau)
    print(f"Mật khẩu của bạn là: {''.join(mat_khau)}")

    # Đánh giá độ mạnh của mật khẩu
    if len(mat_khau) <= 6:
        print(
            "Mật khẩu của bạn yếu, hãy thử sử dụng ít nhất 8 ký tự để có mật khẩu mạnh hơn.")
    elif len(mat_khau) == 7:
        print("Mật khẩu của bạn ở mức trung bình, hãy thử sử dụng ít nhất 8 ký tự để có mật khẩu mạnh hơn.")
    else:
        print("Mật khẩu của bạn mạnh.")
