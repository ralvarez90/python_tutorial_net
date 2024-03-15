"""FUNCIONES RECURSIVAS

Son aquellas funciones que se invocan así mismo en su interior.
Requieren una condición base para que la función pueda decidir
cuando ya no invocarse.
"""


def count_down_01(n: int):
    assert n >= 0 and n is not None, 'n can not be < 0 or None'
    if n == 0:
        print('Adios!')
    else:
        print(n)
        count_down_01(n - 1)


def count_down_02(n: int):
    assert n >= 0 and n is not None, 'n can not be < 0 or None'
    print(n)
    next = n - 1
    if next > 0:
        count_down_02(next)


def get_sum_01(n: int) -> int:
    """sum(n) = 1+2+...+n
    sum(n) = n + sum(n-1)"""
    if n > 0:
        return n + get_sum_01(n - 1)
    return 0


def get_sum_02(n: int) -> int:
    assert n >= 0 and n is not None, 'n can not be a negative or None'
    return n + get_sum_02(n - 1) if n > 0 else 0


def show_example_01():
    # ejemplo 1
    count_down_01(10)
    print()

    # ejemplo 2
    count_down_02(10)
    print()

    # ejemplo 3
    print(f'sum(1+2+...+5000) -> {get_sum_01(500)}')


def main():
    show_example_01()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
