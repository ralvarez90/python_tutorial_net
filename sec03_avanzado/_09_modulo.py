"""OPERADOR MÓDULO

El operador % entre dos enteros retorna el residuo resultado
al dividir dos enteros.

Este operador es útil ya que nos permite saber múltiplos, generar
criterios de paridad e imparidad, y nos permite convertir unidades.
"""
from math import floor


def runtimeType(obj: object) -> str:
    return str(type(obj))[8:-2]


def isEven(n: int) -> bool:
    return n % 2 == 0


def isOdd(n: int) -> bool:
    return n % 2 != 0


def getTime(seconds: int) -> int:
    return {
        'days': floor(seconds / 60 / 60 / 24),
        'hours': floor(seconds/60/60) % 24,
        'minutes': floor(seconds/60) % 60,
        'seconds': seconds % 60,
    }


def showExample01():
    # test de paridad
    n: int = int(input('Ingrese un entero: '))
    print(f'{n} es par' if isEven(n) else f'{n} es impar')


def showExample02():
    someSeconds = 93_750
    print(f'Conversión de {someSeconds} segundos')
    print(getTime(someSeconds))


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
