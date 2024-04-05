"""ORDENAMIENTO DE LISTAS

1. sort
Método de las listas que ordena de acuerdo a un key, los
elementos. Este método cambia el estado del la lista ordenándola.

2. sorted
Método build-in en python que recibe un iterables de objetos
comparables de alguna forma, y retorna una lista de los elementos
ordenados.
"""
from typing import Tuple
import random


def showExample01():
    items = [random.randint(1, 100) for _ in range(10)]
    print(f'items: {items}')
    items.sort()
    print(f'items: {items}')

    items.sort(reverse=True)
    print(f'items: {items}')


def showExample02():
    items = [
        ('Google', 2019, 134.81),
        ('Apple', 2019, 260.2),
        ('Facebook', 2019, 70.7),
    ]

    ordenados = sorted(items, key=lambda item: item[0])
    print(f'original items: {items}')
    print(f'items         : {ordenados}')


def showExample03():
    items = [
        ('Google', 2019, 134.81),
        ('Apple', 2019, 260.2),
        ('Facebook', 2019, 70.7),
    ]

    print(f'original: {items}')

    def helperFromName(companyData: Tuple[str, int, float]) -> str:
        return companyData[0]

    def helperFromYear(companyData: Tuple[str, int, float]) -> int:
        return companyData[1]

    items.sort(key=lambda company: company[2])
    print(f'Ordenado por monto: {items}')

    items.sort(key=helperFromName)
    print(f'Ordenado por nombre: {items}')

    items.sort(key=helperFromYear)
    print(f'Ordenado por año  : {items}')


def main():
    showExample01()
    showExample02()
    showExample03()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
