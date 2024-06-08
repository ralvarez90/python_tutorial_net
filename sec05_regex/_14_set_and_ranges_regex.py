"""REGEX SETS AND RANGES

Se emplean los corchetes [] para coincidir rangos o conjuntos de 
cualquier caracter. Ver ejemplo 01.

Los rangos se establecen de igual forma entre [] y se usa el
- para establecer el inicio y el fin del rango. Ver ejemplo 02.

Recordemos que el anchor ^ se emplea para matchear elementos 
al incio de un string, si se usa dentro de un [] se emplea como
operador de negación.
"""
import re


def printSeparator(length: int = 50):
    print('-'*length)


def showExample01():
    print('EXAMPLE 01. Using set [cs] to match c or s character')

    s = 'A licence or license'
    pattern = r'licen[cs]e'
    matches = re.finditer(pattern, s)
    for m in matches:
        print(m.group())

    printSeparator()


def showExample02():
    print('EXAMPLE 02. Using ranges in regex')

    s = 'Python'
    pattern1 = r'[aeiou]'
    pattern2 = r'[^aeiou]'

    for m in re.finditer(pattern1, s):
        print(m.group(), end=' ')

    print()

    for m in re.finditer(pattern2, s):
        print(m.group(), end=' ')


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
