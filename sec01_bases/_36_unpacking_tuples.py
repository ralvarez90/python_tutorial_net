"""UNPACKING TUPLES

Podemos desempacar elementos de colecciones empleando *
en diferentes contextos. Es practicamente lo mismo que
el unpacking con listas
"""

# generamos alias
number = int | float


def obtener_head(tpl: tuple):
    head, *_ = tpl
    return head


def obtener_tail(tpl: tuple) -> tuple:
    _, *tail = tpl
    return tuple(tail)


def obtener_suma(*numbers) -> number:
    return sum(numbers)


def show_example_1():
    someTpl = (1, 2, 3)
    head = obtener_head(someTpl)
    tail = obtener_tail(someTpl)
    print(f'head: {head}')
    print(f'tail: {tail}')


def show_example_2():
    primeros_numeros = [i for i in range(1, 5)]
    print(f'1+2+...+100 -> {obtener_suma(*primeros_numeros)}')
    oddNumbers = (1, 3, 5)
    evenNumbers = (2, 4, 6)
    numbers = (*oddNumbers, *evenNumbers)
    print(f'numbers: {numbers}')


def main():
    show_example_1()
    show_example_2()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . .')
