"""SLICING A PROFUNDIDAD

El slicing solo funciona en objetos tipo Sequence. Puede emplearse
tanto en secuencias mutables como inmutables, esto gracias a que
no cambian el estado de las secuencias.

Se emplean dos sintaxis de uso:
- seq[inicio:fin:step]
- slice(inicio, fin, step)

donde inicio, fin y step son enteros, con la posibilidad de ser
positivos o negativas.

Método indices de slices
Dato un slices definido, podemos invocar su método indices que
nos permite obtener índices válidos dentro de un rango especificado
por el slice.
"""
from typing import Sequence, TypeVar


# definición de genérico
T = TypeVar('T')


def showExample01():
    colors = ['red', 'green', 'blue', 'orange']

    # creamos objeto rebanada
    rebanadaTail = slice(1, len(colors)-1)
    print(f'colors              -> {colors}')
    print(f'colors[1:3]         -> {colors[1:len(colors)-1]}')
    print(f'colors[slice(1, 3)] -> {colors[rebanadaTail]}')


def showExample02():
    topic: str = 'Python slicing'

    print(f'topic               -> {topic}')
    print(f'topic[0:6]          -> {topic[0:6]}')
    print(f'topic[0:100]        -> {topic[0:100]}')
    print(f'topic[1:]           -> {topic[1:]}')
    print(f'topic[::-1].lower() -> {topic[::-1].lower()}')


def showExample03():
    message = 'Hello World in Python!'
    print(f'message: "{message}"')

    def getLastItem(seq: Sequence[T]) -> T | None:
        return seq[-1] if len(seq) != 0 else None

    print(f'getLastItem(message) -> {getLastItem(message)}')
    print(f'getLastItem([])      -> {getLastItem([])}')


def showExample04():
    colors = ['red', 'green', 'blue', 'orange']
    s = slice(0, 4, 2)
    t = s.indices(len(colors))
    for index in range(*t):
        print(f'colors[{index}] -> {colors[index]}')


def main():
    showExample01()
    showExample02()
    showExample03()
    showExample04()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
