"""ENTEROS

Son instancias de la clase int, representan números enteros. A
diferencia de otros lenguajes de programación donde los enteros
se almacenan en un tamaño fijo de bits, en python los enteros
se pueden almacenar en 8, 16, 32, 64, 128 bits, etc...

1. sys.getsizeof
Empleamos la función getsizeof del módulo sys para regresar el
número de bytes que ocupa en memoria un objeto.
"""
import sys


def runtimeType(obj: object) -> str:
    return str(type(obj))[8:-2]


def showExample01():
    someNumber: int = 128
    print(f'{someNumber} with type: {runtimeType(someNumber)}')
    print(f'sys.getsizeof(', someNumber, '): ', sys.getsizeof(someNumber), '\n')

    # ejemplo 2, entero más largo
    otherNumber = 1_000_000_000
    print(otherNumber, 'with size:', sys.getsizeof(otherNumber), ' bytes')

    # ejemplo 3, otro entero
    otherNumber = 2**32
    print('sys.getsizeof(', otherNumber, 'with size:', sys.getsizeof(otherNumber))


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue. . .')
