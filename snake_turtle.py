import turtle
import time
import random

# ---------------- Screen ----------------
screen = turtle.Screen()
screen.title("Snake Game - Fixed")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# ---------------- Snake Head ----------------
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# ---------------- Food ----------------
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# ---------------- Score ----------------
score = 0
high_score = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center",
          font=("Arial", 16, "bold"))

# ---------------- Snake Body ----------------
segments = []

# ---------------- Functions ----------------
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

def game_over():
    global score
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

    score = 0
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}",
              align="center", font=("Arial", 16, "bold"))

# ---------------- Keyboard ----------------
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# ---------------- Main Game Loop ----------------
delay = 0.1

while True:
    screen.update()
    time.sleep(delay)

    # Wall collision
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        game_over()

    # Food collision
    if head.distance(food) < 20:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}",
                  align="center", font=("Arial", 16, "bold"))

        delay = max(0.05, delay - 0.002)

    # Move body
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].xcor(),
                          segments[i - 1].ycor())

    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Self collision
    for segment in segments:
        if segment.distance(head) < 20:
            game_over()
