"""DYNAMIC TYPING

Recordemos que python cuenta con asignación de tipos dinámico. Es
decir el tipo de dato puede cambiar en tiempo de ejecución.

Para determinar el tipo de dato de un objeto podemos emplear la 
clase type, que nos otorga información sobre el tipo de dato
a partir del cual se construye.
"""


def get_runtimetype(obj: object) -> str:
    return str(type(obj))[8:-2]


def main():
    some_objects: list[object] = [
        1,
        True,
        None,
        'Hello',
        1.1,
    ]

    for obj in some_objects:
        print(get_runtimetype(obj))


if __name__ == '__main__':

    # run app
    main()

    # end message
    input('\nPress any key to continue . . .')
