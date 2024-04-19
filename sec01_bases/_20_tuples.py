"""TUPLAS

Son secuencias iterables, indexables e inmutables. Son
más eficientes que las listas.

Al igual que las listas y otras colecciones, podemos
crear tuplas a partir de otros iterables.
"""


def runtimeType(obj: object) -> str:
    return str(type(obj))[8:-2]


def showExample01():
    tpl1 = tuple([i for i in range(1, 11)])
    print(f'tuple1: {tpl1}, with type: {runtimeType(tpl1)}')

    tpl2 = 1,
    print(f'tuple2: {tpl2}, with type: {runtimeType(tpl2)}')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
