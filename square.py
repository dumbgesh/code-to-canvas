import turtle

pen = turtle.Turtle()
pen.speed(3)

for i in range(4):
    pen.forward(100)
    pen.left(90)

turtle.done()

# this can become hexagon if you change the range to 6 and the left turn to 60 degrees