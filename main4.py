import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(600,500)
screen.bgcolor('black')
turtle.colormode(255)
t.ht()
t.speed(50)
x = 50
r = 254
g = 0
b = 0
t.penup()
# t.goto(-400, -250)
t.pendown()
while x < 1000:
    tup = (r, g, b)
    t.pencolor(tup)
    for i in range(20):
        if r == 254 and g < 254 and b == 0:
            g += 2
        elif r > 0 and g == 254 and b == 0:
            r -= 2
        elif r == 0 and g == 254 and b < 254:
            b += 2
        elif r == 0 and g > 0 and b == 254:
            g -= 2
        elif r < 254 and g == 0 and b == 254:
            r += 2
        elif r == 254 and g == 0 and b > 0:
            b -= 2
        # t.fd(x/5)
    for j in range(2):
        t.circle(x, 90)
        t.circle(x // 3,90)
    x = x + 1

    t.penup()
    t.goto(0, 0)
    print(x)

    t.right(5)
    t.pendown()

turtle.done()
