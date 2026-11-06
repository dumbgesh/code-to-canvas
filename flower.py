import turtle

pen = turtle.Turtle()
pen.speed(10)

for i in range(6):
    pen.circle(50)
    pen.right(60)

pen.right(90)
pen.forward(200)

turtle.done()
