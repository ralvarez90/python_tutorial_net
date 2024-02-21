"""UNPACKING LIST

Podemos extraer elementos de una lista y asignarlos a nombres
de variables.

Podemos desempacar los elementos de una lista empleando el
operador *.

Podemos extraer exactamente los elementos de una lista (o tupla)
asignando cada uno de sus elementos internos de la forma
v1, v2, ..., vn = [e1, e2, ..., en]
"""
from typing import List


def getHead(items: List):
    head, *_ = items
    print(f'head: {head}')


def getTail(items: List):
    _, *tail = items
    print(f'tail: {tail}')


def exampleUnpackingListV1():
    colors = 'red blue green'.split()
    print(f'colors: {colors}')
    r, g, b = colors
    print(r, g, b)


def exampleUnpackingListV2():
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    getHead(items)
    getTail(items)


def main():
    exampleUnpackingListV1()
    exampleUnpackingListV2()


if __name__ == '__main__':

    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
