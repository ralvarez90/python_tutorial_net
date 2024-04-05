"""UNPACKING TUPLES

Podemos desempacar elementos de colecciones empleando *
en diferentes contextos. Es practicamente lo mismo que
el unpacking con listas.

Si una función como parámetros tiene un nobre de variable
precedido con un *, entonces dicho parámetro es una tupla 
dentro del cuerpo de la función.
"""

# generamos alias
number = int | float | complex


def obtenerCabecera(tpl: tuple):
    head, *_ = tpl
    return head


def obtenerCola(tpl: tuple) -> tuple:
    _, *tail = tpl
    return tuple(tail)


def obtenerSuma(*numbers) -> number:
    return sum(numbers)


def showExample01():
    someTpl = (1, 2, 3)
    head = obtenerCabecera(someTpl)
    tail = obtenerCola(someTpl)
    print(f'head: {head}')
    print(f'tail: {tail}')


def showExample02():
    firstIntNumbers = [i for i in range(1, 5)]
    print(f'1+2+...+100 -> {obtenerSuma(*firstIntNumbers)}')
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
