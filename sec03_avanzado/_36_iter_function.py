"""FUNCIÓN iter

Retorna el correspondiente iterador del objeto que
recibe como argumento.

Esta clase en realidad, requiere que su argumento sea
un objeto iterable o una secuencia.

Primero buscará el método __iter__ del objeto argumento
y si no existe buscará el __getitem__.
"""


def showExample01():
    print('EXAMPLE 01. Using iter method with a none sequence or iterable')

    class Counter:
        def __init__(self) -> None:
            self.__current = 0

    # lanza excepción
    counter = Counter()
    # iterator = iter(counter)


def showExample02():
    print('EXAMPLE 02. Using iter method and adding __getiten__ method in class.  Instances of'
          '\nthis classes are sequence now')

    class Counter:
        def __init__(self) -> None:
            self.current = 0

        def __getitem__(self, index: int):
            if isinstance(index, int):
                self.current += 1
                return self.current


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
