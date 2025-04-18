import unittest
import os
import csv
from parser import safe_float, ShapeFactory, read_shapes_from_csv
from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.triangle import Triangle
from shapes.cube import Cube
from shapes.sphere import Sphere
from shapes.cylinder import Cylinder


class TestSafeFloat(unittest.TestCase):
    def test_valid_float(self):
        self.assertEqual(safe_float("5.5"), 5.5)
        self.assertEqual(safe_float("3"), 3.0)
        
    def test_invalid_float(self):
        self.assertIsNone(safe_float(""))
        self.assertIsNone(safe_float("abc"))
        self.assertIsNone(safe_float(None))

class TestShapeFactory(unittest.TestCase):
    def test_create_circle(self):
        data = {"type": "circle", "radius": "5"}
        shape = ShapeFactory.create_shape(data)
        self.assertIsInstance(shape, Circle)
        self.assertEqual(shape.radius, 5.0)
        
        # Test with side instead of radius
        data = {"type": "circle", "side": "3"}
        shape = ShapeFactory.create_shape(data)
        self.assertIsInstance(shape, Circle)
        self.assertEqual(shape.radius, 3.0)
        
    def test_create_rectangle(self):
        data = {"type": "rectangle", "a": "4", "b": "6"}
        shape = ShapeFactory.create_shape(data)
        self.assertIsInstance(shape, Rectangle)
        self.assertEqual(shape.a, 4.0)
        self.assertEqual(shape.b, 6.0)
        
    def test_create_triangle(self):
        data = {"type": "triangle", "side": "3"}
        shape = ShapeFactory.create_shape(data)
        self.assertIsInstance(shape, Triangle)
        self.assertEqual(shape.side, 3.0)
        
    def test_create_cube(self):
        data = {"type": "cube", "side": "3"}
        shape = ShapeFactory.create_shape(data)
        self.assertIsInstance(shape, Cube)
        self.assertEqual(shape.side, 3.0)
        
    def test_create_sphere(self):
        data = {"type": "sphere", "radius": "7"}
        shape = ShapeFactory.create_shape(data)
        self.assertIsInstance(shape, Sphere)
        self.assertEqual(shape.radius, 7.0)
        
        # Test with side instead of radius
        data = {"type": "sphere", "side": "5"}
        shape = ShapeFactory.create_shape(data)
        self.assertIsInstance(shape, Sphere)
        self.assertEqual(shape.radius, 5.0)
        
    def test_create_cylinder(self):
        data = {"type": "cylinder", "radius": "3", "height": "10"}
        shape = ShapeFactory.create_shape(data)
        self.assertIsInstance(shape, Cylinder)
        self.assertEqual(shape.radius, 3.0)
        self.assertEqual(shape.height, 10.0)
        
        # Test with side instead of radius
        data = {"type": "cylinder", "side": "2", "height": "5"}
        shape = ShapeFactory.create_shape(data)
        self.assertIsInstance(shape, Cylinder)
        self.assertEqual(shape.radius, 2.0)
        self.assertEqual(shape.height, 5.0)
        
    def test_invalid_shape(self):
        data = {"type": "hexagon", "side": "5"}
        with self.assertRaises(ValueError):
            ShapeFactory.create_shape(data)
            
    def test_missing_params(self):
        # Missing radius for circle
        with self.assertRaises(ValueError):
            ShapeFactory.create_shape({"type": "circle"})
            
        # Missing sides for rectangle
        # В оригінальному коді напряму використовується data["a"] і data["b"],
        # тому очікуємо KeyError, а не ValueError
        with self.assertRaises(KeyError):
            ShapeFactory.create_shape({"type": "rectangle", "a": "4"})
            
        with self.assertRaises(KeyError):
            ShapeFactory.create_shape({"type": "rectangle"})
            
        # Missing side for triangle
        with self.assertRaises(KeyError):
            ShapeFactory.create_shape({"type": "triangle"})
            
        # Missing side for cube
        with self.assertRaises(KeyError):
            ShapeFactory.create_shape({"type": "cube"})
            
        # Missing radius for sphere
        with self.assertRaises(ValueError):
            ShapeFactory.create_shape({"type": "sphere"})
            
        # Missing radius for cylinder
        with self.assertRaises(ValueError):
            ShapeFactory.create_shape({"type": "cylinder", "height": "5"})
            
        # Missing height for cylinder
        with self.assertRaises(KeyError):
            ShapeFactory.create_shape({"type": "cylinder", "radius": "3"})

class TestReadShapesFromCSV(unittest.TestCase):
    def setUp(self):
        # Створюємо тимчасовий CSV файл для тестування
        self.test_csv = "test_shapes.csv"
        with open(self.test_csv, 'w', newline='') as csvfile:
            fieldnames = ['type', 'a', 'b', 'radius', 'side', 'height']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'type': 'circle', 'radius': '5'})
            writer.writerow({'type': 'rectangle', 'a': '4', 'b': '6'})
            writer.writerow({'type': 'triangle', 'side': '3'})
            writer.writerow({'type': 'cube', 'side': '3'})
            writer.writerow({'type': 'sphere', 'radius': '7'})
            writer.writerow({'type': 'cylinder', 'radius': '3', 'height': '10'})
            # Додаємо неправильний рядок
            writer.writerow({'type': 'hexagon', 'side': '5'})
    
    def tearDown(self):
        # Видаляємо тимчасовий файл після тестування
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)
    
    def test_read_shapes(self):
        shapes = read_shapes_from_csv(self.test_csv)
        # Перевіряємо, що ми отримали правильну кількість фігур (6 валідних фігур, 1 невалідна)
        self.assertEqual(len(shapes), 6)
        
        # Перевіряємо типи фігур
        self.assertIsInstance(shapes[0], Circle)
        self.assertIsInstance(shapes[1], Rectangle)
        self.assertIsInstance(shapes[2], Triangle)
        self.assertIsInstance(shapes[3], Cube)
        self.assertIsInstance(shapes[4], Sphere)
        self.assertIsInstance(shapes[5], Cylinder)
        
        # Перевіряємо параметри фігур
        self.assertEqual(shapes[0].radius, 5.0)
        self.assertEqual(shapes[1].a, 4.0)
        self.assertEqual(shapes[1].b, 6.0)
        self.assertEqual(shapes[2].side, 3.0)
        self.assertEqual(shapes[3].side, 3.0)
        self.assertEqual(shapes[4].radius, 7.0)
        self.assertEqual(shapes[5].radius, 3.0)
        self.assertEqual(shapes[5].height, 10.0)
    
    def test_read_empty_file(self):
        # Створюємо порожній CSV файл
        empty_csv = "empty.csv"
        with open(empty_csv, 'w', newline='') as csvfile:
            fieldnames = ['type', 'a', 'b', 'radius', 'side', 'height']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        
        shapes = read_shapes_from_csv(empty_csv)
        self.assertEqual(len(shapes), 0)
        
        # Видаляємо тимчасовий файл
        if os.path.exists(empty_csv):
            os.remove(empty_csv)
    
    def test_file_not_found(self):
        # Тестуємо випадок, коли файл не існує
        with self.assertRaises(FileNotFoundError):
            read_shapes_from_csv("nonexistent_file.csv")

if __name__ == '__main__':
    unittest.main()