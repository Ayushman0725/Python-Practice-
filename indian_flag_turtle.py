import turtle

# Screen setup
screen = turtle.Screen()
screen.title("Indian Flag")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.penup()

# Function to draw a filled rectangle
def draw_rectangle(color, width, height):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Function to draw Ashoka Chakra
def draw_chakra(radius):
    t.color("navy")
    t.width(2)
    t.circle(radius)

    for _ in range(24):
        t.penup()
        t.goto(0, 0)
        t.setheading(0)
        t.right(_ * 15)
        t.pendown()
        t.forward(radius)

# Move turtle to starting position
t.goto(-300, 150)
t.setheading(0)
t.pendown()

# Top stripe (Saffron)
draw_rectangle("#FF9933", 600, 100)

# Middle stripe (White)
t.right(90)
t.forward(100)
t.left(90)
draw_rectangle("white", 600, 100)

# Bottom stripe (Green)
t.right(90)
t.forward(100)
t.left(90)
draw_rectangle("#138808", 600, 100)

# Draw Ashoka Chakra
t.penup()
t.goto(0, -50)
t.setheading(0)
t.pendown()
draw_chakra(40)

t.hideturtle()
turtle.done()
