"""SHORT LIST

1. sort
Método de las listas que ordena de acuerdo a un key, los
elementos.

2. sorted
Método build-in en python que recibe un iterables de objetos
comparables de alguna forma, y retorna una lista de los elementos
ordenados.

"""
import random
from typing import Tuple


def showShortExample():
    items = [random.randint(1, 100) for _ in range(10)]
    print(f'items: {items}')

    # sorted
    items.sort()
    print(f'items: {items}')

    items.sort(reverse=True)
    print(f'items: {items}')


def showShortedExample():
    items = [
        ('Google', 2019, 134.81),
        ('Apple', 2019, 260.2),
        ('Facebook', 2019, 70.7),
    ]

    ordenados = sorted(items, key=lambda item: item[0])
    print(f'original items: {items}')
    print(f'items         : {ordenados}')


def sortListOftuples():
    items = [
        ('Google', 2019, 134.81),
        ('Apple', 2019, 260.2),
        ('Facebook', 2019, 70.7),
    ]

    print(f'original: {items}')

    # sorted by name
    def __fromName(company: Tuple[str, int, float]) -> float:
        return company[0]

    def __fromYear(company: Tuple[str, int, float]) -> float:
        return company[1]

    items.sort(key=lambda company: company[2])
    print(f'Ordenado por monto: {items}')

    items.sort(key=__fromName)
    print(f'Ordenado por nombre: {items}')

    items.sort(key=__fromYear)
    print(f'Ordenado por año  : {items}')


if __name__ == '__main__':

    # sort
    showShortExample()

    # short list with inner tuples
    sortListOftuples()

    # sorted
    showShortedExample()

    # end application
    input('\nPress any key to continue . . . ')
