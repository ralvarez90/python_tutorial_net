"""EXPRESIONES REGULARES

Una regex es una secuencia de caracteres que especifica un patrón
de búsqueda.

Estas son independientes a los lengujes de programación. Para 
interactuar con expresiones regulares empleamos el módulo re.

El patrón \d matchea cualquier dígito entre el 0 y el 9. Podemos
usar regex directamente o compilarlas con el método re.compile
cuando se van a usar de forma recurrente.

1. re.compile
Retorna un objeto Patter a partir de un patrón.

2. re.findall
Retorna una lista de las coincidencias del patrón que invoca
dentro del string que recibe como argumento.
"""
import re


def showExample01():

    # regex patter
    pattern = re.compile(r'\d')

    # string to search
    string = 'Python 3.10 was released on October 04, 2021'

    # find all matches
    results = pattern.findall(string)
    print(results)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
