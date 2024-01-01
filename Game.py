import math
import turtle
import random

win = turtle.Screen()
win.bgcolor("black")
win.title("Space Invaders")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scoreString = "Score: %s" % score
score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -290)
player.setheading(90)
player.speed = 0

number_of_enemy = 5
enemies = []
for i in range(number_of_enemy):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemySpeed = 2

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bulletSpeed = 20
bulletSate = "ready"


def move_left():
    player.speed = -15


def move_right():
    player.speed = 15


def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletSate

    if bulletSate == "ready":
        bulletSate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


win.listen()
win.onkey(move_left, "Left" or "a")
win.onkey(move_right, "Right")
win.onkey(fire_bullet, "space")

while True:
    move_player()

    for enemy in enemies:
        x = enemy.xcor()
        x += enemySpeed
        enemy.setx(x)

        if enemy.xcor() > 280:
            for i in enemies:
                y = i.ycor()
                y -= 40
                i.sety(y)
            enemySpeed *= -1

        if enemy.xcor() < -280:
            for i in enemies:
                y = i.ycor()
                y -= 40
                i.sety(y)
            enemySpeed *= -1

        if is_collision(bullet, enemy):
            bullet.hideturtle()
            bulletSate = "ready"
            bullet.setposition(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)

            score += 10
            scoreString = "Score: %s" % score
            score_pen.clear()
            score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))

        if is_collision(enemy, player):
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER")
            break

    if bulletSate == "fire":
        y = bullet.ycor()
        y += bulletSpeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletSate = "ready"

turtle.mainloop()
