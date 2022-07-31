import turtle

# Create a canvas instance
myturtle = turtle.Turtle()

# Go to a certain coordinate
myturtle.penup()
myturtle.goto(50, 75)

myturtle.pendown()

for _ in range(4):
    myturtle.forward(100)
    myturtle.left(90)

turtle.done()
