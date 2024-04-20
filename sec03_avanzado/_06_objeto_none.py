"""OBJETO NONE

Objeto que representa la referencia nula. Este es un objeto especial
instance de la clase NoneType. Este objeto se emplear para establecer
un estado de nulidad a cualquier objeto.

El objeto None es un singleton de la clase NoneType, lo que quiere decir
que solo existe una única instancia de dicha clase. Puede usar el operador
== y el operador is para comparar este valor.

Se concidera buena práctica usar el operador is e is not para comparar el
objeto None.

Método __eq__
Los objetos definidos por el usuario pueden cambiar el comportamiento del
operador == implementando el método __eq__ en su correspondiente clase. Esto
permite comprar objetos de clases definidas por el usuario con el operador
==.

El operador is no se puede sobrescribir.
"""


def runtimeType(obj: object) -> str:
    return str(type(obj))[8:-2]


def showExample01():
    # info del objeto None
    print(
        f'The object {None} has a id: {hex(id(None))} and type: {runtimeType(None)}')

    # uso de is y ==
    print(f'None is None: {None is None}')
    print(f'None == None: {None == None}')

    class Apple:
        def __eq__(self, __value: object) -> bool:
            return True

    # retorna true en cualquier caso
    a1 = Apple()
    print(a1 == None)
    print(a1 == 123)
    print(a1 == 'Hello World!')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue. . . ')
