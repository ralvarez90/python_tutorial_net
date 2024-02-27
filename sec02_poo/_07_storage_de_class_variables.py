"""ALMACENAMIENTO DE VARIABLES
DE CLASE

Python almacena las variables de clase dentro de
una clase dentro de su atributo __dict__ del
tipo mapping proxy que exitende de dict.

Python no permite manipular directamente este atributo
de las clases __dict__ pero se puede usar setattr
hacer la creación de varianles de clase de forma dinámica
como hemos visto.
"""
from pprint import pprint


class HtmlDocument:
    extension = 'html'
    version = 5


# extenemos con propiedad
HtmlDocument.mediaType = 'text/html'

if __name__ == '__main__':
    pprint('HtmlDocument.__dict__')
    pprint(HtmlDocument.__dict__)
