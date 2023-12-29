import turtle

def draw_petals(t, radius, angle, petals):
    for _ in range(petals):
        t.circle(radius, angle)
        t.left(180 - angle)
        t.circle(radius, angle)
        t.left(180 - (360 / petals))

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")

    # Создаем черепаху для рисования
    flower = turtle.Turtle()
    flower.shape("turtle")
    flower.speed(7)
    flower.color("red")

    # Рисуем цветок
    flower.penup()
    flower.goto(0, -200)
    flower.pendown()
    draw_petals(flower, 100, 60, 10)  # Рисуем лепестки

    # Рисуем стебель
    flower.color("green")
    flower.right(90)
    flower.forward(300)

    # Закончить рисование
    window.exitonclick()

draw_flower()
