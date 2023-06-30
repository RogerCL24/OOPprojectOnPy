
class Shape():

    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
    
    def draw(self):
        pass

class Circle(Shape):
    
    def __init__(self, x, y, radius):
        self.radius = radius
        super().__init__(x, y,radius,radius)

    def draw(self):
        print(f"Printing the circle's shape on ({self.x}, {self.y}), with radius {self.radius}")

class Triangle(Shape):
    
    def __init__(self, x, y, base, height):
        super().__init__(x, y, base, height)
        self.base = base
    
    def draw(self):
        print (
            f"Printing a triangle on ({self.x}, {self.y}), with base {self.base} and height {self.height}"
            )

class Rectangle(Shape):

    def __init__(self, x, y, height, width):
        super().__init__(x, y, height, width)
        
    def draw(self):
        print(
            f"Printing a rectangle on ({self.x},{self.y}), with height {self.height} and width {self.width}"
              )

circle = Circle(
    x= 12,
    y= 30,
    radius= 3.12
)

rectangle = Rectangle(
    x= 20,
    y= 40,
    height= 50,
    width= 12
)

triangle = Triangle(
    x= 12,
    y= 89,
    base= 56,
    height= 90
)

circle.draw()
rectangle.draw()
triangle.draw()
