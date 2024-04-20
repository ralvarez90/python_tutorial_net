"""SLICING A PROFUNDIDAD

El slicing solo funciona en objetos tipo Sequence.
"""


def showExample01():
    colors = ['red', 'green', 'blue', 'orange']

    # creamos objeto rebanada
    rebanadaTail = slice(1, len(colors)-1)
    print(f'colors      -> {colors}')
    print(f'colors[1:3] -> ')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
