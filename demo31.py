import random
import string
from guizero import App, Text, PushButton, Slider, CheckBox, TextBox

def tao_mat_khau_ngau_nhien():
    """Tạo mật khẩu ngẫu nhiên dựa trên các tùy chọn được chọn trong GUI."""
    do_dai = slider.value

    chu_thuong = string.ascii_lowercase
    chu_hoa = string.ascii_uppercase if checkbox_chu_hoa.value else ""
    so = string.digits if checkbox_so.value else ""
    ky_tu_dac_biet = string.punctuation if checkbox_ky_tu_dac_biet.value else ""

    tat_ca_ky_tu = chu_thuong + chu_hoa + so + ky_tu_dac_biet
    if not tat_ca_ky_tu:
        mat_khau.value = "Hãy chọn ít nhất một loại ký tự!"
        return

    mat_khau_duoc_tao = ''.join(random.choices(tat_ca_ky_tu, k=do_dai))
    mat_khau.value = mat_khau_duoc_tao

# Tạo giao diện chính
app = App(title="Trình tạo mật khẩu", width=800, height=250)

# Tiêu đề
Text(app, text="Tạo mật khẩu ngẫu nhiên", size=18, color="blue", align="top")

# Slider chọn độ dài
Text(app, text="Chọn độ dài mật khẩu:")
slider = Slider(app, start=4, end=32, width="fill")
slider.value = 12

# CheckBox để chọn các tùy chọn
checkbox_chu_hoa = CheckBox(app, text="Bao gồm chữ hoa", align="left")
checkbox_so = CheckBox(app, text="Bao gồm số", align="left")
checkbox_ky_tu_dac_biet = CheckBox(app, text="Bao gồm ký tự đặc biệt", align="left")

# Nút tạo mật khẩu
PushButton(app, text="Tạo mật khẩu", command=tao_mat_khau_ngau_nhien)

# Hiển thị mật khẩu đã tạo
Text(app, text="Mật khẩu của bạn:")
mat_khau = TextBox(app, width="fill", multiline=False, text="", enabled=False)

# Chạy ứng dụng
app.display()
