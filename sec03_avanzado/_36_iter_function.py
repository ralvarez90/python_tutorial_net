"""FUNCIÓN iter

Retorna el correspondiente iterador del objeto que
recibe como argumento.

Esta clase en realidad, requiere que su argumento sea
un objeto iterable o una secuencia.

Primero buscará el método __iter__ del objeto argumento
y si no existe buscará el __getitem__.
"""


def showExample01():

    class Counter:
        def __init__(self) -> None:
            self.__current = 0

    # lanza excepción
    counter = Counter()
    # iterator = iter(counter)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
