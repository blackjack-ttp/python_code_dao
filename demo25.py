# Import các thư viên
import turtle
import colorsys

# Tốc độ vẽ nhanh nhất
turtle.speed(0)

# Màu nền
turtle.bgcolor("black")

# Số lượng cánh hoa
NUMBER_OF_PETALS = 16

# Số lượng gân trong mỗi cánh hoa
NUMBER_OF_PETAL_VEINS = 18

# Chỉ định màu sắc ban đầu (vào vòng lặp màu sắc sẽ thay đổi liên tục)
hue = 0

# Thực hiện vòng lập vẽ các cánh hoa
for i in range(NUMBER_OF_PETALS):
    # Thực hiện vòng lặp vẽ gân trong mỗi cánh hoa
    for j in range(NUMBER_OF_PETAL_VEINS):
        # Chuyển từ màu HSV sang màu RGB
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        
        # Chỉ định màu sắc để bắt đầu vẽ
        turtle.color(color)
        
        # Thay đổi màu sắc nhạt dần mỗi khi vẽ một gân cánh hoa
        hue += 0.005
        
        # Quay sangg phải 90 độ, vẽ một nữa gân cánh hoa
        turtle.right(90)
        radius = 150 - j * 6
        turtle.circle(radius, 90)
        
        # Quay chiều ngược lại để vẽ một nữa gân hoa còn lạii
        turtle.left(90)
        turtle.circle(150 - j * 6, 90)
        
        # Quay sang phải một gốc 180 độ để chuẩn bị vẽ cánh hoa kế tiếp
        turtle.right(180)
    
    # Vẽ đường công tịnh tiến đến cánh hoa kế tiếp
    turtle.circle(40, 24)
        