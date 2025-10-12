# polymorphism_demo.py

import math

class Shape:
    """Base class representing a general shape."""
    def area(self):
        """Should be overridden by derived classes."""
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    """Derived class representing a rectangle."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculates and returns the area of a rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates and returns the area of a circle."""
        return math.pi * (self.radius ** 2)
from polymorphism_demo import Shape, Rectangle, Circle

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()