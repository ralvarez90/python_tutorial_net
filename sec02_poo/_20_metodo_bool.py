"""MÉTODO __bool__

Absolutamente todos los objetos en python se pueden evaluar como
booleanos empleando la clase bool.

Por default todos los objetos no nulos se evalúan como True, este
comportamiento se sobrescribe implementando el método __bool__.

Si no se encuentra implementado el método __bool__ y un objeto se
evalúa como booleano, se invoca el método __len__ por default.
"""


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __bool__(self):
        return self.age >= 18 and self.age <= 65

    def __str__(self) -> str:
        return f'Person{self.__dict__}'


class Payroll:
    def __init__(self, length: float) -> None:
        assert length >= 0, 'Length cannot be a negative number'
        self.length = length

    def __len__(self):
        return self.length

    def __str__(self) -> str:
        return f'Payroll{self.__dict__}'


def show_example_01():
    p1 = Person(name='Persona1', age=10)
    p2 = Person(name='Persona2', age=75)
    p3 = Person(name='Persona3', age=35)
    for p in (p1, p2, p3):
        print(p, bool(p))


def show_example_02():
    p1 = Payroll(123)
    p2 = Payroll(0)
    for p in (p1, p2):
        print(p, bool(p))


def main():
    show_example_01()
    show_example_02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
