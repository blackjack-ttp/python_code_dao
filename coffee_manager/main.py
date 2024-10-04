from menu import ThucDon, ThucDonMon
from coffee_maker import MayPhaCaPhe
from money_machine import MayTien


def main():
    # Danh sách đồ uống
    espresso = ThucDonMon("espresso", 50, 0, 18, 1.5)
    latte = ThucDonMon("latte", 200, 150, 24, 2.5)
    cappuccino = ThucDonMon("cappuccino", 250, 100, 24, 3.0)

    # Tạo menu
    menu = ThucDon()

    # Tạo máy pha cà phê
    coffee_maker = MayPhaCaPhe()

    # Tạo máy quản lý tiền
    money_machine = MayTien()

    on = True
    while on:
        choice = input(
            f"Bạn muốn gì? Chọn giữa espresso, latte hoặc cappuccino: ")
        if choice == 'off':
            print("Chúc bạn một ngày tốt lành!")
            on = False
        elif choice == 'report':
            coffee_maker.bao_cao()
            money_machine.bao_cao()
        else:
            coffee_choice = menu.tim_mon(choice)
            if coffee_choice is not None:  # Kiểm tra xem đồ uống có trong menu không
                if coffee_maker.du_nguyen_lieu(coffee_choice) and money_machine.thuc_hien_thanh_toan(coffee_choice.cost):
                    coffee_maker.pha_ca_phe(coffee_choice)
            else:
                print("Xin lỗi, đồ uống bạn yêu cầu không có sẵn.")


if __name__ == "__main__":
    main()
