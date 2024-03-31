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


def obtener_cola(lst: list) -> list:
    """Retoran la cola de una lista.
    >>> obtener_cola([1, 2, 3])
    [2, 3]

    >>> obtener_cola([])
    []

    >>> obtener_cola([True])
    [True]
    """
    return lst[0] if len(lst) == 1 else lst[1:]


def ahow_example_01():
    coordenadas = [
        [0, 0],
        [100, 100],
        [200, 200],
    ]

    # iteramos con un for anidado
    for i in range(len(coordenadas)):
        for j in range(len(coordenadas[i])):
            print(f'coordinates[{i}][{j}] -> {coordenadas[i][j]}')


def show_example_02():
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
    sub_colors = colors[1:4]
    print(f'colors[1:4] -> {sub_colors}')


def show_example_03():
    some_lst = [i for i in range(1, 1)]
    print(f'some_lst: {some_lst}')
    print(f'tail of  : {obtener_cola([1])}')


def main():
    ahow_example_01()
    show_example_02()
    show_example_03()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
