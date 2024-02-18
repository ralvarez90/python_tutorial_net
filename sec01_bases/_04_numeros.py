"""NÚMEROS

Tenemos diversis tipos de números. Extienden de object y son
int, float, complex.
"""


def runtimeType(obj: object) -> str:
    return str(type(obj))[8:-2]


def numbersExample():
    # int
    number = 1
    print(f'number {number} is an instance of {runtimeType(number)}')

    # float
    number = 1.0
    print(f'number {number} is an instance of {runtimeType(number)}')

    # complex
    number = 1+0j
    print(f'number {number} is an instance of {runtimeType(number)}')


if __name__ == '__main__':

    # numbers
    numbersExample()

    # end application
    input('\nPress any key to continue . . . ')
