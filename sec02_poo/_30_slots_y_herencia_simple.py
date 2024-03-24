"""SLOTS Y HERENCIA SIMPLES

El uso de __slots__ en el contexto de herencia puede ser algo
complicado.

Una clase padre puede contener slots pero no su clase hija, esto
quiere decir que el dict __dict__ de dichas istancias será
de la clase hija y los slots del padre. Se suele recomendar que
si una clase padre usa slots también los hijos.

Otro escenario es que una clase padre no tenga __slots__ pero las
clases hijas si. Esto quiere decir que las instancias de la clase
hija tendrán la propiedad __dict__ y __slot__.
"""


class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'


class Point3D(Point2D):
    __slots__ = ('z',)

    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x, y)
        self.z = z

    def __repr__(self) -> str:
        return f'({self.x}, {self.y}, {self.y})'


class Shape:
    pass


class Coordenada2D(Shape):
    __slots__ = ('x', 'y')

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


def showExample01():
    point = Point3D(10, 20, 30)
    point.x = 1
    print(point.__slots__)
    print(point)


def showExample02():
    point = Coordenada2D(10, 20)
    print(point.__dict__)
    print(point.__slots__)


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
