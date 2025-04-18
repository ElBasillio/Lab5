from .shape2d import Shape2D

class Rectangle(Shape2D):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def area(self) -> float:
        return self.a * self.b

    def perimeter(self) -> float:
        return 2 * (self.a + self.b)
