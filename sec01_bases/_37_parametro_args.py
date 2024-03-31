"""PARÁMETRO *ARGS

Podemos tener funciones que reciban un número variable de argumetos. Estos se almacenan en
una tupla que puede ser utilizada dentro del cuerpo de la función. Por convensión a este
parámetro se le nombre args. Esto también se puede utilizar para desempacar tuplas.
"""

# alias numérico
number = int | float


def runtime_type(obj: object) -> str:
    return str(type(object))[8:-2]


def obtener_suma(x: number, y: number, *args: tuple[number]) -> number:
    return x+y+sum(args)


def show_example_01():
    x, y, *_ = 1, 2, 3, 4, 5, 6, 7, 8, 9
    print(f'x: {x}, y: {y}, otros: {_}')


def show_example_02():
    print(f'1 + 2 + ... + 10: {obtener_suma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')


def main():
    show_example_01()
    show_example_02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
