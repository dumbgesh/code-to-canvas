import turtle

pen = turtle.Turtle()
pen.speed(5)
pen.pensize(3)

# Function to draw one tulip
def draw_tulip(x, y, flower_color):

    # Draw stem
    pen.penup()
    pen.goto(0, -170)
    pen.pendown()
    pen.color("green")
    pen.goto(x, y - 35)

    # Position at left side of flower
    pen.penup()
    pen.goto(x - 35, y)
    pen.setheading(0)
    pen.pendown()

    # Draw U-shaped flower

    pen.color(flower_color)
    pen.fillcolor(flower_color)

    pen.begin_fill()

    pen.forward(70)          # Horizontal line
    pen.setheading(90)
    pen.circle(35, -180)     # Downward semicircle

    pen.end_fill()

# Draw four tulips
draw_tulip(-120, 100, "red")
draw_tulip(-40, 180, "yellow")
draw_tulip(50, 170, "purple")
draw_tulip(130, 100, "pink")

turtle.done()