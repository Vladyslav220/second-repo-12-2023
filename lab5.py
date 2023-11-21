from enum import Enum
import math


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Polygon:
    def __init__(self, *points):
        self.__points = list(points)

    @property
    def points(self):
        return self.__points

    def perimeter(self):
        if len(self.__points) < 3:
            return 0
        perimeter = 0
        for i in range(len(self.__points)):
            j = (i + 1) % len(self.__points)
            perimeter += math.sqrt((self.__points[j].x - self.__points[i].x) ** 2 + (self.__points[j].y - self.__points[i].y) ** 2)
        return perimeter

    def longest_diagonal(self):
        if len(self.__points) < 3:
            return 0
        max_distance = 0
        for i in range(len(self.__points)):
            for j in range(i + 1, len(self.__points)):
                distance = math.sqrt((self.__points[j].x - self.__points[i].x) ** 2 + (self.__points[j].y - self.__points[i].y) ** 2)
                if distance > max_distance:
                    max_distance = distance
        return max_distance

    def sort_by_x(self):
        self.__points.sort(key=lambda point: [point.x, point.y])

    def sort_by_y(self):
        self.__points.sort(key=lambda point: [point.y, point.x])


if __name__ == '__main__':
    p1 = Point(0, 0)
    p2 = Point(1, 0)
    p3 = Point(1, 1)
    p4 = Point(0, 1)
    polygon = Polygon(p1, p2, p3, p4)

    print("Периметр:", polygon.perimeter())
    print("Найбільша діагональ:", polygon.longest_diagonal())

    print("Перед сортуванням за x:")
    for point in polygon.points:
        print(f"({point.x}, {point.y})")

    polygon.sort_by_x()
    print("Після сортування за x:")
    for point in polygon.points:
        print(f"({point.x}, {point.y})")

    print("Перед сортуванням за y:")
    for point in polygon.points:
        print(f"({point.x}, {point.y})")

    polygon.sort_by_y()
    print("Після сортування за y:")
    for point in polygon.points:
        print(f"({point.x}, {point.y})")
