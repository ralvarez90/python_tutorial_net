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


def main():

    # test de paridad
    n: int = int(input('Ingrese un entero: '))
    print(f'{n} es par' if is_even(n) else f'{n} es impar')

    # separador
    print('-'*50)

    # uso de operador módulo
    some_seconds = 93_750
    print(f'Conversión de {some_seconds} segundos')
    print(get_time(some_seconds))


if __name__ == '__main__':

    # run app
    main()

    # end message
    input('\nPress any key to continue . . .')
