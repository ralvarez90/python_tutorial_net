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


def get_head(items: List):
    head, *_ = items
    print(f'head: {head}')


def get_tail(items: List):
    _, *tail = items
    print(f'tail: {tail}')


def example_unpacking_list_v1():
    colors = 'red blue green'.split()
    print(f'colors: {colors}')
    r, g, b = colors
    print(r, g, b)


def example_unpacking_list_v2():
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    get_head(items)
    get_tail(items)


def main():
    # ejemplo 1, unpacking
    example_unpacking_list_v1()

    # ejemplo 2, unpacking
    example_unpacking_list_v2()


if __name__ == '__main__':

    # run application
    main()

    # end application
    input('\nPress any key to continue . . . ')
