"""NÚMEROS

Tenemos diversis tipos de números. Extienden de object y son
int, float, complex.
"""


def runtime_type(obj: object) -> str:
    return str(type(obj))[8:-2]


def numbers_example():
    # int
    number = 1
    print(f'number {number} is an instance of {runtime_type(number)}')

    # float
    number = 1.0
    print(f'number {number} is an instance of {runtime_type(number)}')

    # complex
    number = 1+0j
    print(f'number {number} is an instance of {runtime_type(number)}')


if __name__ == '__main__':

    # numbers
    numbers_example()

    # end application
    input('\nPress any key to continue . . . ')
