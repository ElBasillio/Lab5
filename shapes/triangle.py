import math
from .shape2d import Shape2D

class Triangle(Shape2D):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return (math.sqrt(3) / 4) * self.side ** 2

    def perimeter(self) -> float:
        return 3 * self.side
