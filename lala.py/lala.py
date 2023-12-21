import turtle as t
from turtle import *
import random as r

t.speed(10)
t.delay(0)

n = 100.0
screensize(bg='black')
left(90)
forward(3 * n)
color("orange", "yellow")
begin_fill()
left(126)

for i in range(5):
    forward(n / 5)
    right(144)
    forward(n / 5)
    left(72)
end_fill()
right(126)


def drawlight():
    if r.randint(0, 30) == 0:
        color('tomato')
        circle(6)
    elif r.randint(0, 30) == 1:
        color('orange')
        circle(3)
    else:
        color('dark green')


color("dark green")
backward(n * 4.8)


def tree(d, s):
    if d <= 0: return
    forward(s)
    tree(d - 1, s * .8)
    right(120)
    tree(d - 3, s * .5)
    drawlight()
    right(120)
    tree(d - 3, s * .5)
    right(120)
    backward(s)


tree(15, n)
backward(n / 2)

for i in range(200):
    a = 200 - 400 * r.random()
    b = 10 - 20 * r.random()
    up()
    forward(b)
    left(90)
    forward(a)
    down()
    if r.randint(0, 1) == 0:
        color('tomato')
    else:
        color('wheat')
    circle(2)
    up()
    backward(a)
    right(90)
    backward(b)

t.color("dark red", "red")
t.penup()
t.goto(0, -100)  # Adjust the y-coordinate to move the text below the tree
t.pendown()
t.write("Merry Christmas", align="center", font=("Comic Sans MS", 40, "bold"))
t.penup()
t.goto(0, -150)  # Adjust the y-coordinate to move the text below the tree
t.pendown()
t.write("Các Chị em, Chúc các chị em có giáng sinh vui vẻ ", align="center", font=("Comic Sans MS", 30, "normal"))


def drawsnow():
    flakes = []
    t.pensize(2)
    for i in range(200):
        flake = {'x': r.randint(-350, 350), 'y': r.randint(-100, 350), 'size': r.randint(1, 10)}
        flakes.append(flake)

    while True:
        for flake in flakes:
            t.pencolor("white")
            t.pu()
            t.setx(flake['x'])
            t.sety(flake['y'])
            t.pd()
            dens = 6
            snowsize = flake['size']
            for j in range(dens):
                t.fd(int(snowsize))
                t.backward(int(snowsize))
                t.right(int(360 / dens))
                flake['y'] -= 1  # Move snowflake downward

            if flake['y'] < -100:  # Reset snowflake if it goes below the screen
                flake['y'] = 350


def draw_snowman():
    t.pu()
    t.goto(100, -150)
    t.pd()
    t.color("white")
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.pu()
    t.goto(100, -130)
    t.pd()
    t.color("white")
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.pu()
    t.goto(100, -80)
    t.pd()
    t.color("white")
    t.begin_fill()
    t.circle(40)
    t.end_fill()


drawsnow()
t.done()
