"""TEST DE ITERABLES

Para determinar si un objeto es iterable puede veriricar si los métodos __iter__ o
__getitem__ están implementados. Otra alternativa es usar la función iter.
"""
from typing import Any


def showExample01():

    # test de iterabilidad
    def isIterable(obj: Any) -> bool:
        try:
            iter(obj)
        except TypeError:
            return False
        else:
            return True

    # run tests
    print(isIterable([1, 2, 3]))
    print(isIterable('Python iter'))
    print(isIterable(100))


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
