"""
Var 17
"""
from enum import Enum
import math


class Color(Enum):
    """
    Define a color
    """
    RED = 1
    GREEN = 2
    BLUE = 3


class Point:
    """
    Define a point
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    def get_x(self):
        """Get x"""
        return self.x
    def get_y(self):
        """Get y"""
        return self.y
    def print_point(self):
        """Print out point data"""
        print(f"Point x = {self.x}, y = {self.y}")
    def __del__(self):
        """Destructor"""
        print("Point has been deleted")


class Polynom:
    """
    Define a polynom with color and points
    """
    def __init__(self, color, *points):
        self.color = color
        self.points = list(points)

    def __repr__(self):
        return f"Polynom({self.color.name}, {', '.join(map(str, self.points))})"
    def get_points(self):
        """Get list of points"""
        return self.points

    def get_color(self):
        """Get color of a point"""
        return self.color
    def print_polynom(self):
        """Print out polynom data"""
        print(f"Polynom color {self.color} with points {self.points}")
    def perimeter(self):
        """Count perimeter"""
        if len(self.points) < 2:
            return 0

        p = 0
        for i in range(len(self.points) - 1):
            p += math.dist((self.points[i].x,
                            self.points[i].y),
                           (self.points[i + 1].x,
                            self.points[i + 1].y))
        p += math.dist((self.points[-1].x,
                         self.points[-1].y),
                       (self.points[0].x,
                         self.points[0].y))
        return p
    def longest_diagonal(self):
        """Define longest diagonal"""
        if len(self.points) < 4:
            return 0

        max_distance = 0
        for i in range(len(self.points) - 1):
            for j in range(i + 1, len(self.points)):
                distance = math.dist(
                    (self.points[i].x, self.points[i].y), (self.points[j].x, self.points[j].y))
                if distance > max_distance:
                    max_distance = distance
        return max_distance
    def sort_by_x(self):
        """Sort points by x"""
        def get_x_(point):
            return point.get_x()
        return self.points.sort(key=get_x_)
    def sort_by_y(self):
        """Sort points by y"""
        def get_y(point):
            return point.y
        self.points.sort(key=get_y)
    def __del__(self):
        print("Polynom has been deleted")

        
if __name__ == "__main__":
    point1 = Point(0, 0)
    point2 = Point(3, 0)
    point3 = Point(1, 2)
    point4 = Point(2, 1)

    polynom = Polynom(Color.RED, point1, point2, point3, point4)

    print("Original Polynom:")
    print(polynom)

    print(f"Perimeter: {polynom.perimeter()}")
    print(f"Longest Diagonal: {polynom.longest_diagonal()}")

    polynom.sort_by_x()
    print("\nSorted by X:")
    print(polynom)
    polynom.sort_by_y()
    print("\nSorted by Y:")
    print(polynom)

    polynom1 = Polynom(Color.GREEN, point1, point2, point3)
    print(f"\n\npolynom1: {polynom1}")
    print(f"Perimeter polynom1: {polynom1.perimeter()}")
    print(f"Longest Diagonal polynom1: {polynom1.longest_diagonal()}")
