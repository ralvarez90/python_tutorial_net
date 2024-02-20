"""MÓDULOS

Un módulo es una pieza de software que tiene una funcionalidad 
específica. Un módulo de Python es un archivo que contiene 
código Python. 

Cada módulo es un archivo de código fuente de Python 
independiente.

Uso de import
Para usar los objetos de otro módulo se emplea la sentencia 
import. La sitnaxis es de la forma:
import nombremodulo

Pude usar cada elementos dentro de un módulo de la forma
modulo.nombreObjecto
modulo.nombreFuncion()
etc...

Podemos asignar alias a los módulos usando la palabra reservada
as, esto sirve por si el nombre de nuestro módulo a importar
es muy grande.

Podemos importar todo un módulo o únicamente objetos específicos
de la forma
from nombreModulo import objeto1
"""
import sys


def mostrarModulosPython():
    for path in sys.path:
        print(path)


def main():
    mostrarModulosPython()


if __name__ == '__main__':

    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
