import turtle

# screen setup
screen = turtle.Screen()
screen.bgcolor("black")

#turtle setup

t = turtle.Turtle()
t.speed(0)
t.width(2)

colors = ["red", "yellow", "blue", "green", "purple", "orange"]

# draw flower pattern

for i in range(60):
    t.color(colors[i % 6])
    t.circle(100)
    t.left(6)


turtle.done()

