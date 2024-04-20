"""LISTAS POR COMPRENSIÓN

Tanto la función for loop como map() pueden ayudarle a crear una 
nueva lista basada en una existente. Las listas por comprensión
(comprehension list) son otra alternativa para generar secuencias
de valores dinámicas.
"""


def showExample01():
    numbers = [1, 2, 3, 4, 5]
    squares = [n ** 2 for n in numbers]
    print(f'numbers: {numbers}')
    print(f'squares: {squares}')


def showExample02():
    mountains = (
        ['Malaku', 8485],
        ['Lhotse', 8516],
        ['Kanchendzonga', 8586],
        ['K2', 8611],
        ['Everest', 8848],
    )
    higuests1 = list(filter(lambda m: m[1] > 8600, mountains))
    higuests2 = [m for m in mountains if m[1] > 8600]
    print(f'higuest1: {higuests1}')
    print(f'higuest2: {higuests2}')


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
