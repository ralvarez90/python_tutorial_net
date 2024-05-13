"""GENERADORES POR EXPRESIÓN

Así como podemos generar listas por expresión, podemos crear
generadores por expresión.

Recordemos que una función que emplea yield en su cuerpo retorna un
generador y como los generadores son iteradores entonces se pueden
emplear junto con el ciclo for. Ver ejemplo 1.

En el ejemplo dos creamos el mismo generador por expressión, que se
asemeja mucho a los lit comprehension en términos de sintaxis.

Una lista por comprensión retorna un iterable, sin embergo un generator
expression retorna un lazy iterator.
"""
from math import sqrt


def showExample01():
    print('EXAMPLE 01. Use generator by function.')

    def getSquares(length: int):
        for n in range(length):
            yield n**2

    for square in getSquares(length=10):
        print(f'{int(sqrt(square))}^2 -> {square}')

    print()


def showExample02():
    print('EXAMPLE 02. Use expression generator')

    # create generator
    squares = (n**2 for n in range(10))
    for s in squares:
        print(f'{int(sqrt(s))}^2 -> {s}')

    print()


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
