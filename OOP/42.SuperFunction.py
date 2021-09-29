# super() = Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):
        # since we have length and width on both methods, we can reuse that with the super function
        super().__init__(length, width)

    def area(self):
        return self.length * self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


square = Square(4, 2)
cube = Cube(4, 2, 3)

print(square.area())
print(cube.volume())
