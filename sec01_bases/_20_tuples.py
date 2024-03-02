"""TUPLAS

Son secuencias iterbales e indexables inmutables. Son
más eficientes que las listas.

Al igual que las listas y otras colecciones, podemos
crear tuplas a partir de otros iterables.
"""


def runtime_type(obj: object) -> str:
    return str(type(obj))[8:-2]


def show_example():
    tpl = tuple([i for i in range(1, 11)])
    print(f'tuple1: {tpl}, with type: {runtime_type(tpl)}')


def main():
    show_example()
    print(runtime_type((1,)))


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
