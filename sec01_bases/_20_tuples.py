"""TUPLAS

Son secuencias iterbales e indexables inmutables. Son
más eficientes que las listas.

Al igual que las listas y otras colecciones, podemos
crear tuplas a partir de otros iterables.
"""


def runtime_type(obj: object) -> str:
    return str(type(obj))[8:-2]


def ejemplo_tuplas():
    tpl = tuple([i for i in range(1, 11)])
    print(f'tuple1: {tpl}, with type: {runtime_type(tpl)}')


if __name__ == '__main__':

    # ejemplo 1
    ejemplo_tuplas()

    # end message
    input('\nPress any key to continue . . . ')
