"""DYNAMIC TYPING

Recordemos que python cuenta con asignación de tipos dinámico. Es
decir el tipo de dato puede cambiar en tiempo de ejecución.

Para determinar el tipo de dato de un objeto podemos emplear la 
clase type, que nos otorga información sobre el tipo de dato
a partir del cual se construye.
"""


def runtimeType(obj: object) -> str:
    return str(type(obj))[8:-2]


def showExample01():
    someObjects: list[object] = [
        1,
        True,
        None,
        'Hello',
        1.1,
    ]

    for obj in someObjects:
        print(runtimeType(obj))


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
