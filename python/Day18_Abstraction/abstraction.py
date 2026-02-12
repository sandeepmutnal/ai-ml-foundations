# Day 18 - Abstraction using abc module

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle = length * width")

class Circle(Shape):
    def area(self):
        print("Area of Circle = pi * r * r")

# Objects
rect = Rectangle()
circle = Circle()

rect.area()
circle.area()
