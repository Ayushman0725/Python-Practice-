import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Advanced Turtle Art")

# Turtle setup
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
t.hideturtle()
turtle.colormode(255)

# Function to generate a list of colors using HSV
def generate_colors(n):
    colors = []
    hue = 0
    for i in range(n):
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        colors.append((int(r * 255), int(g * 255), int(b * 255)))
        hue += 1 / n
    return colors

# Recursive pattern drawing
def draw_pattern(size, depth, colors):
    if depth == 0:
        return
    t.pencolor(colors[depth % len(colors)])
    for _ in range(6):  # Hexagonal symmetry
        t.forward(size)
        draw_pattern(size / 3, depth - 1, colors)
        t.backward(size)
        t.right(60)

# Main drawing
t.penup()
t.goto(0, 0)
t.pendown()

colors = generate_colors(36)  # Smooth gradient colors
draw_pattern(200, 5, colors)

# Keep window open until clicked
turtle.done()
