"""LOOP RANGE

1. Clase range

Extiende de una Sequence[int] por lo que es una secuencia de enteros

Se suele emplear en bucles junto con la sentencia for. Genera los elementos
de forma dinámica bajo demanda, por lo que es un generador.

Esta clase puede tener hasta 3 parámetros, que indica el inicio, fin y el
step a utilizar.
"""


def showExample01():
    total = 0
    for n in range(1, int(input('>>> ')) + 1):
        total += n
    print(f'Total: {total}')


def showExample02():
    total = 0
    for n in range(1, int(input('>>> '))+1):
        total += n
    else:
        print(f'Total: {total}')


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
