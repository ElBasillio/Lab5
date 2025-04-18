from .shape3d import Shape3D

class Cube(Shape3D):
    def __init__(self, side: float):
        self.side = side

    def volume(self) -> float:
        return self.side ** 3
