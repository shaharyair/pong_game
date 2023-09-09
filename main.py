import turtle
import random
import time
import os


def add_long_space(a, string1, string2):
    return string1 + " " * a + string2


# Game Screen
screen = turtle.Screen()
screen.title('Pong Game')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

# Score Board
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = random.choice([-2, 2])
ball.dy = random.choice([-2, 2])

# Scoreboard
score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0, 250)

# winner
win = turtle.Turtle()
win.speed(0)
win.color('white')
win.penup()
win.hideturtle()
win.goto(0, 0)


# Paddle Movement
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


# Paddle B movement
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


screen.listen()
screen.onkeypress(paddle_a_up, 'w')
screen.onkeypress(paddle_a_down, 's')
screen.onkeypress(paddle_b_up, 'Up')
screen.onkeypress(paddle_b_down, 'Down')

# Main Game Loop
os.system('afplay start.mp3&')

while True:
    screen.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # If the ball touches after the top part or the bottom part of the screen
    # the ball will change the dy to negative and change the y direction
    if ball.ycor() > 285:
        ball.sety(285)
        ball.dy *= -1
        os.system('afplay pongsound.mp3&')

    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1
        os.system('afplay pongsound.mp3&')

    # if the ball touches the right or the left side of the screen
    # it will go to the center and get a random x and y direction \ add to the scoreboard
    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= random.choice([-1, 1])
        score_a += 1

    if ball.xcor() < -370:
        ball.goto(0, 0)
        ball.dx *= random.choice([-1, 1])
        score_b += 1

    # Ball and Paddle Collisions
    if 330 < ball.xcor() < 340 and paddle_b.ycor() + 60 > ball.ycor() > paddle_b.ycor() - 60:
        ball.setx(330)
        ball.dx *= -1
        os.system('afplay pongsound.mp3&')

    if -330 > ball.xcor() > -340 and paddle_a.ycor() + 60 > ball.ycor() > paddle_a.ycor() - 60:
        ball.setx(-330)
        ball.dx *= -1
        os.system('afplay pongsound.mp3&')

    # Score
    score.clear()
    score.write(add_long_space(30, f'Player A: {score_a}', f'Player B: {score_b}'), align='center',
                font=('courier', 20, 'normal'))
    screen.update()

    # Winner = 3
    if score_a >= 3:
        win.write('Player A Won!', align='center', font=('courier', 55, 'normal'))
        screen.update()
        ball.hideturtle()
        time.sleep(5)
        break

    if score_b >= 3:
        win.write('Player B Won!', align='center', font=('courier', 55, 'normal'))
        screen.update()
        ball.hideturtle()
        time.sleep(5)
        break

    # Loop Paddle Movement
    # Paddle A
    if paddle_a.ycor() >= 380:
        paddle_a.sety(-380)
    elif paddle_a.ycor() <= -380:
        paddle_a.sety(380)

    # Paddle B
    if paddle_b.ycor() >= 380:
        paddle_b.sety(-380)
    elif paddle_b.ycor() <= -380:
        paddle_b.sety(380)

    # Ball sleep each time it gets to the center
    if ball.xcor() == 0:
        time.sleep(0.2)
