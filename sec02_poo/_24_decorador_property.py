"""DECORADOR @property

Permite establecer propiedades através del decorador @property así como
asignarle sus respecivos setters de forma dinámica.

Dado una propiedad, si no establecemos su respectivo setter entonces
la propiedad será de solo lectura. Es decir, una vez establecido su estado
este no podrá cambiarse.
"""


class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        assert value != '', 'name cannot be an empty string'
        self._name = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        assert value >= 0, 'Age value cannot be a negative integer'
        self._age = value

    def __str__(self) -> str:
        return f'Person{self.__dict__}'


class Circle:
    PI = 3.14159

    def __init__(self, radius: float) -> None:
        self._radius = radius
        self._area = None

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        assert value >= 0, 'Radius value cannot be a negative number'
        self._radius = value

    @property
    def area(self) -> float:
        return self.PI * self._radius**2

    def __str__(self) -> str:
        return 'Circle{radius: %s, area: %.2f u^2}' % (self.radius, self.area)


def showExample01():
    p1 = Person(name='John Wick', age=45)
    p1.age += 1
    p1.name = 'Juan Wick'
    print(p1)


def showExample02():
    c = Circle(10)
    print(f'Area: {c.area} u^2')
    print(c)


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
