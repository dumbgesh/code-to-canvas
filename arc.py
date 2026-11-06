import turtle

pen = turtle.Turtle()
pen.speed(3)

for i in range(2):
    while i <= 2:
        pen.forward(100)
        pen.left(90)
        i += 1
        pen.circle(100, 180)

turtle.done()