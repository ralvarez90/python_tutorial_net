"""NAMED TUPLAS

Las tuplas nombradas son una especie de comninacion entre
clases y tuplas. De el módulo collections es de donde se
importa. Las tuplas nombradas son subclases de tuple.
"""
from collections import namedtuple


def showExample01():
    """Uso de tuplas normales.
    """
    point = (100, 200)
    print(f'point: {point}')
    print(f'point[0] -> {point[0]}')
    print(f'point[1] -> {point[1]}')


def showExmaple02():
    class Point2D:
        def __init__(self, x, y) -> None:
            self.x = x
            self.y = y

        def __eq__(self, value: object) -> bool:
            if not isinstance(value, Point2D):
                return False
            return self.x == value.x and self.y == value.y

        def __str__(self) -> str:
            return f'({self.x}, {self.y})'

    point1 = Point2D(100, 200)
    point2 = Point2D(100, 200)
    print(f'point1: {point1}')
    print(f'point2: {point2}')
    print(point1 is point2)
    print(point1 == point2)


def showExample03():
    Point2D = namedtuple(typename='Point2D', field_names=['x', 'y'])
    point1 = Point2D(x=100, y=200)
    point2 = Point2D(100, 200)
    print(point1)
    print(point2)
    print(point1 is point2)
    print(point2 == point1)
    print(type(Point2D))
    print(Point2D.__dict__)


def main():
    showExample01()
    showExmaple02()
    showExample03()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
