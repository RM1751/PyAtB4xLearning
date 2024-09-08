# Polymorphism in Python:= What is Polymorphism: The word polymorphism means having many forms. In programming,
# polymorphism means the same function name (but different signatures) being used for different types. The key
# difference is the data types and number of arguments used in function.
class Shape:
    def area(self):
        print("The Area of the shape ")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1 = Rectangle(3, 4)
print(shape1.area())
