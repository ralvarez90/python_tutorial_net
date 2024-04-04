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


def runtime_type(obj: object) -> str:
    return str(type(obj))[8:-2]


def show_example_01():
    # ejemplo 1, entero
    some_number: int = 128
    print(f'{some_number} with type: {runtime_type(some_number)}')
    print(f'sys.getsizeof(', some_number, '): ',
          sys.getsizeof(some_number), '\n')

    # ejemplo 2, entero más largo
    other_integer = 1_000_000_000
    print(other_integer, 'with size:', sys.getsizeof(other_integer), ' bytes')

    # ejemplo 3, otro entero
    other_integer = 2**32
    print('sys.getsizeof(', other_integer,
          'with size:', sys.getsizeof(other_integer))


def main():
    show_example_01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue. . .')
