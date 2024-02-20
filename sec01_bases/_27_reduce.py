"""FUNCIÓN REDUCE

Permite obtener un valor concreto a partir de una secuencia.
"""
import functools


def reduceExample1():
    numeros = [1, 2, 3, 4, 5]
    total = functools.reduce(lambda x, y: x+y, numeros, 0)
    print(f'sum1: {total}')
    print(f'sum2: {sum(numeros)}')


def reduceExample2():
    def __suma(a: int | float, b: int | float) -> int | float:
        print(f'a={a}, b={b}, {a}+{b} = {a+b}')
        return a+b
    scores = [75, 65, 80, 95, 50]
    total = functools.reduce(__suma, scores)
    print(f'Total: {total}')


def main():
    reduceExample1()
    reduceExample2()


if __name__ == '__main__':

    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
