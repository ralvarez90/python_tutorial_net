"""VARIABLES DE INSTANCIA

Son variables vinculados a los objetos de una clase. Cada objeto
tiene su propia copia de dichas variables de instancia.

Se pueden agregar variables de instancia de forma dinámica, afectando
a solo las instancias a las que se les agreguen o eliminen.
"""
from pprint import pprint


class HtmlDocument:

    # varianles de clase
    extension = 'html'
    version = 5


def main():

    # mostramos variables de clase y dict
    pprint(HtmlDocument.__dict__)

    # mostramos variables de instancia
    home = HtmlDocument()
    print(home.__dict__)
