"""ORDENAMIENTO DE LISTAS

1. sort
Método de las listas que ordena de acuerdo a un key, los
elementos. Este método cambia el estado del la lista ordenándola.

El parámetro de la función asignada en key recibe un solo
argumento.

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

    def _fromName(companyData: Tuple[str, int, float]) -> str:
        return companyData[0]

    def _fromYear(companyData: Tuple[str, int, float]) -> int:
        return companyData[1]

    # se ordena por monto
    items.sort(key=lambda company: company[2])
    print(f'Ordenado por monto: {items}')

    # se ordena por nombre
    items.sort(key=_fromName)
    print(f'Ordenado por nombre: {items}')

    # se ordena por año
    items.sort(key=_fromYear)
    print(f'Ordenado por año  : {items}')


def main():
    showExample01()
    showExample02()
    showExample03()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
