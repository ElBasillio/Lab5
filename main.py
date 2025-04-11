from parser import read_shapes_from_csv
from shapes import Shape2D, Shape3D

def print_shape_info(shape):
    if isinstance(shape, Shape2D):
        print(f"{shape.__class__.__name__}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")
    elif isinstance(shape, Shape3D):
        print(f"{shape.__class__.__name__}: Volume = {shape.volume():.2f}")
    else:
        print("Unknown shape type")

if __name__ == "__main__":
    shapes = read_shapes_from_csv("shapes.csv")
    for shape in shapes:
        print_shape_info(shape)