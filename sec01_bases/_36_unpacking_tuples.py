"""UNPACKING TUPLES

Podemos desempacar elementos de colecciones empleando *
en diferentes contextos.
"""

number = int | float


def getHead(tpl: tuple):
    head, *_ = tpl
    return head


def getTail(tpl: tuple) -> tuple:
    _, *tail = tpl
    return tuple(tail)


def getSum(*numbers) -> number:
    return sum(numbers)


def exampleUnpacking1():
    someTuple = (1, 2, 3)
    head = getHead(someTuple)
    tail = getTail(someTuple)
    print(f'head: {head}')
    print(f'tail: {tail}')


def exampleUnpacking2():
    primerosNumeros = [i for i in range(1, 5)]
    print(f'1+2+...+100 -> {getSum(*primerosNumeros)}')
    oddNumbers = (1, 3, 5)
    evenNumbers = (2, 4, 6)
    numbers = (*oddNumbers, *evenNumbers)
    print(f'numbers: {numbers}')


if __name__ == '__main__':

    # run examples
    exampleUnpacking1()
    exampleUnpacking2()

    # end application
    input('\nPress any key to continue . . .')
