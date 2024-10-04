MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}


def bao_cao():
    print(f"Nước: {resources['water']}ml")
    print(f"Sữa: {resources['milk']}ml")
    print(f"Cà phê: {resources['coffee']}g")
    print(f"Tiền: ${money['value']}")


def kiem_tra_nguyen_lieu(lua_chon_ca_phe):
    """Kiểm tra nếu nguyên liệu đủ cho món uống"""
    du_nguyen_lieu = True
    if MENU[lua_chon_ca_phe]['ingredients']['water'] > resources['water']:
        print(f"Không đủ nước cho món {lua_chon_ca_phe}.")
        du_nguyen_lieu = False
    if MENU[lua_chon_ca_phe]['ingredients']['coffee'] > resources['coffee']:
        print(f"Không đủ cà phê cho món {lua_chon_ca_phe}.")
        du_nguyen_lieu = False
    if lua_chon_ca_phe != 'espresso' and MENU[lua_chon_ca_phe]['ingredients']['milk'] > resources['milk']:
        print(f"Không đủ sữa cho món {lua_chon_ca_phe}.")
        du_nguyen_lieu = False
    return du_nguyen_lieu


def xu_ly_dong_xu(quarters, dimes, nickles, pennies):
    """Xử lý đồng xu và trả về tổng tiền"""
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01


def tru_nguyen_lieu(lua_chon_ca_phe):
    """Trừ nguyên liệu sau khi pha chế"""
    resources['water'] -= MENU[lua_chon_ca_phe]['ingredients']['water']
    resources['coffee'] -= MENU[lua_chon_ca_phe]['ingredients']['coffee']
    if lua_chon_ca_phe != 'espresso':
        resources['milk'] -= MENU[lua_chon_ca_phe]['ingredients']['milk']


def may_pha_ca_phe():
    bat_may = True
    while bat_may:
        lua_chon = input(
            "Bạn muốn uống gì? Nhập 'espresso', 'latte', 'cappuccino': ")
        if lua_chon == 'bao cao':
            bao_cao()
        elif lua_chon == 'tat may':
            print("Tắt máy.")
            bat_may = False
        elif lua_chon in MENU and kiem_tra_nguyen_lieu(lua_chon):
            print("Xin hãy cho vào tiền xu.")
            quarters = int(input("Có bao nhiêu quarters?: "))
            dimes = int(input("Có bao nhiêu dimes?: "))
            nickles = int(input("Có bao nhiêu nickles?: "))
            pennies = int(input("Có bao nhiêu pennies?: "))
            tong_tien = xu_ly_dong_xu(quarters, dimes, nickles, pennies)
            gia_ca_phe = MENU[lua_chon]['cost']

            if tong_tien >= gia_ca_phe:
                tru_nguyen_lieu(lua_chon)
                money['value'] += gia_ca_phe
                tien_thua = round(tong_tien - gia_ca_phe, 2)
                if tien_thua > 0:
                    print(f"Đây là ${tien_thua} tiền thừa.")
                print(f"Đây là ly {lua_chon} ☕ của bạn. Chúc bạn ngon miệng!")
            else:
                print(f"Không đủ tiền, ${tong_tien} được hoàn lại.")
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


may_pha_ca_phe()
