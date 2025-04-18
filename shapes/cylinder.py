import math
from .shape3d import Shape3D

class Cylinder(Shape3D):
    def __init__(self, radius: float, height: float):
        self.radius = radius
        self.height = height

    def volume(self) -> float:
        return math.pi * self.radius ** 2 * self.height
