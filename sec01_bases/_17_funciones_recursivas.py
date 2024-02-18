"""FUNCIONES RECURSIVAS

Son aquellas funciones que se invocan así mismo en su interior.
Requieren una condición base para que la función pueda decidir
cuando ya no invocarse.
"""


def count_down_v1(n: int):
    assert n >= 0, 'n can not be < 1'
    if n == 0:
        print('Adios!')
    else:
        print(n)
        count_down_v1(n-1)


def count_down_v2(n: int):
    print(n)
    next = n-1
    if next > 0:
        count_down_v2(next)


def get_sum_v1(n: int) -> int:
    """sum(n) = 1+2+...+n
    sum(n) = n + sum(n-1)"""
    if n > 0:
        return n + get_sum_v1(n-1)
    return 0


def get_sum_v2(n: int) -> int:
    assert n >= 0, 'n can not be a negative'
    return n+get_sum_v2(n-1) if n > 0 else 0


if __name__ == '__main__':

    # count down
    count_down_v1(10)
    print()

    # count down
    count_down_v2(10)
    print()

    # get sum
    print(f'sum(1+2+...+5000) -> {get_sum_v1(500)}')
    print(f'sum(1+2+...+5000) -> {get_sum_v2(500)}')

    # end application
    input('\nPress any key to continue . . . ')
