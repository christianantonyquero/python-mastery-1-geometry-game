import turtle
from random import randint


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside_rectangle(self, rectangle_to_compare):
        if rectangle_to_compare.point1.x < self.x < rectangle_to_compare.point2.x \
                and rectangle_to_compare.point1.y < self.y < rectangle_to_compare.point2.y:
            return True
        else:
            return False

    def distance(self, point):
        return ((self.x - point.x) ** 2
                + (self.y - point.y) ** 2) ** 0.5


class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()

        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)


class GuiPoint(Point):
    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


# Generate 2 random points
p1 = Point(randint(0, 400), randint(0, 400))
p2 = Point(randint(10, 400), randint(10, 400))

# Draw random generated rectangle
rectangle = GuiRectangle(p1, p2)
# Print rectangle coordinates
print("Rectangle Coordinates: (", rectangle.point1.x, ",",
      rectangle.point1.y, ") and (", rectangle.point2.x, ",",
      rectangle.point2.y, ")", )


# Get input point from the user
user_x_input = float(input("Guess X: "))
user_y_input = float(input("Guess Y: "))
# Draw user input point
user_point = GuiPoint(user_x_input, user_y_input)

# Get area guess from the user
user_area_input = float(input("Guess rectangle area: "))

# Print out game result
result = user_point.is_inside_rectangle(rectangle)
print("Your point is inside the rectangle: ", result)

print("Your area was off by: ", rectangle.area() - user_area_input)

# Measure distances
user_point_to_point1_distance = user_point.distance(rectangle.point1)
user_point_to_point2_distance = user_point.distance(rectangle.point2)

# Print distance to points
print(user_point_to_point1_distance, user_point_to_point2_distance)

# Initialize Turtle
myturtle = turtle.Turtle()

# Draw rectangle on canvas
rectangle.draw(canvas=myturtle)

# Draw point on canvas
user_point.draw(canvas=myturtle)

turtle.done()
