"""OPERADOR MÓDULO

El operador % entre dos enteros retorna el residuo resultado
al dividir dos enteros.

Este operador es útil ya que nos permite saber múltiplos, generar
criterios de paridad e imparidad, y nos permite convertir unidades.
"""
from math import floor


def runtime_type(obj: object) -> str:
    return str(type(obj))[8:-2]


def is_even(n: int) -> bool:
    return n % 2 == 0


def is_odd(n: int) -> bool:
    return n % 2 != 0


def get_time(total_seconds: int) -> int:
    return {
        'days': floor(total_seconds / 60 / 60 / 24),
        'hours': floor(total_seconds/60/60) % 24,
        'minutes': floor(total_seconds/60) % 60,
        'seconds': total_seconds % 60,
    }


def show_example_01():
    # test de paridad
    n: int = int(input('Ingrese un entero: '))
    print(f'{n} es par' if is_even(n) else f'{n} es impar')


def show_example_02():
    some_seconds = 93_750
    print(f'Conversión de {some_seconds} segundos')
    print(get_time(some_seconds))


def main():
    show_example_01()
    show_example_02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
