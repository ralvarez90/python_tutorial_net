"""NÚMEROS

Representan valores numéricos enteros y con decimales. Exsisten
en python los tipos int, float y complex.
"""


def runtime_type(obj: object) -> str:
    return str(type(obj))[8:-2]


def show_example_01():
    # int
    number = 1
    print(f'number {number} is an instance of {runtime_type(number)}')

    # float
    number = 1.0
    print(f'number {number} is an instance of {runtime_type(number)}')

    # complex
    number = 1 + 0j
    print(f'number {number} is an instance of {runtime_type(number)}')


def main():
    show_example_01()


if __name__ == '__main__':
    # run application
    main()

    # end application
    input('\nPress any key to continue . . . ')
