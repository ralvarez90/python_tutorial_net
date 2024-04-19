"""LISTAS

1. Listas
Son secuencias de elementos indexados, iterables y de estado
mutables. Pueden ser unidimensional o multidimensionales.

Podemos acceder a cada elemento por medio de los índices, y
podemos eliminarlos empleando el operador del.

Tenemos disponibles los siguientes métodos pop, remove, insert,
append.

2. Slicing
Podemos obtener sublistas a partir de otras empleando la notación 
slicing. La notación es
sublista = lista[inicio:fin:step]
"""


def obtenerCola(lst: list) -> list:
    """Retoran la cola de una lista.
    >>> obtenerCola([1, 2, 3])
    [2, 3]

    >>> obtenerCola([])
    []

    >>> obtenerCola([True])
    [True]
    """
    return lst[0] if len(lst) == 1 else lst[1:]


def showExample01():
    coordenadas = [
        [0, 0],
        [100, 100],
        [200, 200],
    ]

    # iteramos con un for anidado
    for i in range(len(coordenadas)):
        for j in range(len(coordenadas[i])):
            print(f'coordinates[{i}][{j}] -> {coordenadas[i][j]}')


def showExample02():
    colors = [
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'indigo',
        'violet',
    ]

    print(f'colors: {colors}')
    subColores = colors[1:4]
    print(f'colors[1:4] -> {subColores}')


def showExample03():
    someList = [i for i in range(1, 1)]
    print(f'some_lst: {someList}')
    print(f'tail of  : {obtenerCola([1])}')


def main():
    showExample01()
    showExample02()
    showExample03()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
