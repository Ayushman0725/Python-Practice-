import turtle

# ---------------- Screen ----------------
screen = turtle.Screen()
screen.setup(1200, 650)
screen.bgcolor("skyblue")
screen.title("House, Garden, Mountains & Birds")

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# ---------------- Helpers ----------------
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def rectangle(color, width, height):
    t.color("black", color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def square(color, size):
    rectangle(color, size, size)

# ---------------- Ground ----------------
move(-600, -250)
rectangle("lightgreen", 1200, 250)

# ---------------- Mountains ----------------
def mountain(x1, y1, x2, y2, x3, y3, color):
    t.color("black", color)
    t.begin_fill()
    move(x1, y1)
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1, y1)
    t.end_fill()

mountain(-600, -50, -300, 250, 0, -50, "#9CA3AF")
mountain(-200, -50, 100, 300, 400, -50, "#6B7280")
mountain(200, -50, 500, 220, 800, -50, "#4B5563")

# ---------------- Sun ----------------
move(-450, 250)
t.color("orange")
t.begin_fill()
t.circle(40)
t.end_fill()

# ---------------- House ----------------
def draw_house():
    move(-250, -250)
    rectangle("lightyellow", 300, 200)

    # Roof
    t.color("black", "brown")
    t.begin_fill()
    move(-270, -50)
    t.goto(-100, 130)
    t.goto(50, -50)
    t.goto(-270, -50)
    t.end_fill()

    # Door
    move(-120, -250)
    rectangle("saddlebrown", 60, 100)

    # Windows
    move(-200, -150)
    square("lightblue", 50)
    move(-20, -150)
    square("lightblue", 50)

draw_house()

# ---------------- Tree ----------------
def draw_tree():
    move(150, -250)
    rectangle("sienna", 40, 120)

    for dx, dy in [(-40, 0), (0, 30), (40, 0)]:
        move(170 + dx, -130 + dy)
        t.color("darkgreen")
        t.begin_fill()
        t.circle(60)
        t.end_fill()

draw_tree()

# ---------------- Flowers ----------------
def flower(x, y):
    move(x, y)
    t.color("red")
    for _ in range(6):
        t.circle(6)
        t.left(60)
    t.color("yellow")
    t.begin_fill()
    t.circle(4)
    t.end_fill()

for x in range(-450, 450, 80):
    flower(x, -220)

# ---------------- Birds ----------------
def bird(x, y, size):
    t.color("black")
    move(x, y)
    t.setheading(60)
    t.circle(size, 60)
    move(x, y)
    t.setheading(120)
    t.circle(size, 60)
    t.setheading(0)

bird(-100, 200, 25)
bird(-50, 220, 20)
bird(20, 210, 18)
bird(100, 230, 22)

turtle.done()
