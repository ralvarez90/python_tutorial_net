"""ATRIBUTOS

setattr
Podemos cambiar el estado e atributos de clase o de instancia
de forma dinámica y en tiempo de ejecución empleando el método 
setattr.

delattr
Podemos eliminar un atributo de un objeto empleando la función
delattr.
"""


class HmtlDocument:
    extension = 'html'


def showExample01():
    # accedemos a atribitos
    print(f'Extension document: {HmtlDocument.extension}')

    # set atributte form 1
    HmtlDocument.filename = 'index'

    # establecemos atributo de clase
    setattr(HmtlDocument, 'version', 5)
    print(f'Html version: {HmtlDocument.version}')

    # eliminamos atributo
    delattr(HmtlDocument, 'filename')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
