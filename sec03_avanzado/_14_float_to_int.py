"""CONVERSIÓN DE FLOTANTES A INT

Python nos provee de 3 mecanismos para obtener valores enteros
a partir de números flotantes.

1. Función trunc
Retorna la parte entera de un número. Ingora la parte con
punto decimal. Esta función se encuentra dentro del módulo
math.

2. Constructor de int
De forma similar, el constructor de int retorna la parte
entera de un flotante.

3. Función piso
La función piso (floor) del módulo math igualmente retorna
el entero <= al flotante o número que recibe como
argumento.

4. Función ceil (techo)
Retorna el entero >= al que recibe como argumento.

Notas:
- Verificar comportamiento cuando floor y ceil reciban
números negativos.
"""
from math import trunc, floor


def showExample01():
    someNums: list[float] = [
        12.2, 12.5, 12.7,
    ]
    for nf in someNums:
        print(f'trunc({nf}) -> {trunc(nf)}')
        print(f'  int({nf}) -> {int(nf)}')
        print(f'floor({nf}) -> {floor(nf)}')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue. . .')
