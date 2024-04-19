"""FILTER FUNCTIONS

A veces, es necesario iterar sobre los elementos de una lista y 
seleccionar algunos de ellos según criterios específicos.

La función asignada al parámetro de filter recibe un
valor y retorna un booleano.
"""


def showExample01():
    scores = [70, 60, 80, 80, 50]
    filtered = list(filter(lambda score: score >= 70, scores))
    print(f'scores: {scores}')
    print(f'filter: {filtered}')


def showExample02():
    countries = [
        ['China', 1394015977],
        ['United States', 329877505],
        ['India', 1326093247],
        ['Indonesia', 267026366],
        ['Bangladesh', 162650853],
        ['Pakistan', 233500636],
        ['Nigeria', 214028302],
        ['Brazil', 21171597],
        ['Russia', 141722205],
        ['Mexico', 128649565],
    ]

    print('Filtered countries:')
    populated = list(filter(lambda country: country[1] > 3_000_000, countries))
    for c in populated:
        print(c)


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
