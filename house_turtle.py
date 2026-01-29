import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("House using Turtle")

t = turtle.Turtle()
t.speed(3)
t.width(3)

# Draw square (house body)
t.penup()
t.goto(-100, -100)
t.pendown()

t.color("black", "lightyellow")
t.begin_fill()
for _ in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

# Draw roof (triangle)
t.color("black", "brown")
t.begin_fill()
t.goto(-100, 100)
t.goto(0, 200)
t.goto(100, 100)
t.goto(-100, 100)
t.end_fill()

# Draw door
t.penup()
t.goto(-30, -100)
t.pendown()

t.color("black", "saddlebrown")
t.begin_fill()
t.forward(60)
t.left(90)
t.forward(100)
t.left(90)
t.forward(60)
t.left(90)
t.forward(100)
t.end_fill()

# Draw window (left)
t.penup()
t.goto(-80, 20)
t.pendown()

t.color("black", "lightblue")
t.begin_fill()
for _ in range(4):
    t.forward(40)
    t.left(90)
t.end_fill()

# Draw window (right)
t.penup()
t.goto(40, 20)
t.pendown()

t.begin_fill()
for _ in range(4):
    t.forward(40)
    t.left(90)
t.end_fill()

t.hideturtle()
turtle.done()
