"""VARIABLES DE INSTANCIA

Son variables vinculados a los objetos de una clase. Cada objeto
tiene su propia copia de dichas variables de instancia.

Se pueden agregar variables de instancia de forma dinámica, afectando
a solo las instancias a las que se les agreguen o eliminen.

Se les dicen atributos a las las variables de instancia. Recordar que
python almacena todas las variables de instancia en el atributo
__dict__ de la instancia.
"""
from pprint import pprint


class HtmlDocument:
    # variables de clase
    extension = 'html'
    version = 5


def showExample01():
    # mostramos variables de clase y dict
    pprint(HtmlDocument.__dict__)

    # mostramos variables de instancia
    home = HtmlDocument()
    print(home.__dict__)

    # agregamos variable de instancia
    home.media_type = 'text/html'
    print(home.__dict__)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue. . .')
