"""MÉTODOS COMUNES A LAS SECUENCIAS

1. len
Retorna el número de elementos de la secuencia.

2. in
Podemos usar el operador in de contención para verificar
si determinado objeto se encuentra o no dentro de la secuencia.

2. index
Retorna el índice de la primer ocurrencia de un objeto argumento
dentro de la secuencia. Si no existe el elemento retorna un ValueError.

Index también puede recibir un segundo parámetro indicando un índice específico
a partir de cual buscar.

3. max y min
Podemos obtener el elemento máximo y mínimo de una secuencia.
"""
import random


def showExample01():
    cities: list[str] = [
        'San Francisco',
        'New York',
        'Washinton DC',
    ]
    print(f'cities: {cities} with len -> {len(cities)}')
    print(f'CDMX in {cities} ? {"CDMX" in cities}')


def showExample02():
    numbers = [1, 4, 5, 3, 5, 7, 8, 5]
    try:
        print(numbers.index(3))
        print(numbers.index(10))
    except ValueError as e:
        print(e)

    print(numbers.index(5, 3))


def showExample03():
    numbers = [random.randint(1, 11) for _ in range(10)]
    print(f'Si numbers es igual a "{numbers}"')
    print(f'min(numbers): {min(numbers)}')
    print(f'max(numbers): {max(numbers)}')


def main():
    showExample01()
    showExample02()
    showExample03()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
