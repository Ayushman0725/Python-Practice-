import turtle
import random
import time

# ---------------- Screen ----------------
screen = turtle.Screen()
screen.title("Catch The Ball - Advanced")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

# ---------------- Player (Tray) ----------------
player = turtle.Turtle()
player.shape("square")
player.color("white")
player.shapesize(stretch_wid=1, stretch_len=5)
player.penup()
player.goto(0, -250)

# ---------------- Ball ----------------
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 250)

# ---------------- Score Board ----------------
score = 0
miss = 0
MAX_MISS = 5

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 260)

def update_score():
    pen.clear()
    pen.write(
        f"Score: {score}   Miss: {miss}/{MAX_MISS}",
        align="center",
        font=("Arial", 18, "bold")
    )

update_score()

# ---------------- Movement Flags ----------------
move_left = False
move_right = False

def left_press():
    global move_left
    move_left = True

def left_release():
    global move_left
    move_left = False

def right_press():
    global move_right
    move_right = True

def right_release():
    global move_right
    move_right = False

screen.listen()
screen.onkeypress(left_press, "Left")
screen.onkeyrelease(left_release, "Left")
screen.onkeypress(right_press, "Right")
screen.onkeyrelease(right_release, "Right")

# ---------------- Game Variables ----------------
ball_speed = 3
game_over = False

# ---------------- Game Over Screen ----------------
def show_game_over():
    pen.goto(0, 0)
    pen.write(
        "GAME OVER\nPress R to Restart",
        align="center",
        font=("Arial", 28, "bold")
    )

def restart_game():
    global score, miss, ball_speed, game_over
    score = 0
    miss = 0
    ball_speed = 3
    game_over = False
    ball.goto(random.randint(-380, 380), 250)
    player.goto(0, -250)
    pen.goto(0, 260)
    update_score()

screen.onkey(restart_game, "r")

# ---------------- Main Game Loop ----------------
while True:
    screen.update()
    time.sleep(0.02)

    if game_over:
        continue

    # Smooth tray movement
    if move_left and player.xcor() > -350:
        player.setx(player.xcor() - 6)

    if move_right and player.xcor() < 350:
        player.setx(player.xcor() + 6)

    # Move ball
    ball.sety(ball.ycor() - ball_speed)

    # Ball missed
    if ball.ycor() < -300:
        miss += 1
        ball.goto(random.randint(-380, 380), 250)
        update_score()

        if miss >= MAX_MISS:
            game_over = True
            pen.clear()
            show_game_over()

    # Collision detection
    if (ball.ycor() < -220 and
        player.xcor() - 60 < ball.xcor() < player.xcor() + 60):
        score += 1
        ball_speed += 0.4
        ball.goto(random.randint(-380, 380), 250)
        update_score()
