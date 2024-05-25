"""ANCHORS

Las expresiones regulares le proporcionan dos anclajes (anclas) que
permiten coincidir con las posiciones de los caracteres:

^ este caracter llamado (caret) o asento circunflejo coincide con
el comienzo de un string

$ el dollar anchor coincide con el final de un string.
"""
import re


def printSeparator(length: int = 50):
    print('-'*length)


def showExample01():
    print('EXAMPLE 01. Use ^ regex anchor with two digits')
    time = '14:30 hrs'

    # equivalent \d\d
    print('Using "\d\d"')
    r1 = re.compile(r'\d{2}')
    for m in re.finditer(pattern=r1, string=time):
        print(m.group())

    # equivalte ^\d\d
    print('Using "^\d\d"')
    r2 = re.compile(r'^\d{2}')
    for m in re.finditer(pattern=r2, string=time):
        print(m.group())

    printSeparator()


def showExample02():
    print('EXAMPLE 02. Using $ regex anchor.')
    time = '12:20'
    matches = re.finditer('\d\d$', time)
    for m in matches:
        print(m.group())

    printSeparator()


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
