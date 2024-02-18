"""FILTER FUNCTIONS

A veces, es necesario iterar sobre los elementos de una lista y 
seleccionar algunos de ellos según criterios específicos.
"""


def filterExample():
    scores = [70, 60, 80, 80, 50]
    filtered = list(filter(lambda score: score >= 70, scores))
    print(f'scores: {scores}')
    print(f'filter: {filtered}')


def otherFilterExample():
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
        ['Mexico', 128649565]
    ]

    populated = list(filter(lambda c: c[1] > 3_000_000, countries))
    print(f'populated: {populated}')


if __name__ == '__main__':

    # filter1
    filterExample()

    # filter 2
    otherFilterExample()

    # end application
    input('\nPress any key to continue . . . ')
