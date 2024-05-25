"""DOT CHARACTER SET

El caracter . matchea con cualquier caracter distinto al 
salto de línea.
"""
import re


def printSeparator(length: int = 50) -> None:
    print('-'*length)


def showExample01():
    print('EXAMPLE 01. Use the dot (.) character set')

    strContent = 'Python\n4'
    matches = re.finditer(r'.', strContent)
    for m in matches:
        print(m.group(), end=' ')
    print()

    printSeparator()


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
