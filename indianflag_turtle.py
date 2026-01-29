import turtle
import math
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.setup(1000, 500)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Colors
SAFFRON = "#FF9933"
GREEN = "#138808"
NAVY = "#000080"

FLAG_WIDTH = 500
STRIPE_HEIGHT = 80

# Wave parameters
AMPLITUDE = 10     # lehr ki height
WAVELENGTH = 60
phase = 0

def wave_y(x, base_y, phase):
    return base_y + math.sin((x + phase) / WAVELENGTH) * AMPLITUDE

def draw_stripe(color, base_y):
    t.color(color)
    t.begin_fill()

    t.goto(-FLAG_WIDTH//2, wave_y(-FLAG_WIDTH//2, base_y, phase))
    t.pendown()

    for x in range(-FLAG_WIDTH//2, FLAG_WIDTH//2, 10):
        t.goto(x, wave_y(x, base_y, phase))

    for x in range(FLAG_WIDTH//2, -FLAG_WIDTH//2, -10):
        t.goto(x, wave_y(x, base_y - STRIPE_HEIGHT, phase))

    t.goto(-FLAG_WIDTH//2, wave_y(-FLAG_WIDTH//2, base_y, phase))
    t.end_fill()
    t.penup()

def draw_chakra():
    t.color(NAVY)
    t.width(2)
    t.goto(0, -STRIPE_HEIGHT//2 - 40)
    t.setheading(0)
    t.pendown()
    t.circle(30)
    t.penup()

    for i in range(24):
        t.goto(0, -STRIPE_HEIGHT//2)
        t.setheading(i * 15)
        t.pendown()
        t.forward(30)
        t.penup()

# Flag pole
def draw_pole():
    t.color("brown")
    t.width(6)
    t.goto(-FLAG_WIDTH//2 - 20, -200)
    t.setheading(90)
    t.pendown()
    t.forward(350)
    t.penup()
    t.width(2)

# Animation loop
while True:
    t.clear()

    draw_pole()
    draw_stripe(SAFFRON, 80)
    draw_stripe("white", 0)
    draw_stripe(GREEN, -80)
    draw_chakra()

    screen.update()
    phase += 2
    time.sleep(0.03)
