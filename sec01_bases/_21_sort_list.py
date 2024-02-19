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


def example_sort_v1():
    items = [random.randint(1, 100) for _ in range(10)]
    print(f'items: {items}')
    items.sort()
    print(f'items: {items}')

    items.sort(reverse=True)
    print(f'items: {items}')


def example_sort_v2():
    items = [
        ('Google', 2019, 134.81),
        ('Apple', 2019, 260.2),
        ('Facebook', 2019, 70.7),
    ]

    ordenados = sorted(items, key=lambda item: item[0])
    print(f'original items: {items}')
    print(f'items         : {ordenados}')


def example_sort_tuplas():
    items = [
        ('Google', 2019, 134.81),
        ('Apple', 2019, 260.2),
        ('Facebook', 2019, 70.7),
    ]

    print(f'original: {items}')

    def __desde_nombre(compania_data: Tuple[str, int, float]) -> str:
        return compania_data[0]

    def __desde_anio(compania_data: Tuple[str, int, float]) -> int:
        return compania_data[1]

    items.sort(key=lambda company: company[2])
    print(f'Ordenado por monto: {items}')

    items.sort(key=__desde_nombre)
    print(f'Ordenado por nombre: {items}')

    items.sort(key=__desde_anio)
    print(f'Ordenado por año  : {items}')


def main():
    # ejemplos
    example_sort_v1()
    example_sort_v2()

    # ordenamiento de tuplas, usando funciones
    # interans como criterio de ordenamiento
    example_sort_tuplas()


if __name__ == '__main__':

    # run application
    main()

    # end messages
    input('\nPress any key to continue . . . ')
