"""SINTAXIS

Se muestra ejemplo de sintaxis de Python.
"""
import keyword


def listKeywords():
    for kw in keyword.kwlist:
        print(kw)


def showExample01():
    # mensaje de bienvenida
    print('Hello World in Python3')

    # se muestran palabras reservadas
    listKeywords()


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
