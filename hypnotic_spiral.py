import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

colors = ["red", "yellow", "blue", "green", "purple", "orange"]

for i in range(120):
    t.color(colors[i % 6])
    t.circle(5 * i)
    t.right(40)
turtle.done()
