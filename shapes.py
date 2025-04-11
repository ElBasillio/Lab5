from abc import ABC, abstractmethod
import math

class Shape2D(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

class Shape3D(ABC):
    @abstractmethod
    def volume(self) -> float:
        pass

class Circle(Shape2D):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

class Rectangle(Shape2D):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def area(self) -> float:
        return self.a * self.b

    def perimeter(self) -> float:
        return 2 * (self.a + self.b)

class Triangle(Shape2D):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return (math.sqrt(3) / 4) * self.side ** 2

    def perimeter(self) -> float:
        return 3 * self.side

class Cube(Shape3D):
    def __init__(self, side: float):
        self.side = side

    def volume(self) -> float:
        return self.side ** 3

class Sphere(Shape3D):
    def __init__(self, radius: float):
        self.radius = radius

    def volume(self) -> float:
        return (4 / 3) * math.pi * self.radius ** 3

class Cylinder(Shape3D):
    def __init__(self, radius: float, height: float):
        self.radius = radius
        self.height = height

    def volume(self) -> float:
        return math.pi * self.radius ** 2 * self.height