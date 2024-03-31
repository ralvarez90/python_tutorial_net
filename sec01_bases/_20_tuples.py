"""TUPLAS

Son secuencias iterables, indexables e inmutables. Son
más eficientes que las listas.

Al igual que las listas y otras colecciones, podemos
crear tuplas a partir de otros iterables.
"""


def runtime_type(obj: object) -> str:
    return str(type(obj))[8:-2]


def show_example_01():
    tpl = tuple([i for i in range(1, 11)])
    print(f'tuple1: {tpl}, with type: {runtime_type(tpl)}')


def main():
    show_example_01()
    print(runtime_type((1,)))


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
