"""FUNCIÓN REDUCE

Permite obtener un valor concreto a partir de una secuencia.
"""
from functools import reduce


def reduceExample():
    """Se muestra como usar reduce para obtener la suma de
    los elementos dentro de una lista.
    """
    someNumbers = [1, 2, 3, 4, 5]
    total = reduce(lambda x, y: x+y, someNumbers, 0)
    print(f'sum1: {total}')
    print(f'sum2: {sum(someNumbers)}')


if __name__ == '__main__':

    # reduce
    reduceExample()

    # end application
    input('\nPress any key to continue . . . ')
