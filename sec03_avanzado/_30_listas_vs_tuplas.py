"""LISTAS VS TUPLAS

Ambas estructuras de datos son secuencias, la principal
diferencia entre las tuplas y las listas es que las tuplas
son inmutables.

Otra diferencia entre las tuplas y las listas es que las
tuplas nos brindan mayor eficiencia y la posibilidad de
establecer retorno de múltiples valores dentro de funciones.

Entre las principales diferencias entre las tuplas y las
listas son:
- Las tuplas ocupan menos espacio en memoria
- Copiar una tupla es más rápido que una lista. 

# todo: agregar ejemplo de timeit
"""
from sys import getsizeof
from timeit import timeit
from typing import Sequence


def showExample01():
    # tupla y lista
    sequence1 = (1, 2, 3, 4, 5)
    sequence2 = [1, 2, 3, 4, 5]

    # test de tipo
    print(f'sequence1 is a Sequence: {isinstance(sequence1, Sequence)}')
    print(f'sequence2 is a Sequence: {isinstance(sequence2, Sequence)}')

    # test de tipo
    print(f'type({sequence1}) -> {type(sequence1)}')
    print(f'type({sequence2}) -> {type(sequence2)}')


def showExample02():
    # comparación de tamaño en bytes
    sequence1 = (1, 2, 3, 4, 5)
    sequence2 = [1, 2, 3, 4, 5]
    print(f'{sequence1} has a size: {getsizeof(sequence1)} bytes.')
    print(f'{sequence2} has a size: {getsizeof(sequence2)} bytes.')


def showExample03():
    times = 1_000_000

    t1 = timeit("list(['apple', 'orange', 'banana'])", number=times)
    print(f'Time copy a list {times} times: {t1:,.2f} seg')

    t2 = timeit("tuple(('apple', 'orange', 'banana'))", number=times)
    print(f'Time copy a tuple {times} times: {t2:,.2f} seg')

    diff = '{:.0%}'.format((t2-t1)/t1)
    print(f'Difference: {diff}')


def main():
    showExample01()
    showExample02()
    showExample03()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
