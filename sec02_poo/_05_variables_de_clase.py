"""VARIABLES DE CLASE

Recordemos que las clases también son objetos, cuando 
definimos una clase empleando (class) se crea un objeto
con el mismo nombre de la clase.

Las clases son instancias de la clase type. Las variables
de clase se vinculan al resto de instancias de una clase
por lo que son accesibles desde el nombre de la clase o
desde cada una de las instancias.

Si se desea acceder a una variabla de clase o atributo
que no existe se lanza la excepción AttributeError.
"""


class HtmlDocument:
    """Crea una clase y un objeto con el mismo nombre. Tiene variables
    de clase.
    """
    extension = 'html'
    version = '5'


def showExample01():
    print(f'{HtmlDocument.__name__}')

    # test de instancia
    print(isinstance(HtmlDocument, type))

    # instsancias
    indexDoc = HtmlDocument()
    print(HtmlDocument.extension)
    print(HtmlDocument.version)
    print(indexDoc.extension)
    print(indexDoc.version)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
