from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.triangle import Triangle
from shapes.cube import Cube
from shapes.sphere import Sphere
from shapes.cylinder import Cylinder
import csv


def safe_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None  # або підняти виняток, якщо обов'язково

class ShapeFactory:
    @staticmethod
    def create_shape(data: dict):
        shape_type = data["type"].lower()

        if shape_type == "circle":
            radius = safe_float(data.get("radius") or data.get("side"))
            if radius is None:
                raise ValueError("Missing radius for circle")
            return Circle(radius)

        elif shape_type == "rectangle":
            a = safe_float(data["a"])
            b = safe_float(data["b"])
            if a is None or b is None:
                raise ValueError("Missing sides for rectangle")
            return Rectangle(a, b)

        elif shape_type == "triangle":
            side = safe_float(data["side"])
            if side is None:
                raise ValueError("Missing side for triangle")
            return Triangle(side)

        elif shape_type == "cube":
            side = safe_float(data["side"])
            if side is None:
                raise ValueError("Missing side for cube")
            return Cube(side)

        elif shape_type == "sphere":
            radius = safe_float(data.get("radius") or data.get("side"))
            if radius is None:
                raise ValueError("Missing radius for sphere")
            return Sphere(radius)

        elif shape_type == "cylinder":
            radius = safe_float(data.get("radius") or data.get("side"))
            height = safe_float(data["height"])
            if radius is None or height is None:
                raise ValueError("Missing radius or height for cylinder")
            return Cylinder(radius, height)

        else:
            raise ValueError(f"Unknown shape: {shape_type}")

def read_shapes_from_csv(filename):
    """Read shapes data from a CSV file and return a list of shape objects."""
    shapes = []
    
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                shape = ShapeFactory.create_shape(row)
                shapes.append(shape)
            except ValueError as e:
                print(f"Error creating shape: {e}")
    
    return shapes