import turtle
import random

# Tạo cửa sổ đồ họa
window = turtle.Screen()
window.title("Trò chơi Đua rùa")
window.bgcolor("white")

# Tạo đường đua
pen = turtle.Turtle()
pen.penup()
pen.goto(-200, 200)
pen.speed(0)
pen.pensize(3)

for _ in range(10):
    pen.write("|", align="center", font=("Courier", 24, "normal"))
    pen.right(90)
    pen.forward(20)
    pen.pendown()
    pen.forward(400)
    pen.penup()
    pen.backward(420)
    pen.left(90)
    pen.forward(50)

# Tạo rùa
colors = ["red", "blue", "green", "orange"]
racers = []

for i in range(4):
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.color(colors[i])
    racer.penup()
    racer.goto(-220, 170 - i * 50)
    racer.pendown()
    racers.append(racer)

# Bắt đầu đua
while True:
    for racer in racers:
        distance = random.randint(1, 10)
        racer.forward(distance)

        if racer.position()[0] >= 200:
            winner = colors[racers.index(racer)]
            print("Người chơi", winner, "chiến thắng!")
            break

    if racer.position()[0] >= 200:
        break

# Đóng cửa sổ đồ họa khi người dùng nhấn Enter
input("Nhấn Enter để đóng cửa sổ...")
window.bye()
