"""PROPIEDAD deleter

Recordemos que el constructor de property puede recibir una función fdel que se
invoca cuando una propiedad se elimina de la forma:
del objeto.propiedad

Usando decoradores, empleamos @propiedad.deleter para asignar este comportamiento.
"""
from pprint import pprint


class Person:

    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        assert value != '', 'Name value cannot be an empty string'
        self.__name = value

    @name.deleter
    def name(self):
        print('Se invoca el deleter')
        del self.__name

    def __str__(self) -> str:
        return 'Person{name=%s}' % (self.name)


def show_example_1():
    p1 = Person(name='John Wick')
    p1.name = 'Juan Güick'
    print(p1)
    del p1.name


def main():
    show_example_1()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . .')
