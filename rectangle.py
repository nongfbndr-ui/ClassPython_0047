class Rectangle:
    def __init__(self, length, width):
        if length == 0 or width == 0:
            print("Length and width cannot be 0")
        else:
            self.length = length
            self.width = width

    