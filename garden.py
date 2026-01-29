import turtle

# ---------------- Screen ----------------
screen = turtle.Screen()
screen.setup(1000, 600)
screen.bgcolor("skyblue")
screen.title("House with Garden and Tree")

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
move(-500, -200)
rectangle("lightgreen", 1000, 200)

# ---------------- House ----------------
def draw_house():
    # Body
    move(-200, -200)
    rectangle("lightyellow", 300, 200)

    # Roof
    t.color("black", "brown")
    t.begin_fill()
    move(-220, 0)
    t.goto(-50, 160)
    t.goto(120, 0)
    t.goto(-220, 0)
    t.end_fill()

    # Door
    move(-70, -200)
    rectangle("saddlebrown", 60, 100)

    # Windows
    move(-160, -80)
    square("lightblue", 50)

    move(20, -80)
    square("lightblue", 50)

# ---------------- Tree ----------------
def draw_tree():
    # Trunk
    move(200, -200)
    rectangle("sienna", 40, 120)

    # Leaves
    move(220, -80)
    t.color("darkgreen")
    t.begin_fill()
    t.circle(60)
    t.end_fill()

    move(180, -40)
    t.begin_fill()
    t.circle(60)
    t.end_fill()

    move(260, -40)
    t.begin_fill()
    t.circle(60)
    t.end_fill()

# ---------------- Flowers ----------------
def flower(x, y):
    move(x, y)
    t.color("red")
    for _ in range(6):
        t.circle(5)
        t.left(60)
    t.color("yellow")
    t.begin_fill()
    t.circle(4)
    t.end_fill()

# ---------------- Garden ----------------
def draw_garden():
    for x in range(-350, 350, 80):
        flower(x, -180)

# ---------------- Sun ----------------
def draw_sun():
    move(-350, 200)
    t.color("orange")
    t.begin_fill()
    t.circle(40)
    t.end_fill()

# ---------------- Draw Scene ----------------
draw_sun()
draw_house()
draw_tree()
draw_garden()

turtle.done()
