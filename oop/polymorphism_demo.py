import math

class Shape:
    """Base class representing a generic shape."""
    def area(self):
        """Calculate the area of the shape. Must be overridden by derived classes."""
        raise NotImplementedError("The area method must be implemented by derived classes.")

class Rectangle(Shape):
    """Class representing a rectangle, inheriting from Shape."""
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    """Class representing a circle, inheriting from Shape."""
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)
