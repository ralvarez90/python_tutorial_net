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


def show_example_01():
    items = [random.randint(1, 100) for _ in range(10)]
    print(f'items: {items}')
    items.sort()
    print(f'items: {items}')

    items.sort(reverse=True)
    print(f'items: {items}')


def show_example_02():
    items = [
        ('Google', 2019, 134.81),
        ('Apple', 2019, 260.2),
        ('Facebook', 2019, 70.7),
    ]

    ordenados = sorted(items, key=lambda item: item[0])
    print(f'original items: {items}')
    print(f'items         : {ordenados}')


def show_example_03():
    items = [
        ('Google', 2019, 134.81),
        ('Apple', 2019, 260.2),
        ('Facebook', 2019, 70.7),
    ]

    print(f'original: {items}')

    def __fromName(compania_data: Tuple[str, int, float]) -> str:
        return compania_data[0]

    def __fromYear(compania_data: Tuple[str, int, float]) -> int:
        return compania_data[1]

    items.sort(key=lambda company: company[2])
    print(f'Ordenado por monto: {items}')

    items.sort(key=__fromName)
    print(f'Ordenado por nombre: {items}')

    items.sort(key=__fromYear)
    print(f'Ordenado por año  : {items}')


def main():
    show_example_01()
    show_example_02()
    show_example_03()


if __name__ == '__main__':
    # run application
    main()

    # end messages
    input('\nPress any key to continue . . . ')
