"""LOOP RANGE

1. Clase range

Extiende de una Sequence[int] por lo que es una secuencia de enteros

Se suele emplear en bucles junto con la sentencia for. Genera los elementos
de forma dinámica bajo demanda, por lo que es un generador.

Esta clase puede tener hasta 3 parámetros, que indica el inicio, fin y el
step a utilizar.
"""


def range_example():
    total = 0
    for n in range(1, int(input('>>> '))+1):
        total += n
    print(f'total: {total}')


if __name__ == '__main__':

    # ejemplo de rango
    range_example()

    # end application
    input('\nPress any key to continue . . . ')
