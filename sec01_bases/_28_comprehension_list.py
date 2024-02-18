"""LISTAS POR COMPRENSIÓN

Tanto la función for loop como map() pueden ayudarle a crear una 
nueva lista basada en una existente. Pero el código no es realmente c
onciso ni bonito.

Las list comprehension nos permite generar listas a partir de
expresiones. Se pueden agregar condiciones.
"""


def showExampleV1():
    numbers = [1, 2, 3, 4, 5]
    squares = [n**2 for n in numbers]
    print(f'numbers: {numbers}')
    print(f'squares: {squares}')


def showExampleV2():
    mountains = (
        ['Malaku', 8485],
        ['Lhotse', 8516],
        ['Kanchendzonga', 8586],
        ['K2', 8611],
        ['Everest', 8848],
    )
    higuestsV1 = list(filter(lambda m: m[1] > 8600, mountains))
    higuestsV2 = [m for m in mountains if m[1] > 8600]
    print(f'higuestV1: {higuestsV1}')
    print(f'higuestV2: {higuestsV2}')


if __name__ == '__main__':
    showExampleV1()
    showExampleV2()
    input('\nPress any key to continue . . . ')
