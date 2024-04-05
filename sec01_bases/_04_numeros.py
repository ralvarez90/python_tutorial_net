"""NÚMEROS

Representan valores numéricos enteros y con decimales. Exsisten
en python los tipos int, float y complex.
"""


def runtimeType(obj: object) -> str:
    return str(type(obj))[8:-2]


def showExample01():
    # int
    number = 1
    print(f'number {number} is an instance of {runtimeType(number)}')

    # float
    number = 1.0
    print(f'number {number} is an instance of {runtimeType(number)}')

    # complex
    number = 1 + 0j
    print(f'number {number} is an instance of {runtimeType(number)}')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
