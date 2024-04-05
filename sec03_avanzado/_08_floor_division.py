"""DIVISIÓN ENTERA

En python el operador de división es exacto, mientras que
el operador // retorna la división entera.

1. Función floor
Recibe cualquier número y retorna la parte entera.
"""
import math


def showExample01():
    # división entera
    a = 3
    b = 2
    print(f'{a}  / {b} -> {a/b}')
    print(f'{a} // {b} -> {a//b}')

    # función piso
    number = 1
    for _ in range(50):
        number += 0.1
        print(f'math.floor({number}) -> {math.floor(number)}')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
