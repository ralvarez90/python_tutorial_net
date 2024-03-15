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


def show_example_01():
    colors = 'red blue green'.split()
    print(f'colors: {colors}')
    r, g, b = colors
    print(r, g, b)


def show_example_02():
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    get_head(items)
    get_tail(items)


def main():
    show_example_01()
    show_example_02()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
