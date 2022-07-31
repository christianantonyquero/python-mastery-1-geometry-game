from random import randint


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside_rectangle(self, rectangle):
        if rectangle.ll.x < self.x < rectangle.ur.x \
                and rectangle.ll.y < self.y < rectangle.ur.y:
            return True
        else:
            return False

    def distance(self, point):
        return ((self.x - point.x) ** 2
                + (self.y - point.y) ** 2) ** 0.5


class Rectangle:
    def __init__(self, ll, ur):
        self.ll = ll
        self.ur = ur

    def area(self):
        return (self.ur.x - self.ll.x) * (self.ur.y - self.ll.y)


# Create rectangle object
p1 = Point(randint(0, 400), randint(0, 400))
p2 = Point(randint(10, 400), randint(10, 400))
rectangle = Rectangle(p1, p2)

# Print rectangle coordinates
print("Rectangle Coordinates: (",
      rectangle.ll.x, ",",
      rectangle.ll.y, ") and (",
      rectangle.ur.x, ",",
      rectangle.ur.y, ")", )

# Get point and area from the user
user_x_input = float(input("Guess X: "))
user_y_input = float(input("Guess Y: "))
user_point = Point(user_x_input, user_y_input)
user_area_input = float(input("Guess rectangle area: "))

# Print out game result
result = user_point.is_inside_rectangle(rectangle)
print("Your point is inside the rectangle: ", result)

print("Your area was off by: ",
      rectangle.area() - user_area_input)

# Measure distances
user_point_to_ll_distance = user_point.distance(rectangle.ll)
user_point_to_ur_distance = user_point.distance(rectangle.ur)

# Print distance to points
print(user_point_to_ll_distance)
print(user_point_to_ur_distance)
