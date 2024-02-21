"""UNPACKING TUPLES

Podemos desempacar elementos de colecciones empleando *
en diferentes contextos. Es practicamente lo mismo que
el unpacking con listas
"""

# generamos alias
number = int | float


def obtenerHead(tpl: tuple):
    head, *_ = tpl
    return head


def obtenerTail(tpl: tuple) -> tuple:
    _, *tail = tpl
    return tuple(tail)


def obtenerSuma(*numbers) -> number:
    return sum(numbers)


def exampleUnpacking1():
    someTpl = (1, 2, 3)
    head = obtenerHead(someTpl)
    tail = obtenerTail(someTpl)
    print(f'head: {head}')
    print(f'tail: {tail}')


def exampleUnpacking2():
    primeros_numeros = [i for i in range(1, 5)]
    print(f'1+2+...+100 -> {obtenerSuma(*primeros_numeros)}')
    oddNumbers = (1, 3, 5)
    evenNumbers = (2, 4, 6)
    numbers = (*oddNumbers, *evenNumbers)
    print(f'numbers: {numbers}')


def main():
    exampleUnpacking1()
    exampleUnpacking2()


if __name__ == '__main__':

    # run application
    main()

    # end message
    input('\nPress any key to continue . . .')
