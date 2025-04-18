import unittest
import math
from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.triangle import Triangle
from shapes.cube import Cube
from shapes.sphere import Sphere
from shapes.cylinder import Cylinder

class TestShapes(unittest.TestCase):
    def test_circle(self):
        c = Circle(1)
        self.assertAlmostEqual(c.area(), math.pi)
        self.assertAlmostEqual(c.perimeter(), 2 * math.pi)

    def test_rectangle(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)
        self.assertEqual(r.perimeter(), 10)

    def test_triangle(self):
        t = Triangle(2)
        self.assertAlmostEqual(t.area(), (math.sqrt(3)/4)*4)
        self.assertEqual(t.perimeter(), 6)

    def test_cube(self):
        c = Cube(3)
        self.assertEqual(c.volume(), 27)

    def test_sphere(self):
        s = Sphere(1)
        self.assertAlmostEqual(s.volume(), (4/3)*math.pi)

    def test_cylinder(self):
        cy = Cylinder(1, 2)
        self.assertAlmostEqual(cy.volume(), math.pi * 2)

if __name__ == '__main__':
    unittest.main()