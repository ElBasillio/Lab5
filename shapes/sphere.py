import math
from .shape3d import Shape3D

class Sphere(Shape3D):
    def __init__(self, radius: float):
        self.radius = radius

    def volume(self) -> float:
        return (4 / 3) * math.pi * self.radius ** 3
