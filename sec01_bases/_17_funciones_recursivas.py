"""FUNCIONES RECURSIVAS

Son aquellas funciones que se invocan así mismo en su interior.
Requieren una condición base para que la función pueda decidir
cuando ya no invocarse.
"""


def countDown01(n: int):
    assert n >= 0 and n is not None, 'n can not be < 0 or None'
    if n == 0:
        print('Adios!')
    else:
        print(n)
        countDown01(n - 1)


def countDown02(n: int):
    assert n >= 0 and n is not None, 'n can not be < 0 or None'
    print(n)
    next = n - 1
    if next > 0:
        countDown02(next)


def getSum01(n: int) -> int:
    """sum(n) = 1+2+...+n
    sum(n) = n + sum(n-1)"""
    if n > 0:
        return n + getSum01(n - 1)
    return 0


def getSum02(n: int) -> int:
    assert n >= 0 and n is not None, 'n can not be a negative or None'
    return n + getSum02(n - 1) if n > 0 else 0


def showExample01():
    # ejemplo 1
    countDown01(10)
    print()

    # ejemplo 2
    countDown02(10)
    print()

    # ejemplo 3
    print(f'sum(1+2+...+5000) -> {getSum01(500)}')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
