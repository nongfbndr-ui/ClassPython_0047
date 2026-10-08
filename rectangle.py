class Rectangle:
    def __init__(self, length, width):
        if length == 0 or width == 0:
            print("Length and width cannot be 0")
        else:
            self.length = length
            self.width = width

    def circumference(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def __str__(self):
        return "Rectangle: " + str(self.length) + " cm long, and " + str(self.width) + " cm wide"


rectangle = Rectangle(3, 2)

print(rectangle)
print("Circumference:", rectangle.circumference(), "cm")
