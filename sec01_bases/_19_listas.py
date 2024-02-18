"""LISTAS

Son secuencias de elementos indexados, iterables y de estado
mutables. Pueden ser unidimensional o multidimensionales.

Podemos acceder a cada elemento por medio de los índices, y
podemos eliminarlos empleando el operador del.

Tenemos disponibles los siguientes métodos pop, remove, insert,
append.
"""

coordinates = [
    [0, 0],
    [100, 100],
    [200, 200],
]

if __name__ == '__main__':

    # iterate
    for i in range(len(coordinates)):
        for j in range(len(coordinates[i])):
            print(f'coordinates[{i}][{j}] -> {coordinates[i][j]}')
