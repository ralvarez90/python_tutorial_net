"""DICCIONARIOS POR COMPRENSIÓN

Podemos generar diccionarios por medio de expresiónes
y rangos, al igual que las list comprehension.

De forma general la sintaxis es:
{key:value for (key, value) in dict.items() if condition}
"""


def showExample01():
    stocks = {
        'APLN': 121,
        'AMZN': 3389,
        'MSFT': 4492,
        'LVG': 2232,
    }

    # version sin dict comprehension
    # for k, v in stoks.items():
    #     stoks[k] = int(v*1.20)

    print(f'finalStock: {stocks}')

    # con expresión y k:v a asugbar
    newStock = {k: int(v*1.2) for (k, v) in stocks.items()}
    print(f'newStock:   {newStock}')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
