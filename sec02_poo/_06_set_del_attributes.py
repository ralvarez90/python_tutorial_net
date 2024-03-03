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


def show_example_1():
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
    show_example_1()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . .')
