"""PARTIAL FUNCTIONS

La función partial del módulo functools retorna un nuevo dato que e
s invocable (callable). Cuando invoca el objeto partial, python 
invoca la función que recibe como primer argumento con los 
argumentos posicionales. Es decir es una un partial es una función 
que usa parcialmente otra.
"""
from functools import partial

# alias
number = int | float


def multiplicar(a: number, b: number) -> number:
    return a*b


def partialExample():
    double = partial(multiplicar, b=2)
    print(f'Doble de 10: {double(10)}')


def main():
    partialExample()


if __name__ == '__main__':

    # run application
    main()

    # end application
    input('\nPress any key to continue . . . ')
