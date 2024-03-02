"""DICCIONARIOS POR COMPRENSIÓN

Podemos generar diccionarios por medio de expresiónes
y rangos, al igual que las list comprehension.

De forma general la sintaxis es:
{key:value for (key, value) in dict.items() if condition}
"""
from copy import deepcopy


def show_example_1():
    stoks = {
        'APLN': 121,
        'AMZN': 3389,
        'MSFT': 4492,
        'LVG': 2232,
    }

    # version sin dict comprehension
    # for k, v in stoks.items():
    #     stoks[k] = int(v*1.20)

    print(f'finalStock: {stoks}')

    # con expresipn
    newStock = {k: int(v*1.2) for (k, v) in stoks.items()}
    print(f'newStock:   {newStock}')


def main():
    show_example_1()


if __name__ == '__main__':
    # run application
    main()

    # end amessage
    input('\nPress any key to continue . . . ')
