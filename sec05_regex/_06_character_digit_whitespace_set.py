"""CONJUNTOS DE CARACTERES

Un character set (o character class) es un conjunto de caracteres que
permiten construir expresiones regulares.

\d - digit character set
La expresión regular \d se emplea para representar un (digit character set)
que matchea un simple dígito del 0 al 9.

Empleamos \d\d para matchear cualquier conjunto de dos dígitos.

Podemos emplear quantificadores para acortar patrones dentro de una 
regex. Se establece en {}, por ejemplo \d\d\d\d es equivalente a
\d{4}

\w - word character set
Matchea cualquier caractere ascii, incluido el alfabeto latino y el _. Los
espacios en blanco y los puntos . no son incluidos. Ver ejemplo 3.

\s - withespace character set
Mathe cualquier espacio en blanco, inlcuidos tabulaciones, saltos de línea,
retorno de carro y tabulaciones verticales. Ver ejemplo 4.
"""
import re


def printSeparator(length: int = 50) -> None:
    print('-'*length)


def showExample01():
    print('EXAMPLE 01. Using r"\d" and finditer function')
    s = 'Python 3.0 was released in 2008'
    matches = re.finditer(r'\d', s)
    for m in matches:
        print(m.group())
    printSeparator()


def showExample02():
    print('EXAMPLE 02. Using r"\d\d" and r"\d\d\d\d" regex, finditer and group methods')
    s = 'Python 3.0 was released in 2008'

    r1 = re.compile(r'\d\d')
    r2 = re.compile(r'\d\d\d\d')

    matchesr1 = re.finditer(r1, s)
    matchesr2 = re.finditer(r2, s)

    print(f'Using {r1}')
    for m in matchesr1:
        print(m.group())

    print()

    print(f'Using {r2}')
    for m in matchesr2:
        print(m.group())

    printSeparator()


def showExample03():
    print('EXAMPLE 03. Use \w word character set.')
    s = 'Python 3.0'
    matches = re.finditer(r'\w', s)
    for m in matches:
        print(m.group())
    printSeparator()


def showExample04():
    print('EXAMPLE 04. Use \s whitespace character set')
    s = 'Python 3.10'
    matches = re.finditer(pattern=r'\s', string=s)
    for m in matches:
        print(m)
    printSeparator()


def main():
    showExample01()
    showExample02()
    showExample03()
    showExample04()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
