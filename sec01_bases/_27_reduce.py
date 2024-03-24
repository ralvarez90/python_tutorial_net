"""FUNCIÓN REDUCE

Permite obtener un valor concreto a partir de una secuencia.
"""
import functools


def showExample01():
    numbers = [1, 2, 3, 4, 5]
    total = functools.reduce(lambda x, y: x + y, numbers, 0)
    print(f'sum1: {total}')
    print(f'sum2: {sum(numbers)}')


def showExample02():
    def suma(a: int | float, b: int | float) -> int | float:
        print(f'a={a}, b={b}, {a}+{b} = {a + b}')
        return a + b

    scores = [75, 65, 80, 95, 50]
    total = functools.reduce(suma, scores)
    print(f'Total: {total}')


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
