"""DECIMAL MODULE

El módulo decimal permite redondear correctamente y de forma
optimizada números de punto flotante.

1. Clase Decimal
Crea objetos que repreentan números de con punto decimal, con
la característica que estos números se representan de manera
exacta, es decir no acarrea el error de redondeo de los 
float.

Son similares a los objetos BigDecimal en Java. Estos objetos Decimal
son asociados a determinados contextos, es decir siempre son asociados
- precisión durante operaciones aritmeéticas
- algoritmo de redondeo.

# todo - agregar notas sobre decimal context, getcontext y mecanismos
# todo - de redondeo ROUND_UP, ROUND_DOWN, ROUND_FLOOR, ...
"""
from decimal import Decimal


def showExample01():
    x, y, z = 0.1, 0.1, 0.1
    s = x+y+z
    print(f's = {s}')


def showExample02():
    x, y, z = Decimal('0.1'), Decimal('0.1'), Decimal('0.1')
    s = x+y+z
    print(f's = {s}')


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
