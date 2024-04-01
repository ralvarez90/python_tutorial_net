"""MÉTODO __new__

Cuando creamos instancias el método __new__ es el que
se encarga de crear la referencia en memoria. Este 
invoca en su interior el __init__ para otorgar estado
inicial a cada una de las instancias.

El método __new__ es un método estático que se invoca
desde object.

El método __new__ cuenta con la siguiente firma
object.__new__(class, *args, **kwargs) donde el
primer argumento es la clase del nuevo objeto que
se creará, y *args y **kwargs  deben coincidir con los
parámetros del método __init__.

Cuando defines una nueva clase, esa clase hereda implícitamente 
de la clase de objeto. Significa que puedes anular el método estático 
__new__ y hacer algo antes y después de crear una nueva instancia de 
la clase.

En la práctica, utiliza el método __new__() cuando desea modificar el 
objeto en el momento de la instancia.
"""


class Person:
    def __new__(cls, firstname: str, lastname: str):
        self = object.__new__(cls)
        return self

    def __init__(self, name: str) -> None:
        print(f'Initializing the person2 object...')
        self.name = name

    def __str__(self) -> str:
        return f'Person2{self.__dict__}'


class SquareNumber(int):
    def __new__(cls, value: int):
        # el __new__ de la clase padre invoca al __init__
        return super().__new__(cls, value**2)


def show_example_01():
    p = Person(name='Person1')
    print(p)


def show_example_02():
    x = SquareNumber(3)
    print(x, isinstance(x, int))


def main():
    show_example_01()
    show_example_02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue. . .')
