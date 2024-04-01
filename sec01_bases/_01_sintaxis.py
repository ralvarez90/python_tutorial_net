"""SINTAXIS

Se muestra ejemplo de sintaxis de Python.
"""
import keyword


def list_keywords():
    for kw in keyword.kwlist:
        print(kw)


def show_example_01():
    # mensaje de bienvenida
    print('Hello World in Python3')

    # se muestran palabras reservadas
    list_keywords()


def main():
    show_example_01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
