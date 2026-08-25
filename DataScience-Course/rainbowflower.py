import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rainbow Flower")

flower = turtle.Turtle()
flower.speed("fastest")
flower.hideturtle()

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
for i in range(36):
    flower.color(colors[i % len(colors)])
    for j in range(2):
        flower.circle(80, 60)
        flower.left(120)
    flower.left(10)

flower.penup()
flower.goto(0, -20)
flower.pendown()
flower.color("gold")
flower.begin_fill()
flower.circle(20)
flower.end_fill()

turtle.done()