"""
Vẽ Lá Cờ Việt Nam Bằng Python Turtle 
"""
import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.bgcolor("white")
star = turtle.Turtle()
star.speed(5)

# Hàm vẽ ngôi sao vàng


def draw_star(size):
    star.color("yellow")
    star.begin_fill()
    for _ in range(5):
        star.forward(size)
        star.right(144)
        star.forward(size)
        star.left(72)
    star.end_fill()

# Hàm vẽ hình chữ nhật


def draw_rectangle(width, height):
    star.color("red")
    star.penup()
    star.goto(-width/2, height/2)  # Đặt vị trí ban đầu vẽ hình chữ nhật
    star.pendown()
    star.begin_fill()

    for _ in range(2):
        star.forward(width)  # Chiều dài cờ
        star.right(90)
        star.forward(height)  # Chiều rộng cờ
        star.right(90)
    star.end_fill()


# Kích thước cờ
rectange_width = 600
rectange_height = 400

# Vẽ cờ
draw_rectangle(rectange_width, rectange_height)

# Đặt vị trí vẽ ngôi sao giữa cờ
star.penup()
star.goto(25, 20)  # Điều chỉnh vị trí sao cho cân đối
star.pendown()

# Vẽ ngôi sao vàng
draw_star(100)

# Ẩn con rùa sau khi vẽ xong
star.hideturtle()

# Kết thúc chương trình
turtle.done()
