"""INVERSE CHARACTER SETS

Los characters sets \d, \w y \s tienen inversos equivalentes a su
negación, que son \D, \W y \S.

\D
Matchea un caractere que no sea un dígito.

\W
Matchea cualquier caractere que no sea un word character.

\S
Matchea cualquier caracter que no sea un espacio en blanco.

re.sub
Se emplear para reemplazar del string a analizar los elementos
que matchen con la expresión regular, remplazando por el string
correspondiente al segundo argumento. Ver ejemplo 02.
"""

import re


def printSeparator(length: int = 50) -> None:
    print('-'*length)


def substractPhoneNumber(number: str) -> str:
    return re.sub(r'\D', '', number)


def showExample01():
    print('EXAMPLE 01. Using \D character set.')
    s = '+52-(561)-933-2500'
    print(f'String a matchear coincidencias: "{s}"')

    pattern = re.compile(r'\D')
    matches = re.finditer(pattern, s)
    for m in matches:
        print(m.group())

    printSeparator()


def showExample02():
    print('EXAMPLE 02. Using re.sub function')
    s = '+52-(561)-933-2500'

    phoneNumber = substractPhoneNumber(number=s)
    print(s)
    print(phoneNumber)
    printSeparator()


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
