"""FILTER FUNCTIONS

A veces, es necesario iterar sobre los elementos de una lista y 
seleccionar algunos de ellos según criterios específicos.
"""


def show_example_01():
    scores = [70, 60, 80, 80, 50]
    filtered = list(filter(lambda score: score >= 70, scores))
    print(f'scores: {scores}')
    print(f'filter: {filtered}')


def show_example_02():
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
    show_example_01()
    show_example_02()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
