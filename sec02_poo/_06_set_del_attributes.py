"""ATRIBUTOS

setattr
Podemos cambiar el estado e atributos de clase o de instancia
de forma directao o empleando el método setattr.

delattr
Podemos eliminar un atributo de un objeto empleando la función
delattr
"""


class HmtlDocument:
    extension = 'html'


if __name__ == '__main__':

    # accedemos a atribitos
    print(f'Extension document: {HmtlDocument.extension}')

    # set atributte form 1
    HmtlDocument.filename = 'index'

    # establecemos atributo de clase
    setattr(HmtlDocument, 'version', 5)
    print(f'Html version: {HmtlDocument.version}')

    # eliminamos atributo
    delattr(HmtlDocument, 'filename')
