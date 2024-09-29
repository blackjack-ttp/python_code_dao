"""
Xây dựng chương trình rút thăm trúng thưởng với các chức năng:
- Thêm một số điện thoại số vào thùng phiếu dự thưởng
- Xóa một số điện thoại từ thùng phiếu dự thưởng
- Quay số ngẫu nhiên lấy ra một số điện thoại trúng thưởng
"""
# Khai báo thư viên
import random

# Khai báo set
thungPhieu = {}

# Khởi tại hàm nhập thông tin


def input_data(data_type, message):
    while True:
        try:
            # Nhập thông tin và chuyển đổi sang kiểu dữ liệu yêu cầu
            user_input = data_type(input(message))
            return user_input
        except ValueError:
            # Nếu nhập sai kiểu dữ liệu, thông báo lỗi và yêu cầu nhập lại
            print(f"\033[91mVui lòng nhập dữ liệu kiểu {
                  data_type.__name__} hợp lệ.\033[0m")


# Khởi tạo hàm thêm số điện thoại vào thùng phiếu
def add_phone_number():
    while True:
        phone_number = input_data(
            int, "Nhập số điện thoại dự thưởng (10 số): ")
        # Kiểm tra độ dài số điện thoại
        if len(str(phone_number)) == 9:
            thungPhieu[phone_number] = True
            print("\n---------------------------------")
            print("\n\033[92mĐã thêm thành công!\033[0m")
            break
        else:
            print(
                "\033[91mSố điện thoại phải có đúng 10 chữ số. Vui lòng nhập lại.\033[0m")


# Khởi tạo hàm xóa số điện thoại khỏi thùng phiếu
def remove_phone_number():
    while True:
        phone_number = input_data(int, "Nhập số điện thoại cần xóa: ")
        # Kiểm tra độ dài số điện thoại
        if len(str(phone_number)) == 9:
            if phone_number in thungPhieu:
                del thungPhieu[phone_number]
                print("\n\033[92mĐã xóa thành công!\033[0m")
            else:
                print(f"\nSố điện thoại {
                    phone_number} không tồn tại trong thùng phiếu.")
        else:
            print(
                "\033[91mSố điện thoại phải có đúng 10 chữ số. Vui lòng nhập lại.\033[0m")


# Khởi tạo hàm quay số ngẫu nhiên lấy ra số điện thoại
def random_phone_number():
    if thungPhieu:
        phone_number = random.choice(list(thungPhieu.keys()))
        print("---------------------------------")
        print("\nSố trúng thưởng\n")
        print(f"Số điện thoại trúng thưởng ngẫu nhi\033[92m0{
              phone_number}\033[0m")
        print("---------------------------------")
    else:
        print("\n\033[91mThùng phiếu đang trống.\033[0m")

# Khởi tạo hàm main chính chạy chương trình


def menu():
    while True:
        print("""
              CHƯƠNG TRÌNH QUAY SỐ TRÙNG THƯỞNG\n
              --------------MENU---------------
              Vui lòng chọn chức năng:\n
              \t\t1. Thêm số điện thoại\n
              \t\t2. Xóa số điện thoại\n
              \t\t3. Quay số ngẫu nhiên lấy ra số điện thoại\n
              \t\t4. Thoát\n
              """)
        choice = input("Chọn chức năng (1-4): ")
        print("---------------------------------\n")

        if choice == "1":
            add_phone_number()
        elif choice == "2":
            remove_phone_number()
        elif choice == "3":
            random_phone_number()
        elif choice == "4":
            print("\nThoát chương trình.")
            break


if __name__ == "__main__":
    menu()
