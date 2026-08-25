# PART 1: Importing the turtle module
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Mandela")


# PART 2: Create a turtle pen
board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()

# PART 3: Outer color circle (movement + loops + color)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
for i in range(80):
    board.color(colors[i % len(colors)])
    board.width(2)
    board.forward(i * 2)
    board.right(91)

# PART 4: Pen control: Move to center and draw a filled star

board.penup()
board.goto(0, -60)
board.setheading(90)
board.pendown()
board.color("gold", "yellow")
board.begin_fill()
for i in range(5):
    board.forward(130)
    board.right(144)
board.end_fill()

# PART 5: Inner Petal Ring (Nested loop + Fill)

board.penup()
board.goto(0, 0)
board.pendown()
petal_colors = ["cyan", "orange", "lime", "deeppink", "blue", "indigo", "violet"]
for i in range(36):
    board.color(petal_colors[i % len(petal_colors)], petal_colors[(i + 2) % len(petal_colors)])
    board.begin_fill()
    for j in range(4):
        board.forward(55)
        board.right(90)
    board.end_fill()
    board.right(10)

turtle.done()