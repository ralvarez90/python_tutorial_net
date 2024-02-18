"""PARÁMETRO *ARGS

Podemos tener funciones que reciban un número
variable de argumetos. Estos se almacenan en
una tupla que puede ser utilizada dentro del
cuerpo de la función. Por convensión a este
parámetro se le nombre args. Esto también se puede
utilizar para desempacar tuplas.
"""

number = int | float


def runtimeType(obj: object) -> str:
    return str(type(object))[8:-2]


def getSum(x: number, y: number, *args: tuple[number]) -> number:
    return x+y+sum(args)


def unpackingExample1():
    x, y, *_ = 1, 2, 3, 4, 5, 6, 7, 8, 9
    print(f'x: {x}, y: {y}, otros: {_}')


def unpackingExample2():
    print(f'1 + 2 + ... + 10: {getSum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')


if __name__ == '__main__':

    # run examples
    unpackingExample1()
    unpackingExample2()

    # end application
    input('\nPress any key to continue . . .')
