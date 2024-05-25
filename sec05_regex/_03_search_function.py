"""MÉTODOS search, match y fullmatch

1. search
Busca un patrón dentro deun string, si se encuentra retorna un
objeto Match y si no un None.

El objeto Match tiene diversos métodos de utilidad:
- group
    Retorna el string matcheado
- start
    Retorna la posicion de inicio del string matcheado
- end
    Retorna la posición del fin del string matcheado
span
    Retorna una tupla con la posición inicial y final de string matcheado
"""
import re


def showExample01():
    print('Example 01. Match object and re.search method.')

    # string to search
    s = 'Python 3.10 was released on October 04, 2021.'

    # matching all two digits numbers
    pattern = r'\d{2}'
    matchResult = re.search(pattern, s)
    print('matchResult -> %s' % (matchResult))
    print('With type   -> %s' % (type(matchResult)))
    print(f'matchResult.group() -> {matchResult.group()}')
    print(f'matchResult.start() -> {matchResult.start()}')
    print(f'matchResult.end()   -> {matchResult.end()}')
    print(f'matchResult.span()  -> {matchResult.span()}')
    print()


def showExample02():
    print('Example 02. Other Match object example')

    # string to search
    s = 'Python 3.10 was released on October 04, 2021'
    result = re.search(r'\d', s)

    def showMatchInfo(m: re.Match) -> None:
        print(f'Matched string   : {result.group()}')
        print(f'Starting position: {result.start()}')
        print(f'Ending position  : {result.end()}')
        print(f'Positions        : {result.span()}')

    showMatchInfo(m=result)


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
