import turtle
screen = turtle.Screen()
screen.setup(500, 600, startx=0, starty=100)
t = turtle.Turtle()
S = turtle.Screen()
S.bgcolor("Black")
t.pencolor('red')
a= 0
b = 0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()
while(True):
    t.forward(a)
    t.right(b)
    a+= 3
    b+= 1
    if b == 210:
        break
    t.hideturtle()
    turtle.done