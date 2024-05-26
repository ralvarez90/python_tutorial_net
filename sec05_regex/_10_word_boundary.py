"""REGEX WORD BOUNDARY  (LIMITES DE PALABRAS CON REGEX)

Podemos construir expresiones regulares que coincidan con las
posiciones de los limites de las palabras.

En expresiones regulares en Python, el \b se utiliza para 
representar un límite de palabra. Este coincide con el 
límite entre un carácter de palabra (alfanumérico o subrayado) y 
un carácter que no es de palabra en una cadena.

Por ejemplo, si tienes la expresión regular \bcat\b, coincidirá con 
la palabra "cat" solo si está precedida y seguida por un límite de 
palabra. Esto significa que coincidirá con "cat" en "The cat is black", 
pero no coincidirá con "cats" o "scatter".

En resumen, \b se usa para hacer coincidir palabras completas 
y no fragmentos de palabras dentro de una cadena.
"""
import re


def printSeparator(length: int = 50):
    print('-'*length)


def showExample01():
    print('EXAMPLE 01. Use "Python" pattern  in regex')
    s = 'CPython is the implementation of Python in C'
    print(f'Message: "{s}"')
    matches = re.finditer(r'Python', s)
    for m in matches:
        print(m.group())
    printSeparator()


def showExample02():
    print('EXAMPLE 02. Use \b word boundary in regex')
    s = 'CPython is the implementation of Python in C'
    print(f'Message: "{s}"')
    matches = re.finditer(r'\bPython\b', s)
    for m in matches:
        print(m.group())
    printSeparator()


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
