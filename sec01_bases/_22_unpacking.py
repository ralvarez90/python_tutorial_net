"""UNPACKING LIST

Podemos extraer elementos de una lista y asignarlos a nombres
de variables.

Podemos desempacar los elementos de una lsita empleando el
operador *.
"""
from typing import List


def getHead(items: List):
    head, *_ = items
    print(f'head: {head}')


def getTail(items: List):
    _, *tails = items
    print(f'tails: {tails}')


def unpackingListExample():
    colors = 'red blue green'.split()
    print(f'colors: {colors}')
    r, g, b = colors
    print(r, g, b)


def unpackingListExample2():
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    getHead(items)
    getTail(items)


if __name__ == '__main__':

    # unpacking
    unpackingListExample()

    # unpacking v2
    unpackingListExample2()

    # end application
    input('\nPress any key to continue . . . ')
