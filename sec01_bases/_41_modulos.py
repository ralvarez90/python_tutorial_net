"""MÓDULOS

Son piezas de código acotadas por un espacio de nombres. Un
archivo python es un módulo. El conjunto de módulos se denomina
paquete. 
"""
import sys


def mostrarModulosPython():
    for path in sys.path:
        print(path)


if __name__ == '__main__':

    # run example
    mostrarModulosPython()

    # end application
    input('\nPress any key to continue . . . ')
