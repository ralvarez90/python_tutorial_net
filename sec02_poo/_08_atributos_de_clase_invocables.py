"""ATRIBUTOS DE CLASE INVOCABLES

Recordemos que en python todo es un objeto, por lo que
como variables de clase podemos tener objetos function.

Cuando agrega una función a una clase esta se convierte
en un atributo de clase. Dado que una función es un  objeto
invocable, entonces el atributo de clase se denomina
atributo de clase (o variable de clase) invocable.
"""
from pprint import pprint


class HtmlDocument:
    extension = 'html'
    version = 5

    def render():
        print('Rendering the Html document...')


if __name__ == '__main__':

    # mostrmos __dict__ de la clase
    pprint(HtmlDocument.__dict__)

    # instancia
    index = HtmlDocument()
    
    # callable variable class
    HtmlDocument.render()
