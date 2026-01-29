import turtle

t = turtle.Turtle()
t.speed(0)
t.color("cyan")
turtle.bgcolor("black")

for i in range(500):
    t.forward(i)
    t.left(800)

turtle.done()
