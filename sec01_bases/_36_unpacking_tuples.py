"""UNPACKING TUPLES

Podemos desempacar elementos de colecciones empleando *
en diferentes contextos. Es practicamente lo mismo que
el unpacking con listas
"""

# generamos alias
number = int | float


def getHead(tpl: tuple):
    head, *_ = tpl
    return head


def getTail(tpl: tuple) -> tuple:
    _, *tail = tpl
    return tuple(tail)


def getSum(*numbers) -> number:
    return sum(numbers)


def showExample01():
    someTpl = (1, 2, 3)
    head = getHead(someTpl)
    tail = getTail(someTpl)
    print(f'head: {head}')
    print(f'tail: {tail}')


def showExample02():
    primeros_numeros = [i for i in range(1, 5)]
    print(f'1+2+...+100 -> {getSum(*primeros_numeros)}')
    oddNumbers = (1, 3, 5)
    evenNumbers = (2, 4, 6)
    numbers = (*oddNumbers, *evenNumbers)
    print(f'numbers: {numbers}')


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
